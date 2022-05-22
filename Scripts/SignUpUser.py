import selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class NewUserBot():
    def __init__(self):
        self.signUp('nithin@gmail.com','Test User1','TestUser1','password1')

    def signUp(self, email, full_name, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(2)

        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')
        email_input.send_keys(email)

        full_name_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
        full_name_input.send_keys(full_name)

        username_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')
        password_input.send_keys(password)




def main():
    my_bot = NewUserBot()

if __name__ == '__main__':
    main()