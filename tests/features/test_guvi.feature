Feature:
    @smoke_test
    Scenario: This Test Verifies Page URl, Title and Navigate to Login Page and SignUp Page
      Given User Navigates to the URL and Validates the Page Title
      When User Click on Login Button
      And User should Land on Login page
      Then User Clicks on Signup Link
      And Navigate to Signup Page
      And User Click on Login to Navigate to Login Page







