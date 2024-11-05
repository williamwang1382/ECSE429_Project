import requests

url = "http://localhost:4567/todos"


# After scenario configuration to delete all non default todos
def after_scenario(context, scenario):
    response = requests.get(url)
    todos = response.json()['todos']
    for todo in todos:
        if todo['id'] != "1" and todo['id'] != "2":
            requests.delete(url + "/" + str(todo['id']))