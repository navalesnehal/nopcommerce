import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginClass
from Utilities.readconfigfile import Readconfig
from Utilities.Logger import LoggenClass


class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    @pytest.mark.sanity
    def test_verify_url_001(self, setup):
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.log.info("Page Title is --> " + self.driver.title)
        # print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test_Case test_verify_url_001 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\SHREE\\PycharmProjects\\Nopcom_python\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.log.info("Test_Case test_verify_url_001 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\SHREE\\PycharmProjects\\Nopcom_python\\Screenshots\\test_verify_url_001_fail.png")
            assert False
        self.log.info("Test_case test_verify_url_001 is Completed")

    @pytest.mark.sanity
    def test_user_login_002(self, setup):
        self.log.info("Test_case test_user_login_002 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Password - " + self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.click_Login_Button()
        if self.lp.Verify_Login_Status() == "Login Pass":
            self.log.info("Test_case test_user_login_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.log.info("Click on Logout button")
            self.lp.click_LogOutButton()
            assert True
        else:
            self.log.info("Test_case test_user_login_002 is Failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False
        self.log.info("Test_case test_user_login_002 is Completed")

# pytest -v -n=2 --html=HtmlReports/myreport.html\

# test_emp_add
# test_emp_edit
# test_emp_search
#
# -k test_emp
