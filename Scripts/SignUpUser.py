from InstagramUserBot import InstagramUserBot
from EmailUserBot import EmailUserBot
from time import sleep


class emailBot(InstagramUserBot, EmailUserBot):
    def __init__(self):
        self.signUpEmail()
        self.signUpInstagram()


def main():
    # TODO create a Class for creating the usernames for email and instagram
    # TODO Might be better to have EmailUserBot and InstagramUserBot to be subclasses of this main class
    username = "ilikedtogotothe2468724345425"
    password = "greniogn4389673468306!!!!"
    emailUsername = username + "@tutanota.com"
    full_name = "Test User12345"

    email_bot = EmailUserBot(username, password)
    sleep(10)
    instagram_bot = InstagramUserBot(emailUsername, full_name, username, password)

main()