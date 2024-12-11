values_file, tests_file, report_file = input().split()

with open(values_file, 'r') as f:
    values_data = eval(f.read().replace("null", "None"))

with open(tests_file, 'r') as f:
    tests_data = eval(f.read().replace("null", "None"))


values_dict = {}
for item in values_data["values"]:
    values_dict[str(item["id"])] = item["value"]

def fill_values(tests):
    for test in tests:
        if "id" in test:
            if str(test["id"]) in values_dict:
                test["value"] = values_dict[str(test["id"])]
            else:
                test["value"] = None
        if "values" in test:
            fill_values(test["values"])

fill_values(tests_data["tests"])

def format_json(data, indent=0):
    if type(data) == dict:
        result = "{\n"
        for key, value in data.items():
            result += " " * indent + '"' + key + '": ' + format_json(value, indent + 2) + ",\n"
        result = result.rstrip(",\n") + "\n" + " " * (indent - 2) + "}"
        return result
    elif type(data) == list:
        result = "[\n"
        for value in data:
            result += " " * indent + format_json(value, indent + 2) + ",\n"
        result = result.rstrip(",\n") + "\n" + " " * (indent - 2) + "]"
        return result
    elif type(data) == str:
        return '"' + data + '"'
    elif data is None:
        return "null"
    else:
        return str(data)

with open(report_file, 'w') as f:
    f.write("{\n" + format_json(tests_data, 2) + "\n}")
