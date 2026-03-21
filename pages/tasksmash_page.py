from playwright.sync_api import Page


class TaskSmashPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role("heading", name="Task Smash")
        self.add_task_button = page.locator("#btn_submit")

    def click_login(self):
        self.add_task_button.click()


#
