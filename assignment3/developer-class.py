class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = float(salary)

class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

dev_1 = Developer("Ricardo", "Santiz", 60000, "Python")
print(f"Name: {dev_1.first} {dev_1.last}")
print(f"Language: {dev_1.prog_lang}")
print(f"Salary: {dev_1.salary}")