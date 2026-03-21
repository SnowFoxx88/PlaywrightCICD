from .login_page import LoginPage
from .tasksmash_page import TaskSmashPage
from playwright.sync_api import Page


class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.tasksmash_page = TaskSmashPage(page)
