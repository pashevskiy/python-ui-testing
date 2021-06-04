from page_object.base_components.base_page import BasePage


class PositionsPage(BasePage):
    ADD_POSITION_BUTTON_XPATH = "//button[./span/p[text()='Add position']]"
    IMPORT_BUTTON_XPATH = "//button/span/p[text()='Import']"
    EXPORT_TEMPLATE_BUTTON_XPATH = "//button/span/p[text()='Export template']"
    DELETE_BUTTON_XPATH = "//button/span/p[text()='Delete']"

    def is_shown(self):
        return (len(self.browser.find_by_xpath(self.TAB_BY_NAME.format(text="All positions"))) > 0
                and len(self.browser.find_by_xpath(self.TAB_BY_NAME.format(text="Completed positions"))) > 0)

    def click_on_add_position_button(self):
        self.browser.find_by_xpath(self.ADD_POSITION_BUTTON_XPATH).click()

    def add_position_button_is_shown(self):
        return len(self.browser.find_by_xpath(self.ADD_POSITION_BUTTON_XPATH)) > 0

    def import_button_is_shown(self):
        return len(self.browser.find_by_xpath(self.IMPORT_BUTTON_XPATH)) > 0

    def click_on_import_button(self):
        self.browser.find_by_xpath(self.IMPORT_BUTTON_XPATH).click()

    def click_on_delete_button(self):
        self.browser.find_by_xpath(self.DELETE_BUTTON_XPATH).click()

    def export_button_is_shown(self):
        return len(self.browser.find_by_xpath(self.EXPORT_TEMPLATE_BUTTON_XPATH)) > 0

    def click_on_export_template_button(self):
        self.browser.find_by_xpath(self.EXPORT_TEMPLATE_BUTTON_XPATH).click()

    def click_on_export_button(self):
        self.browser.find_by_xpath(self.EXPORT_BUTTON_XPATH).click()
