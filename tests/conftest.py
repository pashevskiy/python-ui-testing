import logging
import pytest
import yaml

from selenium.webdriver.chrome.options import Options
from utils.database import GTDatabase


def pytest_addoption(parser):
    parser.addoption('--demo', action='store_true', help='Start in Demo mode')
    parser.addoption('--containerized', action='store_true', help='Start in containerized mode')
    parser.addoption('--headless', action='store_true', help='Start in headless mode')
    parser.addoption('--env', action="store", type=str, help='Use specified environment')


@pytest.fixture(scope='session')
def get_config(file="config.yaml"):
    with open(file, "r") as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.FullLoader)


@pytest.fixture(scope='session')
def get_env_config(request, get_config):
    if request.config.getoption("--env"):
        return get_config[request.config.getoption("--env")]
    return get_config["default"]


@pytest.fixture(scope='session')
def splinter_selenium_speed(request, get_config):
    if request.config.getoption("--demo"):
        return 1
    if get_config["system"]["demo_mode"]:
        return 1
    return 0


@pytest.fixture(scope='session')
def splinter_webdriver(get_config):
    return get_config["webdriver"]["browser"]


@pytest.fixture(scope='session')
def splinter_session_scoped_browser():
    return False


@pytest.fixture(scope='session')
def splinter_selenium_implicit_wait():
    return 1


@pytest.fixture(scope='session')
def splinter_wait_time():
    return 2


@pytest.fixture(scope='session')
def splinter_headless(request, get_config):
    return get_config["webdriver"]["headless"] or request.config.getoption("--headless")


@pytest.fixture(scope='session')
def database(get_env_config) -> GTDatabase:
    return GTDatabase(get_env_config["database"])


@pytest.fixture(scope='session')
def tmpdir_session(request, tmpdir_factory):
    """A tmpdir fixture for the session scope. Persists throughout the pytest session."""
    return tmpdir_factory.mktemp(request.session.name)


@pytest.fixture(scope='session')
def splinter_driver_kwargs(request, get_config, tmpdir_session):
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": str(tmpdir_session),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True})

    if request.config.getoption("--containerized") or get_config["system"]["containerized"]:
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
    return {"options": options}


@pytest.fixture(scope='session')
def splinter_screenshot_dir():
    return "./reports/screenshots"


# URLs
@pytest.fixture()
def url(get_env_config):
    return get_env_config["url"]


@pytest.fixture()
def grand_tenders_accounts(get_env_config):
    return get_env_config["accounts"]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            #TODO
            #ADD Screenshot and source code links to the report
            extra.append(pytest_html.extras.html('<div>...</div>'))
        report.extra = extra


# Logging
def pytest_bdd_after_step(step):
    logging.getLogger().info("\tStep is completed: {step}".format(step=step))


def pytest_bdd_before_scenario(feature, scenario):
    logging.getLogger().info("Scenario is starting: {feature} : {scenario}".format(
                                scenario=scenario.name, feature=feature.name))

def pytest_bdd_step_error(step):
    logging.getLogger().error("\tStep is failed: {step}".format(step=step))
