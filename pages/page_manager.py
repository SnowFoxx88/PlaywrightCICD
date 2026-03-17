from .login_page import LoginPage
from playwright.sync_api import Page


class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
