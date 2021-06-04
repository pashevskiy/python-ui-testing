from sttable import parse_str_table
from pytest_bdd import parsers, then, when
from page_object.base_components.base_page import BasePage
from page_object.base_components.base_form import BaseInputForm, BaseForm, ConfirmDialogForm, AutoCompleteInputForm


@when(parsers.parse("I fill in and submit simple form with \"{value}\" value"))
def fill_in_and_submit_simple_form(browser, value):
    form = BaseInputForm(browser)
    form.type(value)
    form.submit_form()
    form.wait_loading_is_done()


@then(parsers.parse("I check that system returned \"{alert}\" alert(s)"))
def check_system_alerts(alert, page: BasePage):
    assert page.get_alert_messages() == alert.split(";")


@then(parsers.parse("I check that system returned alerts:\n{table}"))
def check_system_alerts(page: BasePage, table):
    expected = parse_str_table(table, table_with_header=False)
    expected_arr = []
    for value in expected.rows:
        expected_arr.append(value['0'])
    current = page.get_alert_messages()
    assert current == expected_arr, (
        "Expected: {expected}\nCurrent: {current}".format(expected=expected_arr,
                                                          current=current))


@when(parsers.parse("I select \"{tab}\" tab on page"))
def select_tab_on_page(page: BasePage, tab):
    page.click_on_tab(tab)


# Forms
@when("I submit the form")
def submit_form(browser):
    form = BaseForm(browser)
    form.submit_form()
    form.wait_loading_is_done()


@then(parsers.parse("I check that \"{header}\" alert is shown"))
def check_that_alert_is_shown(browser, header):
    form = ConfirmDialogForm(browser)
    assert form.is_shown()
    assert form.get_header_text() == header


@when("I submit confirm dialog")
def submit_confirm_dialog(browser):
    form = ConfirmDialogForm(browser)
    form.submit_form()
    form.wait_loading_is_done()
