import requests
from behave import *

url="http://localhost:4567/todos"




# Normal flow
@when(u'I send a DELETE request to the Rest API with a "<project_id>" value that exists in the todo list')
def step_impl(context):
    
    # Add new dummy node
    new_todo = {
        "title": "US2 test delete todo with valid project_id",
        "doneStatus": False,
        "description": "test delete todo"
    }
    response = requests.post(url, json=new_todo)
    assert response.status_code == 201
    context.id_value = response.json()['id']

    # Delete the todo
    context.response = requests.delete(url + "/" +str(context.id_value))


@then(u'the todo instance with the corresponding project_id value of should be deleted from the todo list')
def step_impl(context):
    # Get the deleted todo
    response = requests.get(url+ "/" +str(context.id_value))
    assert response.status_code == 404

@then(u'the API should have a return status code of 200')
def step_impl(context):
    assert context.response.status_code == 200


# Alternate flow
@when(u'I send a DELETE request to the API with the "<project_id>" value that exists in the todo list after already deleting the todo instance with that project_id value')
def step_impl(context):
    # Add new dummy node
    new_todo = {
        "title": "US2 test delete todo with already deleted project_id",
        "doneStatus": False,
        "description": "test delete todo"
    }
    response = requests.post(url, json=new_todo)
    assert response.status_code == 201
    context.id_value = response.json()['id']

    # Delete the todo
    response = requests.delete(url + "/" +str(context.id_value))
    assert response.status_code == 200

    # Get number of todos
    response = requests.get(url)
    context.num_todos = len(response.json()['todos'])

    # Delete the todo again
    context.response = requests.delete(url + "/" +str(context.id_value))


@then(u'the API should have a return status code of 404')
def step_impl(context):
    assert context.response.status_code == 404


@then(u'There should not be any changes to the todo list')
def step_impl(context):
    # Get number of todos
    response = requests.get(url)
    assert len(response.json()['todos']) == context.num_todos


# Error flow
@when(u'I send a DELETE request to the Rest API with a "<project_id>" value of "Hello World" and there is no todo instance with that project_id value')
def step_impl(context):
    # Get number of todos
    response = requests.get(url)
    context.num_todos = len(response.json()['todos'])
    context.response = requests.delete(url + "/Hello World")


