# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.conftest import driver
from guvi_project.pages.base_page import BasePage

# This Class Handles the Verification SignUp link in Login Page and Navigates to SignUp page
class SignUp(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    # Clicks on the Sign-Up link if it is visible and enabled, else logs appropriate error messages
    def click_sign_up_link(self,read_signup_locator):
        try:
           by,value=read_signup_locator
           by=getattr(By,by.upper())
           sign_up=self.wait.until(
               expected_conditions.element_to_be_clickable(
                  (by,value)
               )
           )
           print("____Test Case - 4____")
           if sign_up.is_displayed() and sign_up.is_enabled():
               print("Sign_Up Element Found")
               sign_up.click()
               print("Sign_Up Element Clicked")
           else:
               print("Signup Button is not enabled")
        # Handled Exceptions
        except NoSuchElementException:
            print("Signup Link Element Not Found")
        except TimeoutException:
            print("Signup Time Out")

    # Verifies navigation to the Sign-Up page by printing signup page element.
    def signup_page_navigation(self,read_signup_element):
           print("____Test Case - 5____")
           print("Sign_Up Page Loaded")
           try:
                by_sign,value_sign=read_signup_element
                by_sign=getattr(By,by_sign.upper())
                element_sign_up=self.wait.until(
                    expected_conditions.visibility_of_element_located(
                        (by_sign,value_sign)
                    )
                )
                print(f"Page Name: {element_sign_up.text}")
           # Handled Exceptions
           except NoSuchElementException:
                print("Sign_Up Page Element Not Found ")









