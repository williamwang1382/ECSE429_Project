import requests
from test_todo_module_basic import url
import time



# Check if put request with new id works, should not be allowed
def test_todos_put_new_todo():
    # Create a new todo
    new_todo = {
        "title": "test put new todo",
        "doneStatus": False,
        "description": "test put new todo"
    }
    start_time = time.time()
    response = requests.post(url + "/20", json=new_todo)
    end_time = time.time()
    assert response.status_code == 404
    print("================================================================================")
    print("test_todos_put_new_todo:\n new todo created with id 20: " + str(new_todo))
    print("\nstatus code: ", response.status_code)
    print("Time to add 1 todo: ", end_time - start_time)




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
    print("================================================================================")
    start_time = time.time()
    response = requests.post(url, json=new_todo)
    end_time = time.time()
    assert response.status_code == 201
    id_value = int(response.json()['id'])

    print("Time to add 1 todo: ", end_time - start_time)

    # Get all todos
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    assert response.status_code == 200

    print("Time to get all todos: ", end_time - start_time)
    print("test_todos_put_duplicate_id:\n new todo created with id "+str(id_value)+": " + str(new_todo))
    print("\n All todos after adding new todo: ", response.json())


    data = {
        "id": id_value,
        "title": "test put duplicate id updated",
        "doneStatus": False,
        "description": "test put duplicate id updated"
    }

    start_time = time.time()
    response = requests.put(url + "/"+str(id_value), json=data)
    end_time = time.time()
    print("Time to put 1 duplicate todo: ", end_time - start_time)
    res = response.json()

    assert response.status_code == 200
    assert res['title'] == data['title']
    assert res['doneStatus'] == str(data['doneStatus']).lower()
    assert res['description'] == data['description']

    # Get all todos
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    assert response.status_code == 200
    print("Time to get all todos: ", end_time - start_time)
    print("\n All todos after updating new todo: ", response.json())

    # Delete the todo
    start_time = time.time()
    response = requests.delete(url + "/" +str(id_value))
    end_time = time.time()
    assert response.status_code == 200
    print("Time to delete 1 todo: ", end_time - start_time)




# Amend/update existing todo with post
def test_todos_post_duplicate_id():

    # Create a new todo
    new_todo = {
        "title": "test post duplicate id NOT UPDATED",
        "doneStatus": False,
        "description": "test post duplicate id NOT UPDATED"
    }

    start_time = time.time()
    response = requests.post(url, json=new_todo)
    end_time = time.time()
    assert response.status_code == 201

    print("================================================================================")
    print("test_todos_post_duplicate_id post new todo time to complete: ", end_time - start_time)

    id_value = int(response.json()['id'])


    data = {
        "id": id_value,
        "title": "test post duplicate id UPDATED",
        "doneStatus": False,
        "description": "test post duplicate id UPDATED"
    }

    start_time = time.time()
    response = requests.post(url+ "/"+str(id_value), json=data)
    end_time = time.time()
    print("test_todos_post_duplicate_id post duplicate todo time to complete: ", end_time - start_time)
    res = response.json()

    assert response.status_code == 200
    assert res['title'] == data['title']
    assert res['doneStatus'] == str(data['doneStatus']).lower()
    assert res['description'] == data['description']

    # Delete the todo
    start_time = time.time()
    response = requests.delete(url + "/" +str(id_value))
    end_time = time.time()
    assert response.status_code == 200
    print("test_todos_post_duplicate_id delete todo time to complete: ", end_time - start_time)




# Get a deleted todo by id, should return 404
def test_todos_get_deleted_todo():
    
    # Create a new todo
    new_todo = {
        "title": "test get deleted todo",
        "doneStatus": False,
        "description": "test get deleted todo"
    }

    print("================================================================================")

    start_time = time.time()
    response = requests.post(url, json=new_todo)
    end_time = time.time()

    assert response.status_code == 201
    id_value = response.json()['id']
    
    print("test_todos_get_deleted_todo post new todo time to complete: ", end_time - start_time)

    # Get all todos
    start_time = time.time()
    response2 = requests.get(url)
    end_time = time.time()
    assert response2.status_code == 200
    print("Time to get all todos: ", end_time - start_time)

    print("test_todos_get_deleted_todo:\n new todo created: " + str(new_todo))
    print("\n All todos after adding new todo: ", response2.json())


    # Delete the todo
    start_time = time.time()
    response = requests.delete(url + "/" +id_value)
    end_time = time.time()
    assert response.status_code == 200
    print("test_todos_get_deleted_todo delete todo time to complete: ", end_time - start_time)
    print("todo with id "+id_value+" deleted status code: ", response.status_code)

    # Get the deleted todo
    start_time = time.time()
    response = requests.get(url+ "/" +id_value)
    end_time = time.time()

    print("test_todos_get_deleted_todo get deleted todo time to complete: ", end_time - start_time)

    print("get deleted node id "+id_value+" status code: ", response.status_code)
    # print("get deleted node id "+id_value+" response: ", response.json())

    # Get all todos
    start_time = time.time()
    response2 = requests.get(url)
    end_time = time.time()
    assert response2.status_code == 200
    print("\n All todos after deleting new todo: ", response2.json())
    print("Time to get all todos: ", end_time - start_time)
    assert response.status_code == 404
