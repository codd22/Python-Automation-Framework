from behave import *
from playwright.sync_api import Locator


@given('I verify {element} status is {status}')
def i_verify_element_status(context, element, status):
    loc: Locator = getattr(context.iotDashboardPage, element, None)
    assert context.iotDashboardPage.getText(loc.locator('.status')) == status
