from behave import *
from playwright.sync_api import Locator


@step('I verify {element} status is {status}')
def i_verify_element_status(context, element, status):
    loc: Locator = getattr(context.currentPage, element, None)
    assert context.currentPage.getText(loc.locator('.status')) == status
