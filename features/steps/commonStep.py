from behave import *


@given('I open the url "{url}"')
def i_open_the_url(context, url: str):
    context.basePage.navigate(url)
