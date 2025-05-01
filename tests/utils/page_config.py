from tests.utils.basePage import BasePage
from tests.utils.pages import *


def configPages(context):
    context.basePage = BasePage(context.page)
    context.iotDashboardPage = IotDashboardPage(context.page)
