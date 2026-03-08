import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Browser starten
        if os.getenv("CI") == "true":
            return {**p, "headless": True}
        else:
            browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    # Synchroner Kontext
    page = browser.new_page()
    yield page
    page.close()
