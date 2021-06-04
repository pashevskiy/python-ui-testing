from page_object.base_components.base_page import BasePage
from page_object.positions_page_elements.positions_page import PositionsPage


class LoginPage(BasePage):
    # Login form
    EMAIL_INPUT_XPATH = "//input[@name='email']"
    EMAIL_VALIDATION_ERROR_XPATH = "//div[.//input[@name='email']]/p"
    PASSWORD_INPUT_XPATH = "//input[@name='password']"
    PASSWORD_VALIDATION_ERROR_XPATH = "//div[.//input[@name='password']]/p"
    REMEMBER_ME_XPATH = "//input[@name='rememberMe']"
    SUBMIT_BUTTON_XPATH = "//button[./span/p[text()='LogIn']]"
    REGISTRATION_BUTTON_XPATH = "//button[text()='Registration']"
    FORGOT_PASSWORD_BUTTON_XPATH = "//button[text()='Forgot password?']"
    ALLERT_MESSAGE_XPATH = "//div[@role='alertdialog']/div"

    # Registration form
    # email and password can be used from main form
    FULL_NAME_INPUT_XPATH = "//input[@name='fullName']"
    FULL_NAME_VALIDATION_ERROR_XPATH = "//div[.//input[@name='fullName']]/p"

    PASSWORD_CONFIRM_INPUT_XPATH = "//input[@name='password-confirm']"
    PASSWORD_CONFIRM_VALIDATION_ERROR_XPATH = "//div[.//input[@name='password-confirm']]/p"

    SUBMIT_REGISTRATION_FORM_BUTTON_XPATH = "//button[./span/p[text()='Register']]"
    EXIT_REGISTRATION_FORM_BUTTON_XPATH = "//button[text()='Выйти']"
    SUBMIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH = "//button[./span/p[text()='Send']]"
    EXIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH = "//button[text()='Выйти']"

    def __init__(self, browser, url):
        self.browser = browser
        self.browser.visit(url)

    def is_shown(self):
        return (self.browser.is_element_present_by_xpath(self.EMAIL_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(self.PASSWORD_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(self.REMEMBER_ME_XPATH)
                and self.browser.is_element_present_by_xpath(self.FORGOT_PASSWORD_BUTTON_XPATH)
                and self.browser.is_element_present_by_xpath(self.REGISTRATION_BUTTON_XPATH)
                and self.browser.is_element_present_by_xpath(self.SUBMIT_BUTTON_XPATH))

    def registration_page_is_shown(self):
        return (self.browser.is_element_present_by_xpath(self.EMAIL_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(self.PASSWORD_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(self.FULL_NAME_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(self.PASSWORD_CONFIRM_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(
                    self.EXIT_REGISTRATION_FORM_BUTTON_XPATH)
                and self.browser.is_element_present_by_xpath(self.SUBMIT_REGISTRATION_FORM_BUTTON_XPATH))

    def forgot_password_page_is_shown(self):
        return (self.browser.is_element_present_by_xpath(self.EMAIL_INPUT_XPATH)
                and self.browser.is_element_present_by_xpath(
                    self.SUBMIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH)
                and self.browser.is_element_present_by_xpath(
                    self.EXIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH))

    def set_login(self, login):
        self.browser.find_by_xpath(self.EMAIL_INPUT_XPATH).type(login)

    def set_password(self, password):
        self.browser.find_by_xpath(self.PASSWORD_INPUT_XPATH).type(password)

    def click_on_log_in_button(self):
        self.browser.find_by_xpath(self.SUBMIT_BUTTON_XPATH).click()

    def uncheck_remember_me_checkbox(self):
        self.browser.find_by_xpath(self.REMEMBER_ME_XPATH).uncheck()

    def get_login_validation_error(self):
        return self.browser.find_by_xpath(self.EMAIL_VALIDATION_ERROR_XPATH).text

    def get_alert_messages(self):
        return list(map(lambda x: x.text,
                        self.browser.find_by_xpath(self.ALLERT_MESSAGE_XPATH)))

    def successfull_log_in(self, login, password):
        self.browser.is_element_present_by_xpath(self.EMAIL_INPUT_XPATH, 10)
        self.set_login(login)
        self.set_password(password)
        self.uncheck_remember_me_checkbox()
        self.click_on_log_in_button()
        return PositionsPage(self.browser)

    # Registration form
    def click_on_registration_button(self):
        self.browser.find_by_xpath(self.REGISTRATION_BUTTON_XPATH).click()

    def type_in_full_name_input(self, text):
        self.browser.find_by_xpath(self.FULL_NAME_INPUT_XPATH).type(text)

    def get_full_name_validation_error(self):
        return self.browser.find_by_xpath(self.FULL_NAME_VALIDATION_ERROR_XPATH).text

    def type_in_email_input(self, text):
        self.browser.find_by_xpath(self.EMAIL_INPUT_XPATH).type(text)

    def get_email_validation_error(self):
        return self.browser.find_by_xpath(self.EMAIL_VALIDATION_ERROR_XPATH).text

    def type_in_password_input(self, text):
        self.browser.find_by_xpath(self.PASSWORD_INPUT_XPATH).type(text)

    def get_password_validation_error(self):
        return self.browser.find_by_xpath(self.PASSWORD_VALIDATION_ERROR_XPATH).text

    def type_in_password_confirm_input(self, text):
        self.browser.find_by_xpath(self.PASSWORD_CONFIRM_INPUT_XPATH).type(text)

    def get_password_confirm_validation_error(self):
        return self.browser.find_by_xpath(self.PASSWORD_CONFIRM_VALIDATION_ERROR_XPATH).text

    def click_on_submit_registration_button(self):
        self.browser.find_by_xpath(self.SUBMIT_REGISTRATION_FORM_BUTTON_XPATH).click()

    def click_on_exit_registration_button(self):
        self.browser.find_by_xpath(self.EXIT_REGISTRATION_FORM_BUTTON_XPATH).click()

    # Forgot password form
    def click_on_forgot_password_button(self):
        self.browser.find_by_xpath(self.FORGOT_PASSWORD_BUTTON_XPATH).click()

    def click_on_submit_forgot_password_button(self):
        self.browser.find_by_xpath(self.SUBMIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH).click()

    def click_on_exit_forgot_password_button(self):
        self.browser.find_by_xpath(self.EXIT_FORGOT_PASSWORD_FORM_BUTTON_XPATH).click()
