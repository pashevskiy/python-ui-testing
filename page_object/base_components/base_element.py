import re
import time
from abc import ABC, abstractmethod


class BaseElement(ABC):
    ROOT = "ABSTRACT_LOCATOR"
    HIDDEN_AREA_DIV = "//div/div[@aria-hidden='true']"
    LOADING_ANIMATION = "//div[@class='loader']"

    GET_TEXT_VIA_JS = "return arguments[0].innerText"
    CLICK_VIA_JS = "arguments[0].click()"

    def __init__(self, browser):
        self.browser = browser

    def _get_root(self):
        return self.browser.find_by_xpath(self.ROOT)

    @abstractmethod
    def is_shown(self):
        pass

    # Utility methods
    def wait_loading_is_done(self):
        self.browser.is_element_not_present_by_xpath(self.LOADING_ANIMATION, wait_time=10)

    def click_on_hidden_div(self):
        self.browser.find_by_xpath(self.HIDDEN_AREA_DIV).last.click()

    def get_text_via_js(self, elem):
        return self.browser.execute_script(self.GET_TEXT_VIA_JS, elem._element)

    def click_via_js(self, elem):
        self.browser.driver.execute_script(self.CLICK_VIA_JS, elem._element)

    def _wait_menu_animation(self, elem):
        regex = re.search(r"transform ([0-9]+)ms", elem["style"])
        time.sleep(int(regex.group(1)) * 0.001)
