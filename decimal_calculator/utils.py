import re
from decimal import Decimal

calc_vars = {}


def process_set_var(input_str: str) -> bool:
    # set_var_pattern = r"(\w+)\s*=\s*([+-]?(?:\d+\.\d+|\d+|\.\d+))" # just allow number
    set_var_pattern = r"(\w+)\s*=\s*([^,]+)"
    if re.match(set_var_pattern, input_str):
        find_results = re.findall(set_var_pattern, input_str)
        for find_result in find_results:
            if re.match(r"^\d+$", find_result[0]):
                raise RuntimeError("Various name can not be numeric")
            calc_vars[find_result[0]] = convert_to_decimal_and_execute( find_result[1])
            print(f"{find_result[0]} = {calc_vars[find_result[0]]}")
        return True
    else:
        return False


def replace_var(input_str: str) -> str:
    replaced = input_str
    sorted_name = list(calc_vars.keys())
    sorted_name.sort(key=len, reverse=True)
    for var_name in sorted_name:
        if var_name == "_":
            continue
        var_val = calc_vars[var_name]
        pattern = fr"\b{var_name}\b(?!\()"
        replaced = re.sub(pattern, format(var_val, 'f'), replaced)
    return replaced


def ensure_input_safe(input_str: str):
    if re.match(r"\s*import\s+", input_str):
        raise RuntimeError("Import is not supported")


def convert_to_decimal_and_execute(input_str: str):
    ensure_input_safe(input_str)
    pattern = r'(?:\d+\.\d+|\d+|\.\d+)'
    modified_str = re.sub(pattern, r'Decimal("\g<0>")', input_str)
    # print("Decoded: ", modified_str)
    result = eval(modified_str)
    return result


def process_and_calc(input_str: str):
    if process_set_var(input_str):
        return ""
    modified_str = input_str
    if "_" in calc_vars:  # last result
        result_pattern = r'(?<![a-zA-Z0-9])_(?![a-zA-Z0-9])'
        modified_str = re.sub(result_pattern, lambda x: format(calc_vars["_"], 'f'), modified_str)
    modified_str = replace_var(modified_str)
    calc_vars["_"] = convert_to_decimal_and_execute(modified_str)
    return calc_vars["_"]
