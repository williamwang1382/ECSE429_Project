import requests
from behave import *

url="http://localhost:4567/todos"

default_todo1 = {
  "id": "1",
  "title": "scan paperwork",
  "doneStatus": "false",
  "description": "",
  "categories": [
    {
      "id": "1"
    }
  ],
  "tasksof": [
    {
      "id": "1"
    }
  ]
}

default_todo1_xml = f"""<todos><todo><doneStatus>false</doneStatus><description/><tasksof><id>1</id></tasksof><id>1</id><categories><id>1</id></categories><title>scan paperwork</title></todo></todos>"""

# Normal flow
@when(u'I send a GET request to the Rest API with a "<project_id>" value of "1"')
def step_impl(context):
    response = requests.get(url + "/1")
    context.response = response

@then(u'the default todo instance with the project_id value of "1" should be retrieved from the todo list with all its information as a JSON body')
def step_impl(context):
    assert context.response.headers['Content-Type'] == "application/json"

@then(u'the returned todo instance should have the corresponding project_id, title, doneStatus and description values')
def step_impl(context):
    res = context.response.json()['todos'][0]
    print(res)
    assert res['id'] == default_todo1['id']
    assert res['title'] == default_todo1['title']
    assert res['doneStatus'] == default_todo1['doneStatus']
    assert res['description'] == default_todo1['description']

# Alternate flow
@when(u'I send a GET request to the Rest API with a "<project_id>" value of "1" and I specify headers={"Accept": "application/xml"} in the request')
def step_impl(context):
    response = requests.get(url + "/1", headers={"Accept": "application/xml"})
    context.response = response

@then(u'the default todo instance with the project_id value of "1" should be retrieved from the todo list with all its information as an XML body')
def step_impl(context):
    assert context.response.headers['Content-Type'] == "application/xml"

@then(u'the returned todo instance should have the corresponding project_id, title, doneStatus and description values as XML')
def step_impl(context):
    res = context.response.text
    print(res)
    assert default_todo1_xml == res

# Error flow
@when(u'I send a GET request to the Rest API with a "<project_id>" value of "5000" and there is no todo instance with that project_id value')
def step_impl(context):
    response = requests.get(url + "/5000")
    context.response = response

@then(u'The Rest API should not return a valid todo instance')
def step_impl(context):
    assert context.response.json()['errorMessages'] != ""

