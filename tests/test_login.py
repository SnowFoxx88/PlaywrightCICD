from playwright.sync_api import expect
from pages.page_manager import PageManager
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")


def test_login(pm: PageManager):
    pm.login_page.open_url(url)
