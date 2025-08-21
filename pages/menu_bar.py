# Imported Exception, WebDriver By, Wait, expected_conditions and Class base page
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from guvi_project.pages.base_page import BasePage

# This Class handles the Menu Items Presence
class Menu(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # Initializes driver from BasePage
        self.wait=WebDriverWait(driver,10) # Explicit wait with 10s timeout

    # Verifies if the course menu element is visible and accessible
    def find_menu_course(self, read_menu_course):
        try:
            by,value=read_menu_course
            by=getattr(By,by.upper())
            course=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if course.is_displayed() and course.is_enabled():
                print(f" {course.text} is Present in Menu")
            else:
                print("Course is Not Present in Menu")

        # Handled Exceptions
        except NoSuchElementException:
            print("No Course Element")
        except TimeoutException:
            print("Course Time Out")

    # Verifies if the live_class menu element is visible and accessible
    def find_menu_live_classes(self, read_menu_live_class):
        try:
            by,value=read_menu_live_class
            by=getattr(By,by.upper())
            live_class=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if live_class.is_displayed() and live_class.is_enabled():
                print(f" {live_class.text} is Present in Menu")
            else:
                print("Live Class is Not Present in Menu")
        # Handled Exceptions
        except NoSuchElementException:
            print("No Live Class Element")
        except TimeoutException:
            print("Live Class Time Out")

    # Verifies if the practice menu element is visible and accessible
    def find_menu_practice(self, read_menu_practice):
        try:
            by,value=read_menu_practice
            by=getattr(By,by.upper())
            practice=self.wait.until(expected_conditions.visibility_of_element_located(
                (by,value)
            )
            )
            if practice.is_displayed() and practice.is_enabled():
                print(f" {practice.text} is Present in Menu")
            else:
                print("Practice is Not Present in Menu")
        # Handled Exceptions
        except NoSuchElementException:
            print("No Practice Element")
        except TimeoutException:
            print("Practice Time Out")
