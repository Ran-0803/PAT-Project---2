class WebLocator:

    def __init__(self):
        self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.fypLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
        self.UserNameLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input'
        self.resetPasswordLocator = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
        # This code is used to find the path for password
        self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        # This code is used to find the path for login-button
        self.loginLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        # This code is used to find the path for admin
        self.adminLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        # This code is used to find the header for TestCase-2
        self.optionsLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li'
        # This code is used to find the mainMenu for TestCase-3
        self.options1Locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li'

