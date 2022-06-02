from behave import *

@given('i am on genius page')
def step_impl(context):
    context.genius_page.genius_link_check()

@when('i click in free trial button')
def step_impl(context):
    context.genius_page.click_free_trial()

@then('i navigate to emag genius page')
def step_impl(context):
    context.genius_page.genius_link_check()
