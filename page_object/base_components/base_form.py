from page_object.base_components.base_element import BaseElement


class BaseForm(BaseElement):
    ROOT = "//div[@role='dialog']"

    HEADER_LABEL = "./div/h6"

    CLOSE_BUTTON = ".//button[@aria-label='close']"
    CANCEL_BUTTON = ".//button[./span/p[text()='Cancel']]"
    SUBMIT_BUTTON = "./div/div/span[last()]/button[.//p[text()]][last()]"
    SUBMIT_BUTTON_TEXT = ".//p"

    def is_shown(self):
        return (len(self.browser.find_by_xpath(self.ROOT)) > 0 and
                len(self._get_root().find_by_xpath(self.HEADER_LABEL)) > 0 and
                len(self._get_root().find_by_xpath(self.CLOSE_BUTTON)) > 0 and
                len(self._get_root().find_by_xpath(self.CANCEL_BUTTON)) > 0 and
                len(self._get_root().find_by_xpath(self.SUBMIT_BUTTON)) > 0)

    def get_header_text(self):
        return self._get_root().find_by_xpath(self.HEADER_LABEL).text

    def get_submit_button_text(self):
        return self._get_root().find_by_xpath(self.SUBMIT_BUTTON).find_by_xpath(self.SUBMIT_BUTTON_TEXT).value

    def submit_form(self):
        self._get_root().find_by_xpath(self.SUBMIT_BUTTON).click()

    def close_form(self):
        self._get_root().find_by_xpath(self.CLOSE_BUTTON).click()

    def cancel_form(self):
        self._get_root().find_by_xpath(self.CANCEL_BUTTON).click()


class BaseInputForm(BaseForm):
    ROOT = "//div[@role='presentation' and not(@aria-hidden='true')]//div[@role='dialog']"
    INPUT = ".//input[@type='text']"

    def is_shown(self):
        return super().is_shown() and len(self._get_root().find_by_xpath(self.INPUT)) > 0

    def type(self, text):
        self._get_root().find_by_xpath(self.INPUT).clear()
        self._get_root().find_by_xpath(self.INPUT).type(text)


class ConfirmDialogForm(BaseForm):
    SUBMIT_BUTTON = "./div/span[last()]/button[.//p[text()]]"
    DESC_XPATH = ".//p[@id='alert-dialog-description']"

    def get_description(self):
        return self._get_root().find_by_xpath(self.DESC_XPATH).text


class AutoCompleteInputForm(BaseInputForm):
    ROOT = "//div[@role='dialog']"
    OPTION_VALUE = "//ul/li[@role='option']"
    OPTION_BY_TEXT = "//ul/li[@role='option' " \
                     "and (./p[normalize-space(text()) = '{text}'] or normalize-space(text()) = '{text}')]"

    def select_option(self, option):
        self._get_root().find_by_xpath(self.OPTION_BY_TEXT.format(text=option)).click()
