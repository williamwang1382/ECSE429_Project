import requests
import pytest


# Hardcoded todos, the default 2 todos that are hard-coded can be in any order
hardcoded_todos1: dict = {
        'todos': [
            {
                'id': '2', 'title': 'file paperwork', 'doneStatus': 'false', 'description': '', 'tasksof': [{'id': '1'}]
            }, 
            {
                'id': '1', 'title': 'scan paperwork', 'doneStatus': 'false', 'description': '', 'categories': [{'id': '1'}], 'tasksof': [{'id': '1'}]
            }
        ]
        }

hardcoded_todos2: dict = {
        'todos': [
             {
                'id': '1', 'title': 'scan paperwork', 'doneStatus': 'false', 'description': '', 'categories': [{'id': '1'}], 'tasksof': [{'id': '1'}]
            },
            {
                'id': '2', 'title': 'file paperwork', 'doneStatus': 'false', 'description': '', 'tasksof': [{'id': '1'}]
            }

        ]
        }

url="http://localhost:4567/todos"

# Test if the API page is reachable
def test_todos_reachable():
    response = requests.get("http://localhost:4567/gui/entities")
    assert response.status_code == 200


# Check if we get the right column names with get
def test_todos_get_column_names():
    response = requests.get(url)

    # Check if contains all 4 column titles
    info = response.json()['todos'][0]
    print("================================================================================")
    print("test_todos_get_column_names: ", info)
    assert 'id' in info
    assert 'title' in info
    assert 'doneStatus' in info
    assert 'description' in info

# Check headers with HEAD
def test_todos_head():
    response = requests.head(url)

    # Check if contains all elements in header
    info = response.headers
    print("================================================================================")
    print("test_todos_head info: ", info)
    assert 'Date' in info
    assert 'Content-Type' in info
    assert 'Transfer-Encoding' in info
    assert 'Server' in info




# Check if we get all the todos (the default 2 todos that are hard-coded)
def test_todos_get():
    response = requests.get(url)

    # Check if contains all 4 column titles
    res = response.json()
    print("================================================================================")
    print("test_todos_get all todos: ", res)

    assert response.status_code == 200
    assert res == hardcoded_todos1 or res == hardcoded_todos2

# Same Check test, get XML payload
def test_todos_get_xml():
    response = requests.get(url, headers={"Accept": "application/xml"})

    # Check if contains all 4 column titles
    res = response.text
    print("================================================================================")
    print("test_todos_get_xml res XML: ", res)

    assert response.status_code == 200



# Check if put works, should not be allowed
def test_todos_put():
    new_todo = {
        "title": "test put 1",
        "doneStatus": False,
        "description": "test put 1, regular test"
    }

    try:
        response = requests.put(url, json=new_todo)
        res = response.json()
    except ValueError:
        print("================================================================================")
        print("test_todos_put JSONDecoderError")
    assert response.status_code == 405




# Update the todo with new values
def test_todos_put_update():

    # Create a new todo
    new_todo = {
        "title": "test put update before 1",
        "doneStatus": False,
        "description": "test put update 1, before test"
    }

    response = requests.post(url, json=new_todo)

    res = response.json()

    # Check if the new todo has the correct values
    assert res['title'] == new_todo['title']
    assert res['doneStatus'] == str(new_todo['doneStatus']).lower()
    assert res['description'] == new_todo['description']

    # Update the todo
    new_todo = {
        "title": "test put update after 1",
        "doneStatus": True,
        "description": "test put update 1, after test"
    }

    response = requests.put(url+"/" + str(res['id']), json=new_todo)

    res = response.json()

    # Check if the new todo has the correct values
    assert res['title'] == new_todo['title']
    assert res['doneStatus'] == str(new_todo['doneStatus']).lower()
    assert res['description'] == new_todo['description']

    # Delete the todo
    response = requests.delete(url + "/" + str(res['id']))
    assert response.status_code == 200




