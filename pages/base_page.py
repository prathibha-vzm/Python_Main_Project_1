from selenium.common.exceptions import WebDriverException

# This class is to handle URl and Title for the Web Application
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    # This method will navigate to the appropriate web application and read the title of the page.
    # Handled the Exception, that might occur when landed on wrong page
    def navigate_to_url(self,url):
        try:
           self.driver.get(url)
           print("Landed On Guvi Page")
        except WebDriverException:
            print("Landed On Wrong Page")


