from behave import *
from tests.utils.pages.iotDashboardPage import IotDashboardPage


@given('I verify {element} is {status}')
def i_verify_element_status(context, element, status):
    iotDashboardPage = IotDashboardPage(context.page)
    if element == 'lightCardStatus':
        assert iotDashboardPage.getText(iotDashboardPage.lightCardStatus) == status
