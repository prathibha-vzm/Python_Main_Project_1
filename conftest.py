# Importing Packages
import json
import os.path
from sys import exception
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Add a command-line option "--browser" to pytest so we can choose the browser when running tests
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

# Fixture to initialize and quit browser
@pytest.fixture
def driver(request):
    # Get the browser name from command-line option
    browser = request.config.getoption("--browser")
    # This is to choose cross-browser
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        print(f"Please pass the correct browser name: {browser}")
        raise exception("Driver Not Found")
    driver.maximize_window()
    yield driver
    driver.quit()

# Reads and returns test data from test_data.json
def read_test_data():
    test_data_path=os.path.join(os.path.dirname(__file__),"data\\test_data.json")
    with open(test_data_path,'r', encoding="utf-8") as file_path:
       datas=json.load(file_path)
       return datas

# This method is read the Web Application URL
@pytest.fixture(scope="session")
def read_url():
    return read_test_data()["Url"]["base_url"]

# This method is read the Login button in home page
@pytest.fixture(scope="session")
def read_login_locator():
    return read_test_data()["Login_Button"]["login"]

# This method is read the SignUp link Locator
@pytest.fixture(scope="session")
def read_signup_locator():
    return read_test_data()["SignUp"]["signup"]

# This method is read the Signup page URL for assertion
@pytest.fixture(scope="session")
def expected_url():
    return read_test_data()["Signup_Url"]["url"]

# This method is read the SignUp Element in the SignUp page (To Load the Full Page)
@pytest.fixture(scope="session")
def read_signup_element():
    return read_test_data()["Signup_Element"]["signup_element"]

# This method is read the Login link Locator in SignUp Page
@pytest.fixture(scope="session")
def read_login_link():
    return read_test_data()["Login_Link"]["login"]

# This method is read the Username/Email Locator in Login page
@pytest.fixture(scope="session")
def read_username_field():
    return read_test_data()["Email_Field"]["email"]

# This method is read the Password Locator in Login page
@pytest.fixture(scope="session")
def read_password_field():
    return read_test_data()["Password_Field"]["password"]

# This method is read the Checkbox Locator in Login page
@pytest.fixture(scope="session")
def read_checkbox():
    return read_test_data()["Check_Box"]["logged_in"]

# This method is read the Login Button Locator in Login page
@pytest.fixture(scope="session")
def read_login():
    return read_test_data()["Login_Element"]["login_element"]

# This method is read the Dashboard Element (To Load the Full Page)
@pytest.fixture(scope="session")
def read_dashboard_element():
    return read_test_data()["Dashboard_Element"]["my_course"]

# This method is read the Error_message in Login page
@pytest.fixture(scope="session")
def read_error_message():
    return read_test_data()["Error_Message"]["error_text"]

# This method is read the Menu Item "Course" Locator in Home page
@pytest.fixture(scope="session")
def read_menu_course():
    return read_test_data()["Menu_Course"]["courses"]

# This method is read the Menu Item "Live-Class" Locator in Home page
@pytest.fixture(scope="session")
def read_menu_live_class():
    return read_test_data()["Menu_Live_Class"]["live_class"]

# This method is read the Menu Item "Practice" Locator in Home page
@pytest.fixture(scope="session")
def read_menu_practice():
    return read_test_data()["Menu_Practice"]["practice"]

# This method is read the Dobby Assistant Locator in Dashboard page
@pytest.fixture(scope="session")
def read_dobby_element():
    return read_test_data()["Dobby"]["dobby_chatbot"]

# This method is read the Down_Arrow Locator in Dashboard page (To SignOut)
@pytest.fixture(scope="session")
def read_drop_down():
    return read_test_data()["Drop_Down"]["drop_down"]

# This method is read the SignOut Locator in Dashboard page (To SignOut)
@pytest.fixture(scope="session")
def read_sign_out():
    return read_test_data()["Sign_Out"]["sign_out"]
