from playwright.sync_api import sync_playwright


def launch_browser(headless=True):
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=headless)
    return browser, pw
