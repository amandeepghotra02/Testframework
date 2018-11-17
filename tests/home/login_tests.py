from email.mime import audio

import selenium
from selenium import webdriver
import os
from pages.home.login_page import LoginPage
import unittest
from selenium.webdriver import ChromeOptions, Chrome
import pytest
from utilities.Teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp" , "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("admin", "admin")
        result1 = self.lp.verifyLoginTitle()
       #  assert result1 == True
        self.ts.mark(result1, "Title verified ")
        result2 = self.lp.verifyLoginSuccessful()
        # assert result2 == True
        self.ts.markFinal("test_validlogin", result2, "Login was successful")

    @pytest.mark.parametrize("username, password", [("correct_username", "false_password"),
                                                    ("false_username", "correct_password"),
                                                    ("false_username", "false_password"),
                                                    ("admin", "admin")])
    @pytest.mark.run(order=1)
    def test_invalidLogin(self, username, password):
        self.lp.login()
        result = self.lp.verifyLoginFailed()
        assert result == True



# lg = LoginTests()
# lg.test_validLogin()





