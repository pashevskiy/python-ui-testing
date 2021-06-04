from page_object.base_components.base_element import BaseElement


class BaseTableElement(BaseElement):
    # HEADERS
    ROOT = ".//table[@aria-label='enhanced table']"
    TABLE_COLUMN_HEADERS_XPATH = ".//thead/tr/th[not(.//input) and not(.//button)]/span"
    TABLE_COLUMN_HEADERS_BY_NAME_XPATH = (".//thead/tr/th[not(.//input)"
                                          + " and not(.//button) and ./span[text() = '{text}']]")

    # DATA
    TABLE_LINE_XPATH = ".//tbody/tr"
    TABLE_LINE_SELECT_XPATH = "./td//input"
    TABLE_CELL_XPATH = "./td/div/span"

    def __init__(self, browser, context=None):
        self.context = context
        super().__init__(browser)

    def _get_root(self):
        if self.context:
            return self.context.find_by_xpath(self.ROOT)
        return super()._get_root()

    def is_shown(self):
        return len(self._get_root()) > 0

    def set_context(self, context):
        self.context = context

    def get_headers(self):
        table = self._get_root()
        # table = self.browser.driver.find_elements_by_xpath(self.TABLE_XPATH)[0]
        headers = table.find_by_xpath(self.TABLE_COLUMN_HEADERS_XPATH)
        texts = []
        for header in headers:
            texts.append(self.get_text_via_js(header))

        return texts

    def get_data(self):
        result_data = []

        headers = self.get_headers()
        table = self._get_root()
        lines = table.find_by_xpath(self.TABLE_LINE_XPATH)

        for line in lines:
            result_line = {}
            cells = line.find_by_xpath(self.TABLE_CELL_XPATH)

            for index, cell in enumerate(cells):
                result_line[headers[index]] = self.get_text_via_js(cell)

            result_data.append(result_line)
        return result_data

    def click_on_the_cell(self, column, line_number):
        headers = self.get_headers()
        table = self._get_root()
        line = table.find_by_xpath(self.TABLE_LINE_XPATH)[line_number - 1]
        line.find_by_xpath(self.TABLE_CELL_XPATH)[headers.index(column)].click()


class SelectableTableElement(BaseTableElement):
    TABLE_SELECT_ALL_XPATH = ".//thead/tr/th//input"

    def select_all(self):
        self._get_root().find_by_xpath(self.TABLE_SELECT_ALL_XPATH).click()

    def select_item(self, line):
        table = self._get_root()
        line = table.find_by_xpath(self.TABLE_LINE_XPATH)[line - 1]
        line.find_by_xpath(self.TABLE_LINE_SELECT_XPATH).click()
