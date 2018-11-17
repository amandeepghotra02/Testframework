from selenium.webdriver.common.by import By
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    # call the custom logger method of utilities package and send him level of logging : debug, error, warning etc
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "username"
    _password_field = "password"
    _login_button = "#modalview-login-button"
    _pos_button ="app-ico-POS"

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="CSS" )

    def login(self, username="", password=""):
       self.enterUsername(username)
       self.enterPassword(password)
       self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("app-ico-POS")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Username is required')]",
                                       locatorType='xpath')
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Mi9 Mosaic Clienteling")

