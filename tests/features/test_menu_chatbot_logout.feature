Feature:
    @smoke_test
    Scenario Outline: Verify Menu Items and Dobby
      Given User Enters Guvi page
      When User Verifies Navigation Bar
      And Click on Login Link
      Then User Enters Valid Credentials <username> and <password> to Login
      And User Checks for Dobby Chatbot
      And User Clicks SignOut and Land on Home Page
      Examples:
         |  username                      |  password      |
         | vigneswaranprathibha@gmail.com | VZidane$23     |