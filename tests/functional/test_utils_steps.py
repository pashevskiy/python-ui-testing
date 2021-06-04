import os.path
import time
import re
import py
import openpyxl
from pytest_bdd import given, parsers, then, when
from sttable import parse_str_table
import utils.dict_tools as dict_tools

LOCAL_REFERENCE_FILEPATH = "./test_data/reference_files/{name}"


def _extract_column_letter(coordinates):
    regex = re.search(r"([A-Z]+)[0-9]+", coordinates)
    return regex.group(1)


@then(parsers.parse("I check that table:\n{table1}\ncontains rows:\n{table2}"))
def table_contains_rows(table1, table2):
    table1p = parse_str_table(table1)
    table2p = parse_str_table(table2)
    dict_tools.assert_contains(table2p.rows, table1p.rows, True)


@then(parsers.parse("I check that table:\n{table1}\ndoesnt contain rows:\n{table2}"))
def table_contains_rows(table1, table2):
    table1p = parse_str_table(table1)
    table2p = parse_str_table(table2)
    dict_tools.assert_doesnt_contain(table2p.rows, table1p.rows, True)


@given(parsers.parse("I clean temporary folder"))
@when(parsers.parse("Clean temporary folder"))
def clean_temporary_directory(tmpdir_session: py.path.local):
    for file in tmpdir_session.listdir():
        file.remove()


@then(parsers.parse("I am waiting for \"{filename}\" file downloading within \"{wait_time}\" seconds"))
def wait_for_file_downloading_to_temp_folder(tmpdir_session: py.path.local, filename, wait_time):
    end_time = time.time() + int(wait_time)
    while time.time() < end_time:
        if tmpdir_session.join(filename).exists() and tmpdir_session.join(filename).isfile():
            assert True
            return
    assert False


@then(parsers.parse("I open \"{filename}\" xlsx local file and check data on \"{sheet}\" sheet:\n{table}"))
def open_local_file_and_check_data(filename, sheet, table):
    open_file_and_check_data(os.path.abspath(LOCAL_REFERENCE_FILEPATH.format(name=filename)), sheet, table)


@then(parsers.parse("I open \"{filename}\" xlsx file and check data on \"{sheet}\" sheet:\n{table}"))
def open_file_and_check_data(filename, sheet, table, tmpdir_session: py.path.local = ""):
    file = openpyxl.open(filename=str(filename if os.path.isabs(filename) else tmpdir_session.join(filename)))
    worksheet = file.get_sheet_by_name(sheet)
    actual = []
    for row in worksheet.iter_rows():
        actual_row = {}
        for cell in row:
            if cell.value is None:

                actual_row[_extract_column_letter(cell.coordinate)] = ""
            else:
                actual_row[_extract_column_letter(cell.coordinate)] = str(cell.value)
    expected = parse_str_table(table)
    file.close()
    assert expected.rows == actual, "Expected:\n{expected}\nActual:\n{actual}".format(expected=expected, actual=actual)


@when(parsers.parse("I open \"{filename}\" xlsx file and update data on \"{sheet}\" sheet:\n{table}"))
def open_file_and_update_data(tmpdir_session: py.path.local, filename, sheet, table):
    file = openpyxl.open(filename=str(tmpdir_session.join(filename)))
    worksheet = file.get_sheet_by_name(sheet)
    for updateRow in parse_str_table(table).rows:
        line = updateRow.pop("Line")
        for column in updateRow:
            if re.compile(r"<float>([0-9\.]+)").match(updateRow[column]):
                worksheet[column + line].value = float(updateRow[column].replace("<float>", ""))
            elif updateRow[column] == "<None>":
                worksheet[column + line].value = None
            else:
                worksheet[column + line].value = updateRow[column]
    file.save(filename=str(tmpdir_session.join(filename)))
