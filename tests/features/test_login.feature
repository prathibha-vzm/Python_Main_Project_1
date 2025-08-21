Feature:
    @smoke_test
    Scenario Outline: To Validate Valid and Invalid User Login for Guvi page
      Given User Navigates to the URL
      When User Clicks on Login Link
      And User Enters Credentials <username> and <password> to Login
      Then The Valid User Should gets <expected_result> land on Dashboard
      And The Invalid User Should gets <expected_result>
      Examples:
         |  username                      |  password      | expected_result             |
         | vigneswaranprathibha@gmail.com | VZidane$23     | Login Successful            |
         | vigneswaranprathibha@gmail.com | VZid           | Incorrect Email or Password |