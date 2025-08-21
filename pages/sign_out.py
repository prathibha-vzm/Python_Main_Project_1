# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class handled the Logout Functionality
class SignOut(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # Initializes driver from BasePage
        self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Clicks the dropdown arrow if visible and clickable, else logs relevant error messages
    def click_on_down_arrow(self,read_drop_down):
        try:
            by,value=read_drop_down
            by=getattr(By,by.upper())
            arrow=self.wait.until(expected_conditions.element_to_be_clickable(
                (by,value)
            )
            )
            if arrow.is_displayed():
                print("Arrow is Present")
                arrow.click()
            else:
                print("Arrow Not Present")

        except NoSuchElementException:
            print("Arrow Element Not Found")
        except TimeoutException:
            print("Arrow Time Out")

    # Clicks the SignOut if visible and clickable, else logs relevant error messages
    def click_on_sign_out(self,read_sign_out):
        try:
            by,value=read_sign_out
            by=getattr(By,by.upper())
            sign_out=self.wait.until(expected_conditions.element_to_be_clickable(
                (by,value)
            )
            )
            if sign_out.is_displayed():
                sign_out.click()
                print("Clicked on SignOut")
            else:
                print("SignOut Not Found")

        except NoSuchElementException:
            print("SignOut Element Not Found")
        except TimeoutException:
            print("SignOut Time Out")



