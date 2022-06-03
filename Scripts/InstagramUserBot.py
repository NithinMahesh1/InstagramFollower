import selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from EmailUserBot import EmailUserBot


class InstagramUserBot(EmailUserBot):
    def __init__(self, email, full_name, username, password):
        self.email = email
        self.full_name = full_name
        self.username = username
        self.password = password
        self.signUpInstagram(self.email, self.full_name, self.username, self.password)

    def signUpInstagram(self, email, full_name, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/Users/nithinmahesh/Documents/MyGit/InstagramFollower/Scripts/chromedriver')
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(3)

        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')
        email_input.send_keys(self.email)

        full_name_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
        full_name_input.send_keys(self.full_name)

        username_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')
        username_input.send_keys(self.username)

        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')
        password_input.send_keys(self.password)
