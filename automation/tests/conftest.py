import pytest
from playwright.sync_api import sync_playwright


# @pytest.fixture(params=["chromium", "firefox", "edge"])
@pytest.fixture(params=["edge"])
def launch_browser(request):
    browser_type = request.param
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False, channel="chrome")
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=False, channel="firefox")
        elif browser_type == "edge":
            browser = p.chromium.launch(headless=False, channel="msedge")
        else:
            raise ValueError("Unsupported browser")
        # browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.dominos.co.in/")
        page.wait_for_load_state("networkidle")
        yield page
        page.close()
        context.close()
