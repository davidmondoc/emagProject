from browser import Browser
from pages import home_page

def before_all(context):
    context.chrome=Browser()
    context.homePage=home_page.Home_page()

def after_all(context):
    context.chrome.close()