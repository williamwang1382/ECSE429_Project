

Feature: Create a new todo instance


As a user I want to be able to add a task I want to complete to a todo list
  
  Background:
    Given The Thingifier Rest API is running
    And the todo list is populated with at least the following default todo instances:
    | project_id | title                | doneStatus | description |
    | 2          | file paperwork       | false      |             |
    | 1          | scan paperwork       | false      |             |


    # Normal flow
    Scenario: Add a new todo with all valid values
        When I send a POST request to the API for a new todo with a valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" value in the JSON request body
        Then the new todo should be added to the todo list with the corresponding project_id, title, doneStatus and description values
        And the API should have a return status code of 201


    # Alternate flow
    Scenario: Add a new todo with missing values
        When I send a POST request to the API for a new todo with a valid "<title>" value in the JSON request body but without specifying the "<doneStatus>" and description "<values>"
        Then the new todo should be added to the todo list with the corresponding title and have its project_id automatically generated, have its doneStatus set to false and have an empty description
        And the API should have a return status code of 201


    # Error flow
    Scenario: Add a new todo with missing title
        When I send a POST request to the API for a new todo without specifying the "<title>" value in the JSON request body
        Then the API should have a return status code of 400
        And the new todo should not be added to the todo list
    