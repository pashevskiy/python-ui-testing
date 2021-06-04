from pytest_bdd import given, parsers, then, when
from page_object.login_page import LoginPage


@given("I am on LogIn page", target_fixture="login_page")
def visit_log_in_page(browser, url):
    login_page = LoginPage(browser, url)
    return login_page


@given(parsers.parse("I successfully logged in as \"{text}\" user"), target_fixture="page")
@given(parsers.parse("I successfully logged in MyService as \"{text}\" user"), target_fixture="page")
def successfully_logged_in_as(browser, text, grand_tenders_accounts, grand_tenders_url):
    login_page = LoginPage(browser, grand_tenders_url)
    page = login_page.successfull_log_in(grand_tenders_accounts[text]["login"], grand_tenders_accounts[text]["password"])
    assert page.is_shown()
    return page


@when(parsers.parse("I type \"{text}\" in email input"))
def type_in_email_input(login_page: LoginPage, text):
    login_page.set_login(text)


@when(parsers.parse("I type \"{text}\" in password input"))
def type_in_password_input(text, login_page):
    login_page.set_password(text)


@when("I click on Log In button")
def click_on_log_in_button(login_page: LoginPage):
    login_page.click_on_log_in_button()


@then(parsers.parse("I submit LogIn form and get \"{text}\" alerts"))
def submit_log_in_form_and_get_error(text, login_page):
    login_page.click_on_log_in_button()
    assert login_page.get_alert_messages() == text.split(",")


@when("I click on registration button")
def click_on_registration(login_page: LoginPage):
    login_page.click_on_registration_button()


@when("I click on forgot password button")
def click_on_forgot_password(login_page: LoginPage):
    login_page.click_on_forgot_password_button()


@when("I click on submit registration form button")
def submit_registration_form(login_page: LoginPage):
    login_page.click_on_submit_registration_button()


@when("I click on exit registration form button")
def exit_registration_form(login_page: LoginPage):
    login_page.click_on_exit_registration_button()


@when("I click on submit forgot password form button")
def submit_forgot_password_form(login_page: LoginPage):
    login_page.click_on_submit_forgot_password_button()


@when("I click on exit forgot password form button")
def exit_forgot_password_form(login_page: LoginPage):
    login_page.click_on_exit_forgot_password_button()


@when(parsers.parse("I type \"{text}\" in full name input"))
def type_in_full_name_input(login_page: LoginPage, text):
    login_page.type_in_full_name_input(text)


@when(parsers.parse("I type \"{text}\" in password confirm input"))
def type_in_password_confirm_input(login_page: LoginPage, text):
    login_page.type_in_password_confirm_input(text)


@then(parsers.parse("Email input returns \"{text}\" validation error"))
def get_email_validation_error(login_page: LoginPage, text):
    assert login_page.get_email_validation_error() == text


@then(parsers.parse("Full name input returns \"{text}\" validation error"))
def get_full_name_validation_error(login_page: LoginPage, text):
    assert login_page.get_full_name_validation_error() == text


@then(parsers.parse("Password input returns \"{text}\" validation error"))
def get_password_validation_error(login_page: LoginPage, text):
    assert login_page.get_password_validation_error() == text


@then(parsers.parse("Password-confirm input returns \"{text}\" validation error"))
def get_password_confirm_validation_error(text, login_page: LoginPage):
    assert login_page.get_password_confirm_validation_error() == text


@then("Login page is shown")
def login_page_is_shown(login_page: LoginPage):
    assert login_page.is_shown()


@then("Registration page is shown")
def registration_page_is_shown(login_page: LoginPage):
    assert login_page.registration_page_is_shown()


@then("Forgot password page is shown")
def forgot_password_page_is_shown(login_page: LoginPage):
    assert login_page.forgot_password_page_is_shown()
