from playwright.sync_api import Page


class IotDashboardPageObject:
    def __init__(self, page: Page):
        self.page = page
        self.lightCard = self.page.locator('[ng-reflect-title="Light"]')
        self.rollerShadesCard = self.page.locator('[ng-reflect-title="Roller Shades"]')
        self.wirelessAudioCard = self.page.locator('[ng-reflect-title="Wireless Audio"]')
        self.coffeeMakerCard = self.page.locator('[ng-reflect-title="Coffee Maker"]')
