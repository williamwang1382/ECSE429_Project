

Feature: Delete a todo instance


As a user I want to be able to delete a todo task that I added by mistake or no longer want to complete
  
  Background:
    Given The Thingifier Rest API is running
    And the webpage with the todo list is open
    And the todo list is populated with at least the following default todo instances:
    | project_id | title                | doneStatus | description |
    | 2          | file paperwork       | false      |             |
    | 1          | scan paperwork       | false      |             |


    # Normal flow
    Scenario: Delete a todo with a valid project_id value
        When I send a DELETE request to the Rest API with a "<project_id>" value that exists in the todo list
        Then the default todo instance with the project_id value of "1" should be deleted from the todo list
        And the API should have a return status code of 200


    # Alternate flow
    Scenario: Delete a new todo instance that was already deleted previously
        When I send a DELETE request to the API with the "<project_id>" value that exists in the todo list after already deleting the todo instance with that project_id value
        Then the API should have a return status code of 404
        And There should not be any changes to the todo list


    # Error flow
    Scenario: Delete a todo with a non integer project_id value
        When I send a DELETE request to the Rest API with a "<project_id>" value of "Hello World" and there is no todo instance with that project_id value
        Then the API should have a return status code of 400
        And There should not be any changes to the todo list

    