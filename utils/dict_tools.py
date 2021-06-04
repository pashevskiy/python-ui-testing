from datetime import date

SMART_EQUAL = {
    "<today>": lambda expected: date.today().strftime("%d.%m.%Y") == expected,
    "<some_integer>": lambda expected: expected.isdigit(),
}


def dict_diff(expected, current, partial=False, as_str=True):
    diff_list = []
    if partial:
        if any(elem not in list(current.keys()) for elem in list(expected.keys())):
            return ["Current dictionary keys are not include expected keys. Expected: {expected} Current: {current}"
                        .format(expected=list(expected.keys()), current=list(current.keys()))]
    else:
        if not expected.keys() == current.keys():
            return ["Dictionary keys are not equal. Expected: {expected} Current: {current}"
                        .format(expected=expected.keys(), current=current.keys())]
    for key, value in expected.items():
        if value in SMART_EQUAL.keys():
            if not SMART_EQUAL[value](current[key]):
                diff_list.append(f"Expected value '{key}:{value}' doesn't met mask '{key}:{current[key]}'")
        elif as_str:
            if not str(value) == str(current[key]):
                diff_list.append(
                    f"Expected value '{key}:{str(value)}' is not equal to current value '{key}:{str(current[key])}'")
        else:
            if not value == current[key]:
                diff_list.append(f"Expected value '{key}:{value}' is not equal to current value '{key}:{current[key]}'")
    return diff_list


def contains_diff(expected, current, partial=False):
    diff_list_lines = []
    if not isinstance(current, list):
        current = [current]

    if not isinstance(expected, list):
        expected = [expected]
    assert len(current) >= len(
        expected), f"Length of expected list ({len(expected)}) is more than current ({len(current)})"
    for dict2 in expected:
        not_found = True
        for dict1 in current:
            diff_list = dict_diff(dict2, dict1, partial)
            if len(diff_list) == 0:
                not_found = False
        if not_found:
            diff_list_lines.append("{line} was not found".format(line=dict2))
    return diff_list_lines


def equal_diff(expected, current, partial=False):
    diff_list_lines = []
    if not isinstance(current, list):
        current = [current]

    if not isinstance(expected, list):
        expected = [expected]

    assert len(current) == len(expected), f"Length of expected list ({len(expected)}) " \
                                          f"is not equal to current ({len(current)})"

    for index in range(len(expected)):
        diff = dict_diff(expected[index], current[index], partial)
        if len(diff) > 0:
            details = '\n\t\t'.join(diff)
            diff_list_lines.append(f"{index} line contains difference(s):\n\t\t{details}")

    return diff_list_lines


def doesnt_contain_diff(expected, current, partial=False):
    diff_list_lines = []
    if not isinstance(current, list):
        current = [current]

    if not isinstance(expected, list):
        expected = [expected]
    for dict2 in expected:
        found = False
        for dict1 in current:
            diff_list = dict_diff(dict2, dict1, partial)
            if len(diff_list) == 0:
                found = True
        if found:
            diff_list_lines.append("{line} was found".format(line=dict2))
    return diff_list_lines


def assert_contains(expected, current, partial=False):
    message = f"\nExpected:\n{expected} \n Current:\n{current}\nDetails:\n\t"
    diff = contains_diff(expected, current, partial)
    assert len(diff) == 0, message + "\n\t".join(diff)


def assert_equal(expected, current, partial=False):
    message = f"\nExpected:\n{expected} \n Current:\n{current}\nDetails:\n\t"
    diff = equal_diff(expected, current, partial)
    assert len(diff) == 0, message + "\n\t".join(diff)


def assert_doesnt_contain(expected, current, partial=False):
    message = f"\nExpected:\n{expected} \n Current:\n{current}\nDetails:\n\t"
    diff = doesnt_contain_diff(expected, current, partial)
    assert len(diff) == 0, message + "\n\t".join(diff)

