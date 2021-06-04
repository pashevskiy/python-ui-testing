from pytest_bdd import scenarios

# if you need to make subfolder in features use an import like this
# from tests.functional.your_subfolder import * # pylint: disable=unused-wildcard-import

# It is just entrypoint which imports steps from other classes and locates feature files
scenarios('./features')
