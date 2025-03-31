import openpyxl

def read_test_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    test_data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_id, username, password, date, time, tester_name, result = row
        test_data.append((test_id, username, password, date, time, tester_name))

    return test_data
