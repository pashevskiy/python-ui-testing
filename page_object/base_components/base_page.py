from splinter import Browser
from page_object.base_components.base_element import BaseElement
from abc import abstractmethod


class BasePage(BaseElement):
    ALERT_MESSAGE_XPATH = "//div[contains(@class,'rrt-error')]//div[@role='alertdialog']/div"
    NOTIFICATION_MESSAGE = "//div[@role='alertdialog']"
    TAB_BY_NAME = "//div[@aria-label='view-tabs']/button[./span[text()='{text}']]"

    def __init__(self, browser: Browser):
        super().__init__(browser)

    # It should be implemented in real pages
    @abstractmethod
    def is_shown(self):
        return None

    def get_alert_messages(self):
        return list(map(lambda x: x.text,
                        self.browser.find_by_xpath(self.ALERT_MESSAGE_XPATH)))

    def click_on_tab(self, name):
        self.click_via_js(self.browser.find_by_xpath(self.TAB_BY_NAME.format(text=name)))

    def wait_notifications_are_disappeared(self):
        self.browser.is_element_not_present_by_xpath(self.NOTIFICATION_MESSAGE, 20)
