
UI testing sample project

This project provides an example how to build UI automation tests.

The project implements BDD testing and Page Object, both patterns contain sample obfuscated data. Also, the repo contains dockerfile packaging all tests into Docker image.

This project is based on the next stack:
 - python3 - as a programming language
 - pytest + pytest-bdd - testing framework and plugin for it providing possibility to write testing scenarios by gherkin syntax
 - splinter - it is webdriver wrapper that allows performing actions in browser
 - psycopg2-binary - jdbc client
 - openpyxl - reading/writing into xlsx files
