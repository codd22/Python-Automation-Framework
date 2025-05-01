from playwright.sync_api import Page


class IotDashboardPageObject:
    def __init__(self, page: Page):
        self.page = page
        self.lightCard = self.page.locator('[ng-reflect-title="Light"]')
        self.lightCardStatus = self.lightCard.locator('.status')
        self.rollerShadesCard = self.page.locator('[ng-reflect-title="Roller Shades"]')
        self.rollerShadesCardStatus = self.rollerShadesCard.locator('.status')
        