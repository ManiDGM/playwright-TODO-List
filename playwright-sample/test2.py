import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def before_each(page: Page):
    page.goto("http://127.0.0.1:5500/index.html")


def test(page: Page):
    

    page.locator("#taskInput").type("practice playwright")
    page.click("#addTaskButton")
    page.wait_for_timeout(3000)

    # Expect the new task to appear in the list
    expect(page.locator("li", has_text="practice playwright")).to_be_visible()

    page.screenshot(path="screenshots/add-task.png")

    page.click(".fas.fa-check")
    page.wait_for_timeout(3000)


    page.screenshot(path="screenshots/done-task.png")

    page.click(".fas.fa-trash")
    page.wait_for_timeout(3000)

    page.screenshot(path="screenshots/delete-task.png")
