from playwright.sync_api import Page


class TaskSmashPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role("heading", name="Task Smash")
        self.add_task_button = page.locator("#btn_submit")
        self.task_field = page.locator("#content")
        self.logout_button = page.get_by_role("link", name="Logout")

    def click_logout(self):
        self.logout_button.click()

    def enter_task(self, task):
        self.task_field.fill(task)

    def click_add_task(self):
        self.add_task_button.click()
