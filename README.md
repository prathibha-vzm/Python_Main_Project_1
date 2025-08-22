# Title: Automated Testing of the Web Application https://www.guvi.in
# Project Architecture
<pre>
guvi_project/
│── data/                       # Test data
│   ├── test_data.json          # UI element locators (XPATH, URL)
|
│── pages/                     # Page Object classes
│   ├── base_page.py           # WebApplication URL
|   ├── dobby_chatbot.py       # Dobby Assistant in Dashboard
|   ├── login_link.py          # Login Element in Home Page
│   ├── login_page.py          # Login Page actions
|   ├── menu_bar.py            # Menu items in Home Page
|   ├── navigate_to_login_page.py # Login Element in SignUp Page
|   ├── sign_out.py            # Logout Functionality
│   ├── signup_page.py         # Signup Page actions
│
|── screenshots               # Contains Screenshots taken during test run
|
├──tests/
├── features/                # Feature files written in Gherkin
│   ├── test_guvi.feature    # Covers the Test Verifies Page URl, Title and Navigate to Login Page and SignUp Page (Test cases 1-5)
│   ├── test_login.feature   # Covers login scenarios for valid and Invalid credentials(Error message) (Test Cases - 6 & 7)
│   └── test_menu_chatbot_logout.feature  # Covers menu, chatbot & logout scenarios (Test Cases 8- 10)
│
├── step_def/                # Step definition files in Python
│   ├── __init__.py
│   ├── test_guvi_home.py    # Step definitions for Guvi home page
│   ├── test_guvi_login.py   # Step definitions for login page
│   └── test_menu_chatbot.py # Step definitions for menu/chatbot/logout
│
|── conftest.py              # contains pytest fixtures for driver, cross browser selection, to read json data
|── pytest.ini               # conatins marker and path for feature
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation
</pre>

# Features
. BDD style testing with Behave

. POM, Data Driven Testing

. Perform Cross-Browser Validation

. Covers Home Page, Login, Menu, Chatbot, Logout scenarios

. Handles timeouts, exceptions gracefully

. Uses explicit waits for stable execution

. Console logs for better debugging

# Usage
## To Run the Test in Cross Browser
<pre><code>pytest tests/step_def/test_guvi_home.py -m smoke_test --browser=chrome</code></pre>
<pre><code>pytest tests/step_def/test_guvi_home.py -m smoke_test --browser=edge</code></pre>
## To Run the Tests and Generate allure report
<pre><code>pytest tests/ --alluredir=allure-results -m smoke_test </code>
<code>allure generate allure-results -o allure-report --clean</code>
<code>allure open allure-report</code></pre>

