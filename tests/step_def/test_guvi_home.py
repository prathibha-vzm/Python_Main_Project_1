import time
from pytest_bdd import scenarios, given, when, then
from guvi_project.pages.base_page import BasePage
from guvi_project.pages.login_link import LoginLink
from guvi_project.pages.navigate_to_login_page import ClickLogin
from guvi_project.pages.sign_up_page import SignUp

# Feature Files Path is given
scenarios("test_guvi.feature")

# This Method, Launch the Application URL and Verify the Home Page Title with Screenshot
@given('User Navigates to the URL and Validates the Page Title')
def launch_application(driver,read_url):
    print("____Test Case - 1____")
    base_object=BasePage(driver)
    base_object.navigate_to_url(read_url)
    print("____Test Case - 2____")
    title = driver.title
    print(f"Title: {title}")
    assert title == "GUVI | Learn to code in your native language"

#This Method is to Click on the Login Link in Home Page
@when('User Click on Login Button')
def click_login_button(driver,read_login_locator):
    print("____Test Case - 3____")
    login_link_object=ClickLogin(driver)
    login_link_object.click_login(read_login_locator)
    time.sleep(2)

# This Method, Verifies the User landed on Login Page by Asserting the Title of the Page
@when('User should Land on Login page')
def verify_landed_page(driver):
    title = driver.title
    print(f"Title:{title}")
    time.sleep(2)
    assert title == "GUVI | Login"

# This Method, Verifies the User can Click on SignUp link in Login Page
@then('User Clicks on Signup Link')
def verify_sign_up_link(driver,read_signup_locator):
    signup_object=SignUp(driver)
    signup_object.click_sign_up_link(read_signup_locator)

# This Method, Verifies navigation to SignUp page by asserting the landed URL
@then('Navigate to Signup Page')
def verify_sign_up_navigation(driver,read_signup_element,expected_url):
    signup_object=SignUp(driver)
    signup_object.signup_page_navigation(read_signup_element)
    actual_url=driver.current_url
    print(f"SignUp Page URL: {actual_url}")
    assert actual_url==expected_url

# This Method, Verifies Navigation back to Login Page by Clicking on Login link in SignUp Page
@then('User Click on Login to Navigate to Login Page')
def navigate_to_login(driver,read_login_link):
    login_object=LoginLink(driver)
    login_object.navigate_to_login_page(read_login_link)


