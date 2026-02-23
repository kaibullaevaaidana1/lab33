class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + 500 * self.completed_projects


class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)




info = input().split()
role = info[0]
name = info[1]
base_salary = int(info[2])


if role == "Manager":
    bonus_percent = int(info[3])
    emp = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    completed_projects = int(info[3])
    emp = Developer(name, base_salary, completed_projects)
elif role == "Intern":
    emp = Intern(name, base_salary)
else:
    raise ValueError("Unknown role")

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")