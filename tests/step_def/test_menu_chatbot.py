from pytest_bdd import scenarios, given, when, then, parsers
from guvi_project.pages.base_page import BasePage
from guvi_project.pages.dobby_chatbot import Dobby
from guvi_project.pages.login_page import LoginPage
from guvi_project.pages.menu_bar import Menu
from guvi_project.pages.navigate_to_login_page import ClickLogin
from guvi_project.pages.sign_out import SignOut

# Feature Files Path is given
scenarios("test_menu_chatbot_logout.feature")

# This Method, Launch the Application URL and Verify the Home Page Title with Screenshot
@given('User Enters Guvi page')
def launch_application(driver,read_url):
    print("____Test Case - 1____")
    base_object=BasePage(driver)
    base_object.navigate_to_url(read_url)
    print("____Test Case - 2____")
    title = driver.title
    print(f"Title: {title}")
    assert title == "GUVI | Learn to code in your native language"

# This Method, Verifies the Menu Items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
@when('User Verifies Navigation Bar')
def verify_navigation_bar(driver,read_menu_course,read_menu_live_class,read_menu_practice):
    print("____Test Case - 8____")
    menu_object=Menu(driver)
    menu_object.find_menu_course(read_menu_course)
    menu_object.find_menu_live_classes(read_menu_live_class)
    menu_object.find_menu_practice(read_menu_practice)
    driver.save_screenshot(f"screenshots/Menu_Bar.png")

# This Method, Is to Click on Login link in Home Page
@when('Click on Login Link')
def click_on_login_link(driver,read_login_locator):
    login_link_object=ClickLogin(driver)
    login_link_object.click_login(read_login_locator)

# This Method, Is to Enter Valid Credentials and Login Successfully
@then(parsers.cfparse('User Enters Valid Credentials {username} and {password} to Login'))
def login_with_valid_credentials(driver, username, password, read_username_field, read_password_field, read_checkbox,
                         read_login):
    login_object = LoginPage(driver)
    login_object.enter_username(username, read_username_field)
    login_object.enter_password(password, read_password_field)
    login_object.click_checkbox(read_checkbox)
    login_object.click_on_login_button(read_login)

# This Method, Verifies the Presence of Dobby Assistant with Screenshot.
@then('User Checks for Dobby Chatbot')
def dobby_verification(driver,read_dobby_element):
    print("____Test Case - 9____")
    dobby_object=Dobby(driver)
    dobby_object.locate_dobby(read_dobby_element)
    driver.save_screenshot(f"screenshots/Dobby.png")

# This Method, verifies the Logout Functionality, Assert the Landing page title and print the URL of the page after Logout.
@then('User Clicks SignOut and Land on Home Page')
def logout_functionality(driver, read_drop_down, read_sign_out,read_menu_course):
    print("____Test Case - 10____")
    sign_out_object=SignOut(driver)
    sign_out_object.click_on_down_arrow(read_drop_down)
    driver.save_screenshot(f"screenshots/Sign_Out.png")
    sign_out_object.click_on_sign_out(read_sign_out)
    menu_object = Menu(driver)
    menu_object.find_menu_course(read_menu_course)
    page_title=driver.title
    print(f"Title: {page_title}")
    driver.save_screenshot(f"screenshots/Assert_Login_Page.png")
    assert page_title=="GUVI | Learn to code in your native language"
    page_url=driver.current_url
    print(f"Url: {page_url}")