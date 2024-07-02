Feature: Login in the application
  As a user
  I want to login in the application
  So that I can make purchases

  Scenario: Successful login with valid credentials
    Given I click on the Login button 
    And the login modal is opened
    When I enter valid credentials
    And I click on the login button
    Then I am redirected to the home page
    And I see my user logged