@buy
Feature: Shopping cart, order and checkout

  Background:
    Given I am on the homepage

  @10
  Scenario: Info popup after adding an item to the cart
    And I see the featured items
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button
    Then I see the info popup

  @11
  Scenario: Show cart info - no items
    When I click on the cart button
    Then I see the info popup about the empty cart

  @12
  Scenario: Show cart info - with items
    And I see the featured items
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button
    And I click on the cart button
    Then I see the info popup with the cart items

  @13
  Scenario: Show items info in the cart
    And I see the featured items
    When I click on 1. item on page
    And I click on the 'Add to Cart' button

    And I continue to view cart with link in the info popup

    Then I see item info in the cart

  @14
  Scenario: Order checkout
    And I see the featured items
    When I click on 1. item on page
    And I click on the 'Add to Cart' button

    And I continue to 'Checkout' with the cart button on the page

    Then I see the order form with required fields and default values
    And Button 'Confirm Order' is disabled

  @15
  Scenario Outline: Search and buy item - view cart through the popup
    And I search for '<item>'
    And I see some search results
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button

    And I continue to view cart with link in the info popup

    And I see the item in the cart
    And I click on the 'Checkout' button
    And I fill out the order details
    And I confirm the order
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | mac     | 2     |
      | samsung | 1     |

  @16
  Scenario Outline: Search and buy item - view cart through the cart
    And I search for '<item>'
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button

    And I continue to 'View Cart' with the cart button on the page

    And I see the item in the cart
    And I click on the 'Checkout' button
    And I fill out the order details
    And I confirm the order
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | mac     | 3     |
      | samsung | 2     |

  @17
  Scenario Outline: Search and buy item - checkout through the cart
    And I search for '<item>'
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button

    And I continue to 'Checkout' with the cart button on the page

    And I fill out the order details
    And I confirm the order
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | mac     | 3     |
      | samsung | 2     |

  @18
  Scenario Outline: Buy featured item from homepage
    And I see the featured items
    When I click on <index>. item on page
    And I click on the 'Add to Cart' button

    And I continue to 'Checkout' with the cart button on the page

    And I fill out the order details
    And I confirm the order
    Then I see the order confirmation

    Examples:
      | index |
      #first item index
      | 1     |
      #last item index
      | 4     |
