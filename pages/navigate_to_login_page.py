# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class Handles, The Login Element in Home Page
class ClickLogin(BasePage):
    def __init__(self,driver):
      super().__init__(driver) # Initializes driver from BasePage
      self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Clicks the login button if it is visible and enabled, otherwise logs appropriate messages
    def click_login(self,login_locator):
        try:
            by,value=login_locator
            by=getattr(By,by.upper())
            login_button=self.wait.until(
                expected_conditions.visibility_of_element_located(
                    ((by,value)
                     )
                )
            )
            if login_button.is_displayed() and login_button.is_enabled():
               login_button.click()
               print("Login Button is Found and Clicked")
            else:
               print("Login Button Not Found")
               print("Navigated to Login Page")
        # Handled Exceptions
        except (NoSuchElementException,TimeoutException):
            print("No Such Element or Time Out")




