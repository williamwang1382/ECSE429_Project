import requests
import random

url = "http://localhost:4567/todos"

# Graciously stop the tests if the API is not running
def before_all(context):
    base_url = "http://localhost:4567/todos"
    context.base_url = base_url  # Make the base URL accessible to other steps

    try:
        # Attempt to connect to the API with a short timeout
        response = requests.get(base_url, timeout=3)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    except ConnectionError:
        raise SystemExit("Error: API is not running. Please start the API and try again.")
    except Timeout:
        raise SystemExit("Error: Connection to API timed out. Ensure the API is reachable and try again.")
    

def before_feature(context, feature):
    random.shuffle(feature.scenarios)


# After scenario configuration to delete all non default todos
def after_scenario(context, scenario):
    response = requests.get(url)
    todos = response.json()['todos']
    for todo in todos:
        if todo['id'] != "1" and todo['id'] != "2":
            requests.delete(url + "/" + str(todo['id']))