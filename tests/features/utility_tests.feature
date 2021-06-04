Feature: Utility Tests

  @Unit
  Scenario: Check reading xls files steps
    Then I open "file_comparison_tests.xlsx" xlsx local file and check data on "merge_test" sheet:
      | A      | B    | C    |
      | Um     | dois | tres |
      | quatro |      |      |
      | cinco  |      | seis |