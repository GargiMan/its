@management
Feature: Manage items

  Background:
    Given I am on the administration page and logged in

  @19
  Scenario: Show catalog of products
    When I open the catalog of 'Products'
    Then I see product list with columns
      | Image        |
      | Product Name |
      | Model        |
      | Price        |
      | Quantity     |
      | Action       |
    And I see filter section with fields
      | Product Name |
      | Model        |
      | Price        |
      | Quantity     |
      | Status       |
    And I see buttons for product list management
      | Add New |
      | Copy    |
      | Delete  |

  @20
  Scenario: Show product stock fields
    When I open the catalog of 'Products'
    And I click on edit button for 1. product
    And I go to 'Data' tab
    Then I see stock section with fields
      | Quantity            |
      | Minimum Quantity    |
      | Subtract Stock      |
      | Out Of Stock Status |
      | Date Available      |

  @21
  Scenario Outline: Edit product stock - Quantity, Minimum Quantity
    When I open the catalog of 'Products'
    And I click on edit button for <index>. product
    And I go to 'Data' tab
    And I set '<quantity>' value to 'Quantity' field
    And I set '<quantity>' value to 'Minimum Quantity' field
    And I save the product changes
    And I see success saving message
    And I refresh the page
    And I go to 'Data' tab
    Then I see '<quantitySaved>' value in 'Quantity' field
    And I see '<quantitySaved>' value in 'Minimum Quantity' field
    And I go back to the product list
    And I see <index>. product with '<quantitySaved>' value in 'Quantity' column

    Examples:
      | index | quantity    | quantitySaved |
      | 1     | -2147483649 | -2147483648   |
      | 2     | -2147483648 | -2147483648   |
      | 3     | 0           | 0             |
      | 4     | 2147483647  | 2147483647    |
      | 5     | 2147483648  | 2147483647    |

  @22
  Scenario Outline: Edit product stock - Out Of Stock Status
    When I open the catalog of 'Products'
    And I click on edit button for <index>. product
    And I go to 'Data' tab
    And I select '<option>' in '<field>' dropdown
    And I save the product changes
    And I see success saving message
    And I refresh the page
    And I go to 'Data' tab
    Then I see option '<option>' selected in '<field>' dropdown

    Examples:
      | index | field               | option       |
      | 1     | Out Of Stock Status | 2-3 Days     |
      | 2     | Out Of Stock Status | In Stock     |
      | 3     | Out Of Stock Status | Out Of Stock |
      | 4     | Out Of Stock Status | Pre-Order    |

  @23
  Scenario: Edit product stock - Subtract Stock
    When I open the catalog of 'Products'
    And I click on edit button for 1. product
    And I go to 'Data' tab
    And I toggle 'Subtract Stock' option
    And I save the product changes
    And I see success saving message
    And I refresh the page
    And I go to 'Data' tab
    Then I see saved 'Subtract Stock' option

  @24
  Scenario Outline: Edit product stock - Date Available
    When I open the catalog of 'Products'
    And I click on edit button for 1. product
    And I go to 'Data' tab
    And I set '<date>' value to 'Date Available' field
    And I save the product changes
    And I see success saving message
    And I refresh the page
    And I go to 'Data' tab
    Then I see '<dateExpected>' value in 'Date Available' field

    Examples:
      | date        | dateExpected |
      | -0001-01-01 | 0001-01-01   |
      | 0000-01-01  | 0000-01-01   |
      | 2024-01-01  | 2024-01-01   |
      | 9999-01-01  | 9999-01-01   |
      | 10000-01-01 | 1000-01-01   |
