class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee): 
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self._bonus = bonus

    def get_role(self): 
        return "Manager"

    def get_bonus(self):
        return self._bonus


def print_roles_and_salaries(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Salary: {emp.get_salary()}")

e1 = Employee(5000)
m1 = Manager(9000, 1000)

staff = [e1, m1]
print_roles_and_salaries(staff)