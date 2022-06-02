from behave import *

@given('i am an emag user')
def step_impl(context):
    context.homePage.site_acces()

@when('click on  genius button')
def step_impl(context):
    context.homePage.click_genius_link( )

@then('i navigate to emag genius page')
def step_impl(context):
    context.genius_page.genius_link_check()
