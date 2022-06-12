from InstagramUserBot import InstagramUserBot
from EmailUserBot import EmailUserBot


class emailBot(InstagramUserBot, EmailUserBot):
    def __init__(self):
        self.signUpEmail()
        # self.signUpInstagram()


def main():
    # TODO create a Class for creating the usernames for email and instagram
    # TODO Might be better to have EmailUserBot and InstagramUserBot to be subclasses of this main class
    email_bot = EmailUserBot("Nathan", "Smith", "ilikedtogotothe2468724345425", "greniogn4389673468306!!!!")
    # instagram_bot = InstagramUserBot("testuser@gmail.com", "Test User1", "TestUser", "password1")

main()