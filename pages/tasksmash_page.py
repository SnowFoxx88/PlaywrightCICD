from playwright.sync_api import Page, expect


class TaskSmashPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role("heading", name="Task Smash")
        self.add_task_button = page.locator("#btn_submit")
        self.task_field = page.locator("#content")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.task_rows = page.locator("tbody").get_by_role("row")

    def click_logout(self):
        self.logout_button.click()

    def enter_task(self, task):
        self.task_field.fill(task)

    def click_add_task(self):
        self.add_task_button.click()

    def get_task_locator(self, task):
        target_row = self.task_rows.filter(has_text=task)
        return target_row

    def delete_task(self, task):
        target_row = self.task_rows.filter(has_text=task)
        target_row.get_by_role("link", name="Delete").click()
