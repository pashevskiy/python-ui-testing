from page_object.base_components.base_element import BaseElement


class Search(BaseElement):
    SEARCH_INPUT_ELEMENT_XPATH = "//input[@placeholder='Search...']"
    SEARCH_CLEAR_CROSS_CSS = "div.MuiAutocomplete-root>div:last-child>svg"
    AUTOCOMPLETE_BLOCK_CSS = "ul.MuiAutocomplete-listbox>li"
    AUTOCOMPLETE_ELEMENT_GROUP_CSS = "div.MuiAutocomplete-groupLabel"
    AUTOCOMPLETE_ELEMENT_VALUE_CSS = "li.MuiAutocomplete-option>p"
    AUTOCOMPLETE_ELEMENT_NOT_FOUND_CSS = "div.MuiAutocomplete-noOptions"

    def is_shown(self):
        search = self.browser.find_by_xpath(self.SEARCH_INPUT_ELEMENT_XPATH)
        return len(search) > 0

    def type_text(self, text):
        self.browser.find_by_xpath(self.SEARCH_INPUT_ELEMENT_XPATH).type(text)

    def clear_text(self):
        self.browser.find_by_css(self.SEARCH_CLEAR_CROSS_CSS).click()

    def is_not_found(self):
        not_found_elem = self.browser.find_by_css(self.AUTOCOMPLETE_ELEMENT_NOT_FOUND_CSS)
        return len(not_found_elem) > 0

    def get_autocomplete_blocks(self):
        result = {}
        blocks = self.browser.find_by_css(self.AUTOCOMPLETE_BLOCK_CSS, wait_time=5)

        for block in blocks:
            group = block.find_by_css(self.AUTOCOMPLETE_ELEMENT_GROUP_CSS).text
            values = block.find_by_css(self.AUTOCOMPLETE_ELEMENT_VALUE_CSS)
            values_texts = []
            for value in values:
                values_texts.append(value.text)
            result[group] = values_texts
        return result

    def click_on_autocomplete_block_by_text(self, text):
        blocks = self.browser.find_by_css(self.AUTOCOMPLETE_BLOCK_CSS)

        for block in blocks:
            value_elem = block.find_by_css(self.AUTOCOMPLETE_ELEMENT_VALUE_CSS)
            if value_elem.text == text:
                value_elem.click()
                return

    def click_on_autocomplete_block_by_id(self, index):
        self.browser.find_by_css(self.AUTOCOMPLETE_BLOCK_CSS)[index].click()
