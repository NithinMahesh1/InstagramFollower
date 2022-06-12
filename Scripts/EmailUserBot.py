import random
from selenium import webdriver
from time import sleep
from sys import platform


class EmailUserBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.signUpEmail(self.username, self.password)

    def signUpEmail(self, username, password):
        # rand = random(1, 100000)

        print("Operating System is: ")
        if platform == "linux" or platform == "linux2":
            print("Linux")

        if platform == "darwin":
            print("OSX")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)

            # TODO change this to generic path for any user
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path='D:/MyGit/InstagramFollower/Scripts/chromedriver')
            self.driver.get("https://mail.tutanota.com/login?noAutoLogin=true")
            sleep(3)

            # Clicks the Signup option
            self.driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[3]/div/button/small').click()

            # Clicks the free user option: note that user accounts are deleted after not being used for a month (aka login)
            self.driver.find_element_by_xpath(
                '//*[@id="login-view"]/div[2]/div/div[4]/div/div/div/button[1]/div/div').click()

            # Adding this because of hang (might be because of the plane wifi)
            # Clicks on the dialog signup button to open dialog box with options for free account
            sleep(3)
            try:
                self.driver.find_element_by_xpath(
                    '//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()
            except:
                sleep(33)
                self.driver.find_element_by_xpath(
                    '//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()

            # Clicks the check box for "I do not own any other free account"
            try:
                self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()
            except:
                sleep(7)
                self.driver.find_element_by_xpath(
                    '//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div/div').click()
                self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()

            # Clicks the check box for "I will not use this account for business"
            self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[2]/div/input').click()

            # Clicks on the OK button
            self.driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[3]/button[2]/div').click()


        elif platform == "win32":
            print("Windows")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)

            # TODO change this to generic path for any user
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.get("https://mail.tutanota.com/login?noAutoLogin=true")
            sleep(3)

            # Clicks the More Option
            self.driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[3]/div/button/small').click()

            # Clicks the SignUpButton to open dialog
            sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="login-view"]/div[2]/div/div[4]/div/div/div/button[1]/div').click()

            # Clicks the free account button in dialog
            sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[5]/button/div').click()

            # Clicks the "I do not own any other Free Account" checkbox
            self.driver.find_element_by_xpath(
                '//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()

            # Clicks the "I will not use this account for business" checkbox
            self.driver.find_element_by_xpath(
                '//*[@id="modal"]/div[2]/div/div/div/div[2]/div[2]/div/input').click()

            # Clicks the ok button to submit form
            self.driver.find_element_by_xpath(
                '//*[@id="modal"]/div[2]/div/div/div/div[3]/button[2]/div').click()

            # TODO create a random int that is passed to the username
            sleep(5)
            username_input = self.driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[1]/div/div/div/div[1]/input')
            username_input.send_keys(self.username)

            password_input = self.driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[2]/div[1]/div/div/div/div[1]/input[4]')
            password_input.send_keys(self.password)

            # Inputs repeat password field
            repeat_password = self.driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[2]/div[3]/div/div/div/div/input')
            repeat_password.send_keys(self.password)

            # Clicks terms and conditions checkbox
            self.driver.find_element_by_xpath(
                '//*[@id="signup-account-dialog"]/div/div[3]/div/input').click()

            # Clicks "I am at least 16 years old" checkbox
            self.driver.find_element_by_xpath(
                '//*[@id="signup-account-dialog"]/div/div[4]/div/input').click()

            # Clicks the next button on form after filling out user information
            sleep(10)
            self.driver.find_element_by_xpath(
                '//*[@id="signup-account-dialog"]/div/div[5]/button/div').click()

            # Clicks on the ok button after user is created
            sleep(50)
            # self.driver.find_element_by_xpath(
            #     '//*[@id="wizardDialogContent"]/div[4]/div/button').click()

            # Enters password after creating new user to test it logs in fine
            self.driver.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[1]/form/div[2]/div/label').send_keys(self.password)
