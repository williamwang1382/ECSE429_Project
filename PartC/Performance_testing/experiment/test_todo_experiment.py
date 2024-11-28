import requests
import pytest
import datetime

# Experiment: As the number of objects increases measure the time required to add, delete, or change the objects.
url="http://localhost:4567/todos"
# Test Case 1: Add 1 object
def test_add_one_todo():

    # Create a new todo
    new_todo= {
        "title": "Experiment 1 todo",
        "doneStatus": False,
        "description": "todo instance for experiment 1"
    }
    # Record time to add 1 todo with only default todo instances in the list
    start_time = datetime.datetime.now()
    response = requests.post(url, json=new_todo)
    end_time = datetime.datetime.now()
    assert response.status_code == 201


    time_to_add = end_time - start_time

    id_value  = int(response.json()['id'])

    # Check time to complete update request
    updated_todo = {
        "id": id_value,
        "title": "Experiment 1 todo updated",
        "doneStatus": True,
        "description": "todo instance for experiment 1 updated"
    }

    # Record time to update a todo with only 1 new todo
    start_time = datetime.datetime.now()
    response = requests.put(url + "/"+str(id_value), json=updated_todo)
    end_time = datetime.datetime.now()
    assert response.status_code == 200

    time_to_update = end_time - start_time

    # Check time to complete delete request




# Test Case 2: Add 10 objects

# Test Case 3: Add 100 objects