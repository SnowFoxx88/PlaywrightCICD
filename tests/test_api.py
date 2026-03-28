from playwright.sync_api import Playwright
from utils.api_base import APIUtils
import pytest


@pytest.mark.api
def test_login_api(playwright: Playwright):
    api = APIUtils(playwright)
    response = api.get_token("admin", "admin")
    assert response.ok
