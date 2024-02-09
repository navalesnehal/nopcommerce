from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:
    Text_Email_Xpath = "//input[@id='Email']"
    Text_Password_Xpath = "//input[@id='Password']"
    Click_LoginButton_Xpath = "//button[normalize-space()='Log in']"
    Click_LogOutButton_Xpath = " //a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.Click_LogoutButton_Xpath = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Email(self, Email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(Email)

    def Enter_Password(self, Password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(Password)

    def click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def click_LogOutButton(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_LogoutButton_Xpath)))
            self.driver.find_element(By.XPATH, self.Click_LogOutButton_Xpath).click()
        except:
            pass

    def Verify_Login_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Click_LogOutButton_Xpath)
            return "Login Pass"
        except:
            return "Login Fail"
