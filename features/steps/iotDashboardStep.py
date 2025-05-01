from behave import *


@given('I verify {element} is {status}')
def i_verify_element_status(context, element, status):
    locator = getattr(context.iotDashboardPage, element, None)
    assert context.iotDashboardPage.getText(locator) == status
