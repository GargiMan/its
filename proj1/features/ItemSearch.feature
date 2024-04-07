Feature: Search functionalities

  Background:
    Given I am on the homepage

    #1
  Scenario: Clicking on the search button
    When I click on the search button
    Then I see the search page
    And I see no search results

    #2
  Scenario Outline: Search for existing items
    When I search for '<item>'
    Then I see some search results

    Examples:
      | item    |
      | iphone  |
      | apple   |
      | samsung |

    #3
  Scenario Outline: Search for not existing items
    When I search for '<item>'
    Then I see no search results

    Examples:
      | item      |
      | ihponex   |
      | gloves    |
      | samsung10 |

    #4
  Scenario Outline: Search within categories
    When I click on the search button
    And I search for '<item>' within '<category>'
    Then I see some search results

    Examples:
      | item    | category       |
      | iphone  | Phones & PDAs  |
      | apple   | Monitors       |
      | samsung | Tablets        |
      | samsung | Desktops       |
      | iMac    | All Categories |

    #5
  Scenario: Disabled search in subcategories when searching in all categories
    When I click on the search button
    And I see selected value 'All Categories' in category dropdown
    Then I see the checkbox 'Search in subcategories' is disabled

    #6
  Scenario Outline: Search within subcategories
    When I click on the search button
    And I check checkbox 'Search in subcategories'
    And I select '<category>' in category dropdown
    And I search for '<item>'
    Then I see some search results

    Examples:
      | item    | category       |
      | iphone  | Phones & PDAs  |
      | apple   | Monitors       |
      | samsung | Tablets        |
      | samsung | Desktops       |
      | iMac    | All Categories |

    #7
  Scenario: Show product categories in search
    When I click on the search button
    Then I see the search categories
      | All Categories      |
      | Desktops            |
      | PC                  |
      | Mac                 |
      | Laptops & Notebooks |
      | Macs                |
      | Windows             |
      | Components          |
      | Mice and Trackballs |
      | Monitors            |
      | Printers            |
      | Scanners            |
      | Web Cameras         |
      | Tablets             |
      | Software            |
      | Phones & PDAs       |
      | Cameras             |
      | MP3 Players         |

    #8
  Scenario Outline: Search in product description
    When I click on the search button
    And I check checkbox 'Search in product descriptions'
    And I search for '<text>'
    Then I see some search results

    Examples:
      | text    |
      | intel   |
      | .       |
      | the     |

    #9
  Scenario Outline: Search in product description - no results
    When I click on the search button
    And I check checkbox 'Search in product descriptions'
    And I search for '<text>'
    Then I see no search results

    Examples:
      | text              |
      | $                 |
      | 1234567890        |
      | not existing text |
