from behave import *
from features.page.register_page import RegisterPage

use_step_matcher('re')
@when('I open the register website "([^"]*)"')
def step_register(context,url):
    RegisterPage(context).get_url(url)
    # context.driver.get(url)

@then('I expect that the title is "([^"]*)"')
def step_register(context,title_name):
    title = context.driver.title
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register(context,useremail):
    RegisterPage(context).send_user_email(useremail)
    # context.driver.find_element_by_id('register_email').send_keys(useremail)

@when('I set with username "([^"]*)"')
def step_register(context,username):
    RegisterPage(context).send_user_name(username)
    # context.driver.find_element_by_id('register_nickname').send_keys(username)

@when('I set with password "([^"]*)"')
def step_register(context,password):
    RegisterPage(context).send_password(password)
    # context.driver.find_element_by_id('register_password').send_keys(password)

@when('I set with code "([^"]*)"')
def step_register(context,code):
    RegisterPage(context).send_code(code)
    # context.driver.find_element_by_id('register_code').send_keys(code)

@when('I click with registerbutton')
def step_register(context):
    RegisterPage(context).click_btn()
    # context.driver.find_element_by_id('register_btn').click()


@then('I expect that text "([^"]*)"')
def step_register(context,code_text):
    text = RegisterPage(context).get_title()
    assert code_text in text