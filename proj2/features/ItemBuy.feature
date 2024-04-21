@buy
Feature: Shopping cart, order and checkout

  Background:
    Given I am on the homepage

  @10
  Scenario Outline: Info popup after adding an item to the cart
    And I see the featured items
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button
    Then I see the info popup

    Examples:
      | index |
      | 1     |
      | 2     |

  @11
  Scenario: Show cart info - no items
    When I click on the cart button
    Then I see the cart popover without any items

  @12
  Scenario Outline: Show cart info - with items
    And I see the featured items
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button
    And I click on the cart button
    Then I see the cart popover with 1 item/s

    Examples:
      | index |
      | 1     |
      | 2     |

  #todo scenario for items with required fields

  @13
  Scenario: Show items info in the cart
    And I see the featured items
    When I click on 1. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to view cart with info popup

    Then I see the item in the cart

  @14
  Scenario: Order checkout
    And I see the featured items
    When I click on 1. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to checkout with the cart popover

    Then I see the order form with required fields and default values
    And I see the button 'Confirm Order' is disabled

  @15
  Scenario Outline: Search and buy item - view cart through the popup
    And I search for '<item>' in search bar
    And I see some search results
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to view cart with info popup

    And I see the item in the cart
    And I click on the 'Checkout' button
    And I fill out the order details
    And I click on the 'Confirm Order' button
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | mac     | 3     |
      | samsung | 2     |

  @16
  Scenario Outline: Search and buy item - view cart through the cart
    And I search for '<item>' in search bar
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to view cart with the cart popover

    And I see the item in the cart
    And I click on the 'Checkout' button
    And I fill out the order details
    And I click on the 'Confirm Order' button
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | mac     | 3     |
      | samsung | 2     |

  @17
  Scenario Outline: Search and buy item - checkout through the cart
    And I search for '<item>' in search bar
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to checkout with the cart popover

    And I fill out the order details
    And I click on the 'Confirm Order' button
    Then I see the order confirmation

    Examples:
      | item    | index |
      | iphone  | 1     |
      | samsung | 2     |

  @18
  Scenario Outline: Buy featured item from homepage
    And I see the featured items
    When I click on <index>. item on page
    And I fill out the item required fields
    And I click on the 'Add to Cart' button

    And I continue to checkout with the cart popover

    And I fill out the order details
    And I click on the 'Confirm Order' button
    Then I see the order confirmation

    Examples:
      | index |
      #first item index
      | 1     |
      #last item index
      | 4     |
