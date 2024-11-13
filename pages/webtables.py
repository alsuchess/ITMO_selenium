from pages.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows_found = WebElement(driver, '#div.rt-noData')
        self.btn_delete_row = WebElement(driver, "//*[contains(@id, 'delete')]", 'xpath')
        self.btn_delete_row4 = WebElement(driver, "//*[contains(@id, 'delete-record-4')]", 'xpath')
        self.pencil = WebElement(driver, "//*[contains(@id, 'edit-record-4')]", 'xpath')
        self.no_data = WebElement(driver, "//*[contains(@class, 'noData')]", 'xpath')
        self.add = WebElement(driver, '#addNewRecordButton')
        self.submit = WebElement(driver, '#submit')
        self.form = WebElement(driver, '#userForm')
        self.table = WebElement(driver, "//*[contains(@class, 'table')]", 'xpath')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')


