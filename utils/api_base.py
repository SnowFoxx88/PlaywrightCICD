from playwright.sync_api import Playwright
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")


class APIUtils:
    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.api_context = playwright.request.new_context(base_url=url)

    def get_token(self, username: str, password: str):
        response = self.api_context.post("/login", form={"username": username, "password": password})
        return response
