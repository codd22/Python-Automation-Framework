from behave import *
from tests.utils.basePage import BasePage


@given('I open the url "{url}"')
def i_open_the_url(context, url: str):
    basepage = BasePage(context.page)
    basepage.navigate(url)
