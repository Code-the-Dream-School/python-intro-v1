import csv
import sys
import os
import math
import random
from datetime import datetime

minutes_list = []

def read_employees():
    employees_dict = {}
    try:
        with open('../csv/employees.csv' , 'r') as file:
            reader = csv.reader(file)
            all_data = list(reader)
            employees_dict["fields"] = all_data[0]
            employees_dict["rows"] = all_data[1:]
            return employees_dict
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit()

employees = read_employees()

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4 

def first_name(row_number):
    name_col_index = column_index("first_name")

    row = employees["rows"][row_number]
    return row[name_col_index]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    last_name_index = column_index("last_name")

    employees["rows"].sort(key=lambda row: row[last_name_index])

    return employees["rows"]

sort_by_last_name()

# Task 8
def employee_dict(row):
    emp_dict = {}
    for index, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        emp_dict[field] = row[index]
    return emp_dict

# Task 9

def all_employees_dict():
    big_dict = {}
    id_index = column_index("employee_id")
    for row in employees["rows"]:
        emp_id = row[id_index]
        big_dict[emp_id] = employee_dict(row)
    return big_dict

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11

def string_formatting(row_number):
    name = first_name(row_number)
    return f"The employee name is {name}."

# Task 12
def grid_avg(value):
    return round(value, 2)

# Task 13
def take_square_root(value):
    return math.sqrt(value)

# Task 14
def dice_roll():
    return random.randint(1, 6)

# Task 15
def read_minutes():
    with open('minutes.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = []
        for row in reader:
            date_obj = datetime.strptime(row[1], "%B %d, %Y")
            rows.append((row[0], date_obj))
    return {"fields": header, "rows": rows}, rows

# Task 16
def create_minutes_set():
    data_dict, rows = read_minutes()
    return {row[0] for row in rows}

# Task 17
def create_minutes_list():
    global minutes_list
    data_dict, rows = read_minutes()
    minutes_list = rows
    return minutes_list

# Task 18
def write_sorted_list():
    m_list = create_minutes_list()
    m_list.sort(key=lambda x: x[0])
    final_list = []
    with open('sorted_minutes.txt', 'w') as file:
        for name, date in m_list:
            date_str = date.strftime("%B %d, %Y")
            file.write(f"{name}, {date_str}\n")
            final_list.append((name, date_str))
    return final_list