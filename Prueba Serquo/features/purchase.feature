Feature: Purchase items in the application
as a logged user or not logged user
  I want to purchase items

  Scenario: Successfully purchase  item
    Given I am on the home page
    When I add an item to the cart
    And I proceed to purchase
    And I fill in the information details
    And I confirm the purchase
    Then I see a confirmation message