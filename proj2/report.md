# Test Report

- **Autor:** Marek Gergel (xgerge01)
- **Datum:** 2024-04-17

## Test changes

- Number of tests did not change
- Changed scenario indexes (#1) to scenario tags (@1) to allow execution of specific scenarios using tags
- Added feature tags to allow execution of specific features using tags
- Fixed few typos and renamed steps to be more descriptive

#### itemSearch.feature

- Fixed scenario example value to match expected result

#### itemBuy.feature

- Added step to scenario to fill out item required fields before adding to cart
```gherkin
    And I fill out the item required fields
```
- Removed step and used instead button name in common step
```gherkin
    PREVIOUS:
    And I confirm the order
    
    NOW:
    And I click on the "Confirm order" button
```

#### itemManagement.feature

- Upddated scenario with dateExpected values
```gherkin
    Then I see '<dateExpected>' value in 'Date Available' field

    Examples:
      | date        | dateExpected |
      | -0001-01-01 | 0001-01-01   |
      | 0000-01-01  | 0000-01-01   |
      | 2024-01-01  | 2024-01-01   |
      | 9999-01-01  | 9999-01-01   |
      | 10000-01-01 | 1000-01-01   |
```

## Bugs found

- cannot proceed to order summary, when adding a product to cart without weight 
    - field 'Shipping method' is not displayed in order checkout
    - item without weight: 'MacBook' , Product 16


## Test results

- some tests fail because of item quantity amount required for order checkout