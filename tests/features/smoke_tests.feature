@Smoke
Feature: Smoke tests

  @Stable @LogIn
  Scenario: Log In page simple navigation scenario
    Given I clean all data from database
    Given I apply "vanilla_data" SQL script
    Given I am on GrandTenders LogIn page
    Then Login page is shown
    When I click on Log In button
    Then Email input returns "Введите логин" validation error
    And Password input returns "Введите пароль" validation error
    When I type "xyz" in email input
    Then Email input returns "Логин должен быть корректным email адресом" validation error
    When I type "@zyx.xyz" in email input
    And I type "xyz" in password input
    Then I submit LogIn form and get "Имя пользователя или пароль неверные" alerts
    When I click on registration button
    Then Registration page is shown
    When I click on submit registration form button
    Then Full name input returns "Обязательное поле" validation error
    And Email input returns "Обязательное поле" validation error
    And Password input returns "Обязательное поле" validation error
    And Password-confirm input returns "Обязательное поле" validation error
    When I type "ab" in full name input
    And I type "qwerty" in password input
    And I type "xyz" in email input
    And I type "qwerty1" in password confirm input
    And I click on submit registration form button
    Then Full name input returns "Не менее 3-х символов" validation error
    And Email input returns "Логин должен быть корректным email адресом" validation error
    And Password input returns "Пароль не может быть менее 10 символов" validation error
    And Password-confirm input returns "Пароли не совпадают" validation error
    When I click on exit registration form button
    Then Login page is shown
    When I click on forgot password button
    Then Forgot password page is shown
    When I type "xyz" in email input
    Then Email input returns "Логин должен быть корректным email адресом" validation error
    When I click on exit forgot password form button
    Then Login page is shown

  @Stable
  Scenario: Check search block existing on every page
    Given I clean all data from database
    Given I apply "common_data" SQL script
    Given I successfully logged in as "user1" user
    Given I am on "Positions" page
    Then I check that search element is shown on page
    # ...

  @Stable
  Scenario: Export Test
    Given I clean all data from database
    Given I apply "common_data" SQL script
    When Clean temporary folder
    Given I successfully logged in as "user1" user
    Given I am on "Positions" page
    When I click on "Export" button
    Then I am waiting for "export.xlsx" file downloading within "20" seconds
    Then I open "export.xlsx" xlsx file and check data on "RequiredColumns" sheet:
      | A    | B    | C    |
      | ValA | ValB | ValC |
    When Clean temporary folder
    # ...