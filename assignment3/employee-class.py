
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = float(salary)
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def give_raise(self, amount):
        self.salary += amount

emp_1 = Employee("Ricardo", "Santiz", 50000)
print(emp_1.email)
print(f"Old Salary: {emp_1.salary}")
emp_1.give_raise(5555)
print(f"New Salary: {emp_1.salary}")
