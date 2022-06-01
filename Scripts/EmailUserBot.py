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

    def signUpEmail(self, email, first_name, last_name, password):
        rand = random(1, 100000)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S134305914%3A1653956329880032&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
        sleep(3)

        first_name_input = self.driver.find_element_by_xpath('//*[@id="firstName"]')
        first_name_input.send_keys(self.first_name)

        last_name_input = self.driver.find_element_by_xpath('//*[@id="lastName"]')
        last_name_input.send_keys(self.last_name)

        username_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        username_input.send_keys(self.username + str(rand))

        password_input = self.driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
        password_input.send_keys(self.password + str(rand))

        confirmPswrd_input = self.driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
        confirmPswrd_input.send_keys(self.password + str(rand))

        # Form submit button
        self.driver.find_element_by_class_name('VfPpkd-vQzf8d').click()