import allure
from playwright_configs.browser_config import launch_browser


def before_all(context):
    context.browser, context.playwright = launch_browser(headless=False)


def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_default_timeout(10000)


def after_step(context, step):
    if step.status == "failed":
        context.page.screenshot(path=f"reports/screenshots/{step.name}.png")
        allure.attach.file(f"reports/screenshots/{step.name}.png", name="screenshot", attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
