# Created by Nivethitha at 10/5/2024
Feature: Test to verify target cart
  # Enter feature description here

  Scenario: User can verify Target cart
    Given Open target main page
    When Click on cart icon
    Then Verify your cart is empty message is shown