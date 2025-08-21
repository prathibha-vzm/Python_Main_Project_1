# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class handles Login Link in Home page and Navigate to Login Page
class LoginLink(BasePage):
    def __init__(self,driver):
        super().__init__(driver)# Initializes driver from BasePage
        self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Locate and validate visibility of Login Link element and click on it to Navigate to Login page
    def navigate_to_login_page(self,login_locator):
        try:
            by,value=login_locator
            by=getattr(By,by.upper())
            login=self.wait.until(expected_conditions.element_to_be_clickable(
                 (by,value)
                )
            )
            if login.is_displayed() and login.is_enabled():
                login.click()
                print("Landed On Login Page")
            else:
                print("Login Link Not Found")
        # Handled Exception
        except TimeoutException:
            print("Login Link Time Out Exception")
