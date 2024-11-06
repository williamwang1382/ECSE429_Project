import requests
from behave import *
from requests.exceptions import ConnectionError, Timeout

url="http://localhost:4567/todos"




@given(u'The Thingifier Rest API is running')
def step_impl(context):

    try:
        response = requests.get(url)
        assert response.status_code == 200
    except ConnectionError:
        raise RuntimeError("API is not running. Please start the API and try again.")
    except Timeout:
        raise RuntimeError("API connection timed out. Please ensure the API is reachable.")

@given(u'the todo list is populated with at least the following default todo instances')
def step_impl(context):
    response = requests.get(url)

    # Check if the todo list has at least 2 default todo instances
    assert len(response.json()['todos']) >= 2


# Normal flow
@when(u'I send a POST request to the API for a new todo with a valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" value in the JSON request body')
def step_impl(context):
    context.title = "US1 title + doneStatus + description"
    context.doneStatus = False
    context.description = "description"
    new_todo = {
        "title": "US1 title + doneStatus + description",
        "doneStatus": False,
        "description": "description"
    }
    context.response = requests.post(url, json=new_todo)

@then(u'the new todo should be added to the todo list with the corresponding project_id, title, doneStatus and description values')
def step_impl(context):

    assert context.response.json()['title'] == context.title
    assert context.response.json()['doneStatus'] == (str(context.doneStatus)).lower()
    assert context.response.json()['description'] == context.description


@then(u'the API should have a return status code of 201')
def step_impl(context):
    assert context.response.status_code == 201




# Alternative flow
@when(u'I send a POST request to the API for a new todo with a valid "<title>" value in the JSON request body but without specifying the "<doneStatus>" and description "<values>"')
def step_impl(context):
    context.title = "US1 only title"
    new_todo = {
        "title": "US1 only title"
    }
    context.response = requests.post(url, json=new_todo)

@then(u'the new todo should be added to the todo list with the corresponding title and have its project_id automatically generated, have its doneStatus set to false and have an empty description')
def step_impl(context):
    assert context.response.json()['title'] == context.title
    assert context.response.json()['doneStatus'] == "false"
    assert context.response.json()['description'] == ""


# Error flow
@when(u'I send a POST request to the API for a new todo without specifying the "<title>" value in the JSON request body')
def step_impl(context):
    new_todo = {}
    context.initial_length = len(requests.get(url).json()['todos'])
    context.response = requests.post(url, json=new_todo)

@then(u'the API should have a return status code of 400')
def step_impl(context):
    assert context.response.status_code == 400

@then(u'the new todo should not be added to the todo list')
def step_impl(context):
    assert len(requests.get(url).json()['todos']) == context.initial_length

