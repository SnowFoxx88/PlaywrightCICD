from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_textbox = page.locator("#input_username")
        self.password_textbox = page.get_by_role("textbox", name="password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_message = page.get_by_text("You have been logged out.")

    def open_url(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        self.username_textbox.fill(username)

    def enter_password(self, password):
        self.password_textbox.fill(password)

    def click_login(self):
        self.login_button.click()
