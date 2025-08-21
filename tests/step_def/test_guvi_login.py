# Imported bdd step decorators and classes
from pytest_bdd import scenarios, given, when, parsers, then
from guvi_project.pages.base_page import BasePage
from guvi_project.pages.login_page import LoginPage
from guvi_project.pages.navigate_to_login_page import ClickLogin

# Feature Files Path is given
scenarios("test_login.feature")

# This Method, Launch the Application URL and Verify the Home Page Title with Screenshot
@given('User Navigates to the URL')
def launch_application(driver,read_url):
    print("____Test Case - 1____")
    base_object=BasePage(driver)
    base_object.navigate_to_url(read_url)
    print("____Test Case - 2____")
    title = driver.title
    driver.save_screenshot(f"screenshots/Home_Page.png")
    print(f"Title: {title}")
    assert title == "GUVI | Learn to code in your native language"

#This Method is to Click on the Login Link in Home Page
@when('User Clicks on Login Link')
def click_on_login_link(driver,read_login_locator):
    login_link_object = ClickLogin(driver)
    login_link_object.click_login(read_login_locator)

# This Method is to Enter Username and Password given in Examples
@when(parsers.cfparse('User Enters Credentials {username} and {password} to Login'))
def valid_user_login(driver,username,password,read_username_field,read_password_field,read_checkbox,read_login):
    print("____Test Case - 6____")
    login_object=LoginPage(driver)
    login_object.enter_username(username,read_username_field)
    login_object.enter_password(password,read_password_field)
    login_object.click_checkbox(read_checkbox)
    login_object.click_on_login_button(read_login)

# This Method, Verifies the Successful Login and Navigate to Dashboard page, Assert the Page Title and Take screenshots
@then(parsers.cfparse("The Valid User Should gets {expected_result} land on Dashboard"))
def valid_user_dashboard(driver,expected_result,read_dashboard_element):
    if expected_result=="Login Successful":
       driver.save_screenshot(f"screenshots/Valid_Login_Page.png")
       login_object = LoginPage(driver)
       login_object.dashboard_element_validation(read_dashboard_element)
       actual_title=driver.title
       print(f"Page Title: {actual_title}")
       driver.save_screenshot(f"screenshots/Dashboard_Page.png")
       assert actual_title=='GUVI | courses'
    else:
        print("Invalid Credentials")

# This Method, Verifies the Error Message occurs When Invalid credentials are entered and Take Screenshots
@then(parsers.cfparse("The Invalid User Should gets {expected_result}"))
def invalid_user_error_message(driver,expected_result,read_error_message):
    if expected_result=="Incorrect Email or Password":
        login_object = LoginPage(driver)
        print("____Test Case - 7____")
        login_object.check_error_message(read_error_message)
        driver.save_screenshot(f"screenshots/Invalid_Login.png")
    else:
        print("Valid Credentials")




