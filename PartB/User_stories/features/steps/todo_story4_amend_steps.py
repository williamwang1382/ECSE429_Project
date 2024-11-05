import requests
from behave import *

url="http://localhost:4567/todos"


# Normal flow
@when(u'I send a POST request to the API for a todo with an existing id, a new valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" value in the JSON request body')
def step_impl(context):
    # Create a new todo
    new_todo = {
        "title": "US4 test post amend NOT UPDATED",
        "doneStatus": False,
        "description": "US4 test post amend NOT UPDATED"
    }
    response = requests.post(url, json=new_todo)
    assert response.status_code == 201

    # Get the id of the new todo
    context.id_value = int(response.json()['id'])


    context.title = "US4 test post amend UPDATED"
    context.doneStatus = True
    context.description = "US4 test post amend UPDATED"
    # Amend the todo
    data = {
        "id": context.id_value,
        "title": context.title,
        "doneStatus": context.doneStatus,
        "description": context.description
    }

    context.response = requests.post(url+ "/"+str(context.id_value), json=data)

@then(u'the existing todo with the same projectg_id should have its title, doneStatus and description values updated to the new values')
def step_impl(context):
    res = context.response.json()
    assert res['title'] == context.title
    assert res['doneStatus'] == str(context.doneStatus).lower()
    assert res['description'] == context.description


# Alternate flow
@when(u'I send a POST request to the API for a todo with an existing id, a new valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" in XML format')
def step_impl(context):
    # Create a new todo WITH XML format
    new_todo = f"""
    <todo>
        <doneStatus>false</doneStatus>
        <description>US4 Amend XML NOT UPDATED</description>
        <title>US4 Amend XML NOT UPDATED</title>
    </todo>
    """
    response = requests.post(url, data=new_todo, headers={"Content-Type": "application/xml"})
    print(response.status_code)
    assert response.status_code == 201

    # Get the id of the new todo
    context.id_value = int(response.json()['id'])

    context.title = "US4 test post amend UPDATED XML"
    context.doneStatus = True
    context.description = "US4 test post amend UPDATED XML"
    
    # Amend the todo
    updated_todo = f"""
    <todo>
        <doneStatus>true</doneStatus>
        <description>US4 test post amend UPDATED XML</description>
        <title>US4 test post amend UPDATED XML</title>
    </todo>
    """
    context.response = requests.post(url+ "/"+str(context.id_value), data=updated_todo, headers={"Content-Type": "application/xml"})


# Error flow
@when(u'I send a POST request to the API for a todo but the JSON request body is malformed and contains a single String')
def step_impl(context):
    # Create a new todo
    new_todo = {
        "title": "US4 test post amend malformed JSON NOT UPDATED",
        "doneStatus": False,
        "description": "US4 test post amend malformed missing comma JSON NOT UPDATED"
    }
    response = requests.post(url, json=new_todo)
    assert response.status_code == 201

    # Get the id of the new todo
    context.id_value = int(response.json()['id'])

    context.title = "US4 test post amend malformed JSON UPDATED"
    context.doneStatus = True
    context.description = "US4 test post amend malformed missing comma UPDATED"
    
    # Amend the todo
    data = "malformed json"

    context.response = requests.post(url+ "/"+str(context.id_value), json=data)

@then(u'the existing todo instance should not have its values updated')    
def step_impl(context):
    # Get the todo
    response = requests.get(url+ "/" +str(context.id_value))
    res = response.json()['todos'][0]
    print(res)
    assert res['title'] != context.title
    assert res['doneStatus'] != str(context.doneStatus).lower()
    assert res['description'] != context.description
