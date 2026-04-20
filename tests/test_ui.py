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


@pytest.mark.ui
@pytest.mark.parametrize("user_credentials", credentials)
def test_login_logout(pm: PageManager, user_credentials):
    pm.login_page.open_url(url)
    pm.login_page.enter_username(user_credentials["username"])
    pm.login_page.enter_password(user_credentials["password"])
    pm.login_page.click_login()
    expect(pm.tasksmash_page.header).to_be_visible()
    pm.tasksmash_page.click_logout()
    expect(pm.login_page.logout_message).to_be_visible()


@pytest.mark.ui
@pytest.mark.parametrize("user_credentials", credentials)
def test_add_task(pm: PageManager, user_credentials):
    pm.login_page.open_url(url)
    pm.login_page.enter_username(user_credentials["username"])
    pm.login_page.enter_password(user_credentials["password"])
    pm.login_page.click_login()
    pm.tasksmash_page.enter_task("Smash Admin")
    task = pm.tasksmash_page.enter_task("Smash Admin")
    pm.tasksmash_page.click_add_task()
    expect(pm.tasksmash_page.get_task_locator(task)).to_be_visible()
    # pm.tasksmash_page.delete_task(task)
    time.sleep(5)
