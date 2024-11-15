*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Test Cases ***
Click Login Link
    Go To  ${HOME_URL}
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Go To  ${HOME_URL}
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***

Reset Application And Go To Starting Page
  Reset Application
  Go To Starting Page