from behave import *


@given('I verify {element} is {status}')
def i_verify_element_status(context, element, status):
    if element == 'lightCardStatus':
        assert context.iotDashboardPage.getText(context.iotDashboardPage.lightCardStatus) == status
