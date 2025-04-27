from tests.utils.basePage import BasePage
from tests.utils.pageObject.iotDashboardPageObject import IotDashboardPageObject


class IotDashboardPage(IotDashboardPageObject, BasePage):
    def __init__(self, page):
        super().__init__(page)
