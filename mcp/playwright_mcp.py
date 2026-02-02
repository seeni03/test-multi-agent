from playwright.sync_api import sync_playwright
import json

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

def run_playwright_test(endpoint, validation_text):
    """
    Run a Playwright test to validate content on a webpage.

    Args:
        endpoint: The endpoint to test.
        validation_text: The text to validate on the page.

    Returns:
        bool: True if validation_text is found, False otherwise.
    """
    url = f"{config['base_url']}/{endpoint}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url)
            content = page.text_content("body")
            return validation_text in content
        except Exception as e:
            print(f"Error during Playwright test: {e}")
            return False
        finally:
            browser.close()
