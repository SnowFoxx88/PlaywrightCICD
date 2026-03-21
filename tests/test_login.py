from playwright.sync_api import expect
from pages.page_manager import PageManager
import os
import json
import pytest
from dotenv import load_dotenv
import time

load_dotenv()
url = os.getenv("URL")

with open("data/credentials.json") as f:
    test_data = json.load(f)
    credentials = test_data["credentials"]


@pytest.mark.parametrize("user_credentials", credentials)
def test_login(pm: PageManager, user_credentials):
    pm.login_page.open_url(url)
    pm.login_page.enter_username(user_credentials["username"])
    pm.login_page.enter_password(user_credentials["password"])
    pm.login_page.click_login()
    expect(pm.tasksmash_page.header).to_be_visible()
    time.sleep(3)
