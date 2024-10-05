# Created by Nivethitha at 10/5/2024
Feature: Test to Verify Target Signin functionality
  # Enter feature description here

  Scenario: User can access the signin form
    Given Open target main page
    Given Click sign in
    When Click sign in from the right side navigation menu
    Then Verify sign in form opened