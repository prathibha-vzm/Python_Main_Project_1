from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class Handles Dobby Assistant Element
class Dobby(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # Initializes driver from BasePage
        self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Locate and validate visibility of Dobby element on the page
    def locate_dobby(self,read_dobby_element):
        try:
            by,value=read_dobby_element
            by=getattr(By,by.upper())
            dobby=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if dobby.is_displayed():
                print(f"{dobby.text} is Present")
            else:
                print("Dobby Not Present")

        except NoSuchElementException:
            print("Dobby Element Not Found")
        except TimeoutException:
            print("Dobby Time Out")
