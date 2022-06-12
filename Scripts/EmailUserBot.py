import selenium
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class EmailUserBot():
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.signUpEmail(self.first_name, self.last_name, self.username, self.password)

    def signUpEmail(self, username, first_name, last_name, password):
        # rand = random(1, 100000)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/Users/nithinmahesh/Documents/MyGit/InstagramFollower/Scripts/chromedriver')
        self.driver.get("https://mail.tutanota.com/login?noAutoLogin=true")
        sleep(3)

        # Clicks the Signup option
        self.driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[3]/div/button/small').click()

        # Clicks the free user option: note that user accounts are deleted after not being used for a month (aka login)
        self.driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[4]/div/div/div/button[1]/div/div').click()

        # Adding this because of hang (might be because of the plane wifi)
        # Clicks on the dialog signup button to open dialog box with options for free account
        sleep(7)
        try:
            self.driver.find_element_by_xpath('//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()
        except:
            sleep(33)
            self.driver.find_element_by_xpath('//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()

        # Clicks the check box for "I do not own any other free account"
        try:
            self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()
        except:
            sleep(7)
            self.driver.find_element_by_xpath('//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()
            self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()

        # Clicks the check box for "I will not use this account for business"
        self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[2]/div/input').click()

        # Clicks on the OK button
        self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[3]/button[2]/div').click()

        # TODO create a random int that is passed to the username
        self.driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[1]/div/div').click()
        # email_input_keys = self.driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[1]/div/div')
        # email_input_keys.send_keys(self.username)