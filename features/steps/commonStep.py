from behave import *
from playwright.sync_api import Locator


@given('I open the url "{url}"')
def i_open_the_url(context, url: str):
    context.basePage.navigate(url)
    i_verify_the_page(context, 'IotDashboardPage')


@step('I verify the {page} loaded')
def i_verify_the_page(context, page):
    # Convert first letter to lowercase
    page_variable = page[0].lower() + page[1:]
    # Dynamically fetch the page object from context
    context.currentPage = getattr(context, page_variable)
    # Fetch the current url
    current_url = context.page.url
    # Fetch the sub url to verify
    sub_url = getattr(context.currentPage, 'url')
    # Verify the sub url contains in current url
    assert sub_url in current_url, f"Expected '{sub_url}' to be in URL '{current_url}'"


@when('I click on {element}')
def i_click_on_element(context, element):
    loc: Locator = getattr(context.currentPage, element, None)
    context.currentPage.clickOnElement(loc)
