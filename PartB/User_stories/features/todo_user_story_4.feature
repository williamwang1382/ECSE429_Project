

Feature: Amend a todo instance


As a user I want to be able to update the information of a todo task that was added to the todo list
  Background:
    Given The Thingifier Rest API is running
    And the todo list is populated with at least the following default todo instances:
    | project_id | title                | doneStatus | description |
    | 2          | file paperwork       | false      |             |
    | 1          | scan paperwork       | false      |             |


    # Normal flow
    Scenario: Update an existing todo instance with a new title, new doneStatus and new description
        When I send a POST request to the API for a todo with an existing id, a new valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" value in the JSON request body
        Then the existing todo with the same projectg_id should have its title, doneStatus and description values updated to the new values
        And the API should have a return status code of 200


    # Alternate flow
    Scenario: Update an existing todo instance with a new title, new doneStatus and new description and specifies to use XML
        When I send a POST request to the API for a todo with an existing id, a new valid "<title>" value, a valid "<doneStatus>" value and a valid "<description>" in XML format
        Then the existing todo with the same projectg_id should have its title, doneStatus and description values updated to the new values
        And the API should have a return status code of 200


    # Error flow
    Scenario: Update an existing todo instance with a malformed JSON request body
        When I send a POST request to the API for a todo but the JSON request body is malformed and contains a single String
        Then the API should have a return status code of 400 
        And the existing todo instance should not have its values updated
    