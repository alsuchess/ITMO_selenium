from pages.base_page import BasePage
from components.components import WebElement
class AutomationPracticeForm(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')

        self.submit_btn = WebElement(driver, '#submit')

        self.form = WebElement(driver,' #userForm')
