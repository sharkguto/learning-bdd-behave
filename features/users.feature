Feature: Users management

    Everything in our platform , related with user management will be test here
    Scenario: List all users in platform
        Given I set the page number 2
        When I call api /api/users?page=2 , check status code 200
        Then I validate the output that should return 3 elements

    Scenario: Verify users from list all users
        Given I will give an id from the last scenario, randomically
        When I call api /api/users/<scenario1> with random data, check status code 200
        Then I Validate the output and check all data structure

    Scenario: Verify invalid users
        Given I will pass a invalid id user
        When I call api /api/users/999999999
        Then I validate if status code should be 404