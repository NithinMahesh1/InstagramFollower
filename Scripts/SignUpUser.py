from InstagramUserBot import InstagramUserBot
from EmailUserBot import EmailUserBot


class emailBot(InstagramUserBot, EmailUserBot):
    def __init__(self):
        self.signUpEmail()
        # self.signUpInstagram()


def main():
    # email_bot = EmailUserBot("Nathan", "Smith", "nithin", "password1")
    instagram_bot = InstagramUserBot("testuser@gmail.com", "Test User1", "TestUser", "password1")

main()