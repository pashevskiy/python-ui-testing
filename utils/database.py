import psycopg2
import os

DUMP_FILEPATH = "./test_data/dumps/{name}.sql"


class GTDatabase:
    DELETE_ALL_FROM_TABLE = "delete from public.{table}"

    def __init__(self, connection):
        self.connection = psycopg2.connect(dbname=connection["database"], user=connection["user"],
                                           password=connection["password"], host=connection["host"],
                                           port=connection["port"], connect_timeout=3)

    def __del__(self):
        self.connection.close()

    def apply_script(self, script):
        script_filepath = os.path.abspath(DUMP_FILEPATH.format(name=script))
        with self.connection.cursor() as cursor:
            file = open(script_filepath, "r", encoding="utf-8").read()
            cursor.execute(file)
        self.connection.commit()

    def delete_from_table(self, table):
        with self.connection.cursor() as cursor:
            cursor.execute(self.DELETE_ALL_FROM_TABLE.format(table=table))
        self.connection.commit()
