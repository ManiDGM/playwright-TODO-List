from playwright.sync_api import sync_playwright

def sample():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # headless=False to see the browser
        page = browser.new_page()
        
        # Go to a website
        page.goto('http://127.0.0.1:5500/index.html')
        
        page.locator("#taskInput").type("practice playwright")
        page.wait_for_timeout(3000)
        page.click("#addTaskButton")
        page.wait_for_timeout(3000)

        page.screenshot(path="add-task.png")

        page.click(".fas.fa-check")  # fixed selector
        page.wait_for_timeout(3000)

        page.screenshot(path="done-task.png")


        page.click(".fas.fa-trash")  # fixed selector
        page.wait_for_timeout(3000)

        page.screenshot(path="delete-task.png")
        
        # Close browser
        browser.close()


if __name__ == "__main__":
    sample()
