from page_object.base_components.base_form import ConfirmDialogForm


class MainMenu:
    ITEM_XPATH = "//ul/a"
    CONCRETE_ITEM_BY_TEXT_XPATH = "//a[.//span[text()='{text}']]"
    LOG_OUT_BUTTON_XPATH = "//div[./div/span[@class='userName']]//div[@role='button']/div"

    def __init__(self, browser):
        self.browser = browser

    def get_all_items(self):
        items = self.browser.find_by_xpath(self.ITEM_XPATH)
        texts = []

        for item in items:
            texts.append(item.text)

        return texts

    def select(self, text):
        self.browser.find_by_xpath(self.CONCRETE_ITEM_BY_TEXT_XPATH.format(text=text)).click()

    def log_out(self):
        self.browser.find_by_xpath(self.LOG_OUT_BUTTON_XPATH).click()

    def log_out_confirm(self):
        ConfirmDialogForm(self.browser).submit_form()

    def wait_for_log_out(self):
        self.browser.is_element_not_present_by_xpath(self.LOG_OUT_BUTTON_XPATH)