def test_todos_post():
        new_todo = {
        "title": "test post 1",
        "doneStatus": False,
        "description": "test post 1, regular test"
        }

        response = requests.post(url , json = new_todo)

        print("================================================================================")
        print("test_todos_post new todo: ", new_todo)
        res = response.json()

        # Check if the new todo has the correct values
        assert res['title'] == new_todo['title']
        assert res['doneStatus'] == str(new_todo['doneStatus']).lower()
        assert res['description'] == new_todo['description']

        # Get all todos
        response = requests.get(url)
        resp = response.json()
        print("\nafter POST, todo list: ", resp)

        # Delete the todo
        response = requests.delete(url + "/" + str(res['id']))



# Post todo with existing id which should not be allowed by posting twice
def test_todos_post_existing_id():

    new_todo = {
        "title": "test post 2",
        "doneStatus": False,
        "description": "test post 2, regular test"
    }

    response = requests.post(url, json=new_todo)

    res = response.json()

    # Check if the status code indicates that a new todo was created
    assert response.status_code == 201

    id_value = int(res['id'])

    # Re-post the same todo with same id

    same_todo = {
        "id": id_value,
        "title": "test post 2",
        "doneStatus": False,
        "description": "test post 2, regular test"
    }

    response = requests.post(url, json=same_todo)

    # Check if the new todo has the correct values
    assert response.status_code == 400

    # Delete the todo
    response = requests.delete(url + "/" + str(id_value))
    assert response.status_code == 200



def test_todos_post_empty_title():
    new_todo = {
        "title": "",
        "doneStatus": False,
        "description": "test post empty title"
    }

    response = requests.post(url, json=new_todo)

    res = response.json()

    # Check if the new todo has the correct values
    assert response.status_code == 400
    print("================================================================================")
    print("empty title error status: ", response.status_code)




# Check if delete url works, should fail
def test_todos_delete_all():
    response = requests.delete(url)

    # Check if the new todo has the correct values
    assert response.status_code == 405
    print("================================================================================")
    print("test_todos_delete_all status: ", response.status_code)

    

# Delete a todo
def test_todos_delete():

    # Create dummy todo
    dummy_todo = {
        "title": "test delete 1",
        "doneStatus": False,
        "description": "test delete 1, regular test"
    }

    response = requests.post(url, json=dummy_todo)

    # Make sure todo was created
    assert response.status_code == 201

    id_value = response.json()['id']
    print("================================================================================")
    print("test_todos_delete with \"test delete 1\" dummy todo:", response.json())
    print("\n")

    # Delete the dummy todo
    response = requests.delete(url + "/" + id_value)

    # Check if the new todo has the correct values
    assert response.status_code == 200

    # Check if todo is deleted by getting all todos
    response = requests.get(url)
    assert response.status_code == 200
    print("test_todos_delete with \"test delete 1\" dummy todo DELETED:", response.json())


# Check API behavior when we provide a malformed JSON

def test_todos_post_malformed_json():
    new_todo = "malformed json"

    response = requests.post(url, json=new_todo)

    res = response.json()

    # Check if the new todo has the correct values
    assert response.status_code == 400
    print("================================================================================")
    print("malformed json error status: ", response.status_code)


# Check API behavior when we provide a malformed XML
def test_todos_post_malformed_xml():
    new_todo = "malformed xml"

    response = requests.post(url, headers={"Content-Type": "application/xml"}, data=new_todo)

    res = response.json()

    # Check if the new todo has the correct values
    assert response.status_code == 400
    print("================================================================================")
    print("malformed xml error status: ", response.status_code)





#################################################################################################################

# The following commented out tests must be run individually from the rest of the tests
# The 2 tests check whether the API id counter resets after deleting all todos
# The delete test relies on the assumption that only the 2 hardcoded default todos are present

# # Delete all todos
# def test_todos_delete_all():
#     response = requests.delete(url+"/1")

#     # Check if the new todo has the correct values
#     assert response.status_code == 200

#     response = requests.delete(url+"/2")
#     assert response.status_code == 200

# def test_todos_add_todo():
#     new_todo = {
#         "title": "test post 1",
#         "doneStatus": False,
#         "description": "test post 1, regular test"
#         }

#     response = requests.post(url , json = new_todo)
#     res = response.json()

#     # Check if the new todo has the correct values
#     assert res['title'] == new_todo['title']
#     assert res['doneStatus'] == str(new_todo['doneStatus']).lower()
#     assert res['description'] == new_todo['description']





