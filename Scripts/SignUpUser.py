import selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class NewUserBot():
    def __init__(self, email, full_name, username, password):
        self.email = email
        self.full_name = full_name
        self.username = username
        self.password = password
        self.signUp(self.email, self.full_name, self.username, self.password)

    def signUp(self, email, full_name, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options=options)
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


class emailBot(NewUserBot):
    def __init__(self):
        self.signUp()

    # def signUp(Super.email, Super.full_name, Super.username, Super.password):
    #     print()



def main():
    my_bot = NewUserBot("testuser@gmail.com", "Test User1", "TestUser", "password1")

main()