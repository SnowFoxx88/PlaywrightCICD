import pytest
from playwright.sync_api import sync_playwright, Browser


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser
