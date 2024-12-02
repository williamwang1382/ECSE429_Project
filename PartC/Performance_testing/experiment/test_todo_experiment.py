import requests
import pytest
import time

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
    start_time = time.time()
    response = requests.post(url, json=new_todo)
    end_time = time.time()
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
    start_time = time.time()
    response = requests.put(url + "/"+str(id_value), json=updated_todo)
    end_time = time.time()
    assert response.status_code == 200

    time_to_update = end_time - start_time

    # Check time to complete delete request
    start_time = time.time()
    response = requests.delete(url + "/"+str(id_value))
    assert response.status_code == 200
    end_time = time.time()
    time_to_delete = end_time - start_time
    print()
    print("Time to add 1 todo: ", time_to_add)
    print("Time to update 1 todo: ", time_to_update)
    print("Time to delete 1 todo: ", time_to_delete)
    print("=====================================")




# Test Case 2: Add 10 objects
def test_add_10_todo():

    id_list = []
    # Record time to add 10 todos with only default todo instances in the list
    start_time = time.time()
    end_time = time.time()
    for i in range(10):

        # record time to add on 10th node
        if i == 9:
            # sleep to avoid  batching 
            time.sleep(0.1)
            start_time = time.time()

        # Create a new todo
        new_todo= {
            "title": "Experiment 2 todo number" + str(i+1),
            "doneStatus": False,
            "description": "todo instance for experiment 2"
        }
        response = requests.post(url, json=new_todo)
        assert response.status_code == 201
        id_list.append(int(response.json()['id']))
        if i == 9:
            end_time = time.time()

    time_to_add = end_time - start_time

    # Check time to complete update request
    updated_todo = {
        "title": "Experiment 2 todo updated",
        "doneStatus": True,
        "description": "todo instance for experiment 2 updated"
    }

    # Record time to update the last added todo for 10 new todos experiment
    start_time = time.time()
    id_value = id_list[9]
    response = requests.put(url + "/"+str(id_value), json=updated_todo)
    end_time = time.time()

    time_to_update = end_time - start_time

    # Check time to complete delete request
    start_time = time.time()
    response = requests.delete(url + "/"+str(id_value))
    end_time = time.time()
    time_to_delete = end_time - start_time

    print("Time to add 10 todos: ", time_to_add)
    print("Time to update 10 todos: ", time_to_update)
    print("Time to delete 10 todos: ", time_to_delete)
    print("=====================================")

    # Delete the rest of the todos
    for i in range(9):
        response = requests.delete(url + "/"+str(id_list[i]))
        assert response.status_code == 200

# Test Case 3: Add 100 objects
def test_add_100_todo():

    id_list = []
    # Record time to add 100 todos with only default todo instances in the list
    start_time = time.time()
    end_time = time.time()
    for i in range(100):

        # record time to add on 10th node
        if i == 99:
            # sleep to avoid  batching 
            time.sleep(0.1)
            start_time = time.time()

        # Create a new todo
        new_todo= {
            "title": "Experiment 3 todo number" + str(i+1),
            "doneStatus": False,
            "description": "todo instance for experiment 3"
        }
        response = requests.post(url, json=new_todo)
        assert response.status_code == 201
        id_list.append(int(response.json()['id']))
        if i == 99:
            end_time = time.time()

    time_to_add = end_time - start_time

    # Check time to complete update request
    updated_todo = {
        "title": "Experiment 3 todo updated",
        "doneStatus": True,
        "description": "todo instance for experiment 3 updated"
    }

    # Record time to update the last added todo for 100 new todos experiment
    start_time = time.time()
    id_value = id_list[99]
    response = requests.put(url + "/"+str(id_value), json=updated_todo)
    end_time = time.time()

    time_to_update = end_time - start_time

    # Check time to complete delete request
    start_time = time.time()
    response = requests.delete(url + "/"+str(id_value))
    end_time = time.time()
    time_to_delete = end_time - start_time

    print("Time to add 100 todos: ", time_to_add)
    print("Time to update 100 todos: ", time_to_update)
    print("Time to delete 100 todos: ", time_to_delete)
    print("=====================================")

    # Delete the rest of the todos
    for i in range(99):
        response = requests.delete(url + "/"+str(id_list[i]))
        assert response.status_code == 200


# Test Case 4: Add 1000 objects
def test_add_1000_todos():
    
    id_list = []
    # Record time to add 1000 todos with only default todo instances in the list
    start_time = time.time()
    end_time = time.time()
    for i in range(1000):

        # record time to add on 10th node
        if i == 999:
            # sleep to avoid  batching 
            time.sleep(0.1)
            start_time = time.time()

        # Create a new todo
        new_todo= {
            "title": "Experiment 4 todo number" + str(i+1),
            "doneStatus": False,
            "description": "todo instance for experiment 4"
        }
        response = requests.post(url, json=new_todo)
        assert response.status_code == 201
        id_list.append(int(response.json()['id']))
        if i == 999:
            end_time = time.time()

    time_to_add = end_time - start_time

    # Check time to complete update request
    updated_todo = {
        "title": "Experiment 4 todo updated",
        "doneStatus": True,
        "description": "todo instance for experiment 4 updated"
    }

    # Record time to update the last added todo for 1000 new todos experiment
    start_time = time.time()
    id_value = id_list[999]
    response = requests.put(url + "/"+str(id_value), json=updated_todo)
    end_time = time.time()

    time_to_update = end_time - start_time

    # Check time to complete delete request
    start_time = time.time()
    response = requests.delete(url + "/"+str(id_value))
    end_time = time.time()
    time_to_delete = end_time - start_time

    print("Time to add 1000 todos: ", time_to_add)
    print("Time to update 1000 todos: ", time_to_update)
    print("Time to delete 1000 todos: ", time_to_delete)
    print("=====================================")

    # Delete the rest of the todos
    for i in range(999):
        response = requests.delete(url + "/"+str(id_list[i]))
        assert response.status_code == 200



# Test 5 doesn't work because the server is not able to handle the requests
# # Test Case 5: Add 10000 objects
# def test_add_10000_todos():
    
#     id_list = []
#     # Record time to add 10000 todos with only default todo instances in the list
#     start_time = time.time()
#     end_time = time.time()
#     for i in range(10000):

#         # record time to add on 10th node
#         if i == 9999:
#             # sleep to avoid  batching 
#             time.sleep(0.1)
#             start_time = time.time()

#         # Create a new todo
#         new_todo= {
#             "title": "Experiment 4 todo number" + str(i+1),
#             "doneStatus": False,
#             "description": "todo instance for experiment 4"
#         }
#         response = requests.post(url, json=new_todo)
#         assert response.status_code == 201
#         id_list.append(int(response.json()['id']))
#         if i == 9999:
#             end_time = time.time()

#     time_to_add = end_time - start_time

#     # Check time to complete update request
#     updated_todo = {
#         "title": "Experiment 4 todo updated",
#         "doneStatus": True,
#         "description": "todo instance for experiment 4 updated"
#     }

#     # Record time to update the last added todo for 10000 new todos experiment
#     start_time = time.time()
#     id_value = id_list[9999]
#     response = requests.put(url + "/"+str(id_value), json=updated_todo)
#     end_time = time.time()

#     time_to_update = end_time - start_time

#     # Check time to complete delete request
#     start_time = time.time()
#     response = requests.delete(url + "/"+str(id_value))
#     end_time = time.time()
#     time_to_delete = end_time - start_time

#     print("Time to add 10 000 todos: ", time_to_add)
#     print("Time to update 10 000 todos: ", time_to_update)
#     print("Time to delete 10 000 todos: ", time_to_delete)
#     print("=====================================")

#     # Delete the rest of the todos
#     for i in range(9999):
#         response = requests.delete(url + "/"+str(id_list[i]))
#         assert response.status_code == 200