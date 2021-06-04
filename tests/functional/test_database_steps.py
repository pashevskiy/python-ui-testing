import time
from pytest_bdd import given, parsers, then, when
from utils.database import GTDatabase


@given(parsers.parse("I apply \"{script}\" SQL script"))
def apply_sql_script(script, database: GTDatabase):
    database.apply_script(script)
    time.sleep(5)


@given(parsers.parse("I clean next tables in DB: \"{tables}\""))
def clean_tables(tables, database: GTDatabase):
    for table in tables.split(","):
        database.delete_from_table(table)


@given(parsers.parse("I clean all data from database"))
def clean_all_data(database: GTDatabase):
    # Add user tables into "data" array
    data = []

    for table in data:
        database.delete_from_table(table)
