import pytest
import os
from playwright.sync_api import sync_playwright
from pages.page_manager import PageManager


@pytest.fixture(scope="session")
def browser(pytestconfig):
    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"

        if is_ci == "true":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def pm(page):
    return PageManager(page)
