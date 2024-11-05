

Feature: Get all the existing todo instances


As a user I want to be able to see a list of all the todo tasks that I have to complete
  
  Background:
    Given The Thingifier Rest API is running
    And the webpage with the todo list is open
    And the todo list is populated with at least the following default todo instances:
    | project_id | title                | doneStatus | description |
    | 2          | file paperwork       | false      |             |
    | 1          | scan paperwork       | false      |             |


    # Normal flow
    Scenario: Get all of the existing todo instances
        When I send a GET request to the Rest API without specifying a project_id value
        Then I should get all of the existing todo instances in the todo list with their corresponding project_id, title, doneStatus and description values as a JSON body
        And the API should have a return status code of 200


    # Alternate flow
    Scenario: Get all of the existing todo instances in XML format
        When I send a GET request to the Rest API without specifying a project_id value
        Then I should get all of the existing todo instances in the todo list with their corresponding project_id, title, doneStatus and description values in XML format
        And the API should have a return status code of 200


    # Error flow
    Scenario: Get all of the existing todo instances with an incorrect url 
        When I send a GET request to the Rest API without specifying a project_id value but with the incorrect url address in the request
        Then I should not get any todo instances in the todo list
        And the API should have a return status code of 404
