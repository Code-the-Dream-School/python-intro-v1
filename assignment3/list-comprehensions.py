import csv

with open('csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    

full_names = [f"{row[0]} {row[1]}" for row in data[1:]]
print(full_names)

names_with_e = [name for name in full_names if 'e' in name.lower()]
print(names_with_e)