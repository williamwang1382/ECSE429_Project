import requests
from behave import *

url="http://localhost:4567/todos"

# Since tere are only 2 default todos, the todo list length should be 2 when there is no additonal todos
default_length = 2

# Normal flow
@when(u'I send a GET request to the Rest API without specifying a project_id value')
def step_impl(context):
    response = requests.get(url)
    context.response = response


# Due to the after scenario configuration in environment.py, the todo list should only contain the 2 default todos
@then(u'I should get all of the existing todo instances in the todo list with their corresponding project_id, title, doneStatus and description values as a JSON body')
def step_impl(context):
    res = context.response.json()['todos']
    assert len(res) == default_length



# Alternate flow
@when(u'I send a GET request to the Rest API without specifying a project_id value but I specify the XML format and doneStatus as False')
def step_impl(context):
    response = requests.get(url+"?doneStatus=false", headers={"Accept": "application/xml"})
    context.response = response

# Since the default todos both have doneStatus as false, the todo list length should be 2 when there is no additonal todos
@then(u'I should get all of the existing todo instances in the todo list with their corresponding project_id, title, doneStatus and description values in XML format')
def step_impl(context):
    res = context.response.text
    # print(res)
    todo_count = res.count("<todo>")
    assert todo_count == default_length



# If we want to pass all the automated tests, comment out the error flow test for story test 5

# This error flow exposes an unexpected behavior in the API, where the API does not return an error message when the user specifies a non-existing field in the request
# Error flow
@when(u'I send a GET request to the Rest API on all the todo instance but I specify a filter that does not exist')
def step_impl(context):
    response = requests.get(url+"?badfield=badvalue")
    context.response = response

@then(u'I should not get any todo instances in the todo list')
def step_impl(context):
    print("Resulting JSON from Story test 5 Error flow: ", context.response.json())
    print("Resulting status code from Story test 5 Error flow: ",context.response.status_code)
    assert context.response.json()['errorMessages'] != ""