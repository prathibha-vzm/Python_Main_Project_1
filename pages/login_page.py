# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class handles Username, password, checkbox and Login button locators in Login page
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # Initializes driver from BasePage
        self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Enter the given username into the username input field after validating visibility
    def enter_username(self,username,read_username_field):
        try:
            by,value=read_username_field
            by=getattr(By,by.upper())
            username_locator=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if username_locator.is_displayed():
                username_locator.clear()
                username_locator.send_keys(username)
                print("Entered username")
            else:
                print("Username Field Not Displayed / is Filled")
        # Handled Exceptions
        except NoSuchElementException:
            print("Username not found")
        except TimeoutException:
            print("Username Element Time Out")

    # Enter the given password into the password input field after validating visibility
    def enter_password(self,password,read_password_field):
        try:
            by,value=read_password_field
            by=getattr(By,by.upper())
            password_locator=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if password_locator.is_displayed():
                password_locator.clear()
                password_locator.send_keys(password)
                print("Entered Password")
            else:
                print("Password Field Not Displayed / is Filled")
        # handled Exceptions
        except NoSuchElementException:
            print("Password not found")
        except TimeoutException:
            print("Password Element Time Out")

    # Selects the checkbox if not already selected, ensuring element is clickable
    def click_checkbox(self,read_checkbox):
        try:
            by,value=read_checkbox
            by=getattr(By,by.upper())
            checkbox=self.wait.until(expected_conditions.element_to_be_clickable(
                (by,value)
                                                                                 )
                                     )
            if not checkbox.is_selected():
                checkbox.click()
                print("Checkbox is Selected")
            else:
                print("Checkbox already Selected")
        # handled Exceptions
        except NoSuchElementException:
            print("Checkbox not found")
        except TimeoutException:
            print("Checkbox Element Time Out")

    # Clicks on the Login button if it is visible and enabled
    def click_on_login_button(self,read_login):
        try:
            by,value=read_login
            by=getattr(By,by.upper())
            login=self.wait.until(expected_conditions.element_to_be_clickable(
                (by,value)
            )
            )
            if login.is_displayed() and login.is_enabled():
                login.click()
                print("Login Button is clicked")
            else:
                print("Login Button Not Found")
        # handled Exceptions
        except NoSuchElementException:
            print("Login not found")
        except TimeoutException:
            print("Login Element Time Out")

    # Validates the presence of a dashboard element and prints its text if visible
    def dashboard_element_validation(self,read_dashboard_element):
        try:
            by,value=read_dashboard_element
            by=getattr(By,by.upper())
            my_course=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if my_course.is_displayed():
                print(f"Dashboard Element: {my_course.text}")
            else:
                print("Dashboard Element Not Found")
        # handled Exception
        except TimeoutException:
            print("Dashboard Element Not Found")

    # Validates and prints the error message if displayed
    def check_error_message(self,read_error_message):
        try:
            by,value=read_error_message
            by=getattr(By,by.upper())
            error_message=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if error_message.is_displayed():
                print(f"Error Message: {error_message.text}")
            else:
                print("No Error Message Appeared")
        except NoSuchElementException:
            print("No Error Message")
        except TimeoutException:
            print("Error Time Out")