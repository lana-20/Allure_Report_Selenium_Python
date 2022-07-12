from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.serv_obj = Service()  # configure service object
        self.driver = webdriver.Chrome(service=self.serv_obj)  # launch the browser
        self.driver.get("https://opensource-demo.orangehrmlive.com/")  # open the application url
        self.driver.maximize_window()  # maximize the window
        status = self.driver.find_element(By.XPATH, "//*[@id='divLogo']/img").is_displayed()
        if status:  # verify the presence of the Logo via Python Assertions
            assert True     # Pass
        else:
            assert False    # Fail
        self.driver.close()     # close the browser window currently in focus

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping test - TBA")  # skip intentionally to exhibit PyTest skip() method

    @allure.severity(allure.severity_level.BLOCKER)
    def test_Login(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()
        act_title = self.driver.title
        if act_title == "OrangeHRM123":  # fail intentionally to generate a screenshot
            self.driver.close()
            assert True     # Pass
        else:
            allure.attach(      # use Allure package, .attach() method, pass 3 params
                self.driver.get_screenshot_as_png(),    # param1
                name="testLoginScreen",                 # param2
                attachment_type=AttachmentType.PNG)     # param3
            self.driver.close()
            assert False    # Fail
