import requests
from test_todo_module_basic import url





# Amend/update existing todo with put
def test_todos_put_duplicate_id():
     
    # Create a new todo
    new_todo = {
        "title": "test put duplicate id not updated",
        "doneStatus": False,
        "description": "test put duplicate id not updated",
        "tasksof": [
            {
                "id": "1"
            }
        ]
    }

    response = requests.post(url, json=new_todo)
    assert response.status_code == 201
    id_value = int(response.json()['id'])

    # Get all todos
    response = requests.get(url)
    assert response.status_code == 200

    print("================================================================================")
    print("test_todos_put_duplicate_id:\n new todo created with id "+str(id_value)+": " + str(new_todo))
    print("\n All todos after adding new todo: ", response.json())


    data = {
        "id": id_value,
        "title": "test put duplicate id updated",
        "doneStatus": False,
        "description": "test put duplicate id updated"
    }

    response = requests.put(url + "/"+str(id_value), json=data)
    res = response.json()

    assert response.status_code == 200
    assert res['title'] == data['title']
    assert res['doneStatus'] == str(data['doneStatus']).lower()
    assert res['description'] == data['description']

    # Get all todos
    response = requests.get(url)
    assert response.status_code == 200
    print("\n All todos after updating new todo: ", response.json())

    # Delete the todo
    response = requests.delete(url + "/" +str(id_value))
    assert response.status_code == 200




# Amend/update existing todo with post
def test_todos_post_duplicate_id():

    # Create a new todo
    new_todo = {
        "title": "test post duplicate id NOT UPDATED",
        "doneStatus": False,
        "description": "test post duplicate id NOT UPDATED"
    }

    response = requests.post(url, json=new_todo)
    assert response.status_code == 201
    id_value = int(response.json()['id'])


    data = {
        "id": id_value,
        "title": "test post duplicate id UPDATED",
        "doneStatus": False,
        "description": "test post duplicate id UPDATED"
    }

    response = requests.post(url+ "/"+str(id_value), json=data)
    res = response.json()

    assert response.status_code == 200
    assert res['title'] == data['title']
    assert res['doneStatus'] == str(data['doneStatus']).lower()
    assert res['description'] == data['description']

    # Delete the todo
    response = requests.delete(url + "/" +str(id_value))
    assert response.status_code == 200




# Get a deleted todo by id, should return 404
def test_todos_get_deleted_todo():
    
    # Create a new todo
    new_todo = {
        "title": "test get deleted todo",
        "doneStatus": False,
        "description": "test get deleted todo"
    }

    response = requests.post(url, json=new_todo)

    assert response.status_code == 201
    id_value = response.json()['id']


    # Get all todos
    response2 = requests.get(url)
    assert response2.status_code == 200
    print("================================================================================")
    print("test_todos_get_deleted_todo:\n new todo created: " + str(new_todo))
    print("\n All todos after adding new todo: ", response2.json())


    # Delete the todo
    response = requests.delete(url + "/" +id_value)
    assert response.status_code == 200
    print("todo with id "+id_value+" deleted status code: ", response.status_code)

    # Get the deleted todo
    response = requests.get(url+ "/" +id_value)

    print("get deleted node id "+id_value+" status code: ", response.status_code)
    # print("get deleted node id "+id_value+" response: ", response.json())

    # Get all todos
    response2 = requests.get(url)
    assert response2.status_code == 200
    print("\n All todos after deleting new todo: ", response2.json())

    assert response.status_code == 404
