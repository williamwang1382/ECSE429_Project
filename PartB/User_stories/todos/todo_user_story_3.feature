

Feature: Get an existing todo instance


As a user I want to be able to get information about a todo task that was added to the todo list
  
  Background:
    Given The Thingifier Rest API is running
    And the webpage with the todo list is open
    And the todo list is populated with at least the following default todo instances:
    | project_id | title                | doneStatus | description |
    | 2          | file paperwork       | false      |             |
    | 1          | scan paperwork       | false      |             |


    # Normal flow
    Scenario: Get a todo instance with a valid project_id value
        When I send a GET request to the Rest API with a "<project_id>" value of "1"
        Then the default todo instance with the project_id value of "1" should be retrieved from the todo list with all its information as a JSON body
        And the API should have a return status code of 200


    # Alternate flow
    Scenario: Get a todo instance with a valid project_id value but specifically in XML format
        When I send a GET request to the Rest API with a "<project_id>" value of "1" and I specify headers={"Accept": "application/xml"} in the request
        Then the default todo instance with the project_id value of "1" should be retrieved from the todo list with all its information as an XML body
        And the API should have a return status code of 200



    # Error flow
    Scenario: Get a todo instance with a non existing project_id value
        When I send a DELETE request to the Rest API with a "<project_id>" value of "50" and there is no todo instance with that project_id value
        Then the API should have a return status code of 404
        And The Rest API should not return a valid todo instance

    