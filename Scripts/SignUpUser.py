from InstagramUserBot import InstagramUserBot


class emailBot(InstagramUserBot):
    def __init__(self):
        self.signUp()

    # def signUp(Super.email, Super.full_name, Super.username, Super.password):
    #     print()



def main():
    my_bot = InstagramUserBot("testuser@gmail.com", "Test User1", "TestUser", "password1")

main()