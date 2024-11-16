*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    New Username  ville
    New Password  ville123
    New Password Confirmation  ville123
    Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    New Username  vi
    New Password  ville123
    New Password Confirmation  ville123
    Register Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    New Username  ville
    New Password  ville1
    New Password Confirmation  ville1
    Register Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    New Username  ville
    New Password  villeyykaakoo
    New Password Confirmation  villeyykaakoo
    Register Credentials
    Register Should Fail With Message  Invalid password - contains only letters

Register With Nonmatching Password And Password Confirmation
    New Username  ville
    New Password  ville123
    New Password Confirmation  ville234
    Register Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    New Username  kalle
    New Password  kalle345
    New Password Confirmation  kalle345
    Register Credentials
    Register Should Fail With Message  Username already in use

Login After Successful Registration
    New Username  ville
    New Password  ville123
    New Password Confirmation  ville123
    Register Credentials
    Register Should Succeed
    Go To Ohtu
    Logout User
    Set Username  ville
    Set Password  ville123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    New Username  ville
    New Password  ville1234
    New Password Confirmation  ville123
    Register Credentials
    Register Should Fail With Message  Passwords do not match
    Login User
    Set Username  ville
    Set Password  ville1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
New Username
    [Arguments]  ${username}
    Input Text  username  ${username}

New Password
    [Arguments]  ${password}
    Input Password  password  ${password}

New Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open

Register Credentials
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Go To Ohtu
    Click Link  Continue to main page

Logout User
    Click Button  Logout

Login User
    Click Link  Login

#Loginiin liittyvät avainsanat
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}