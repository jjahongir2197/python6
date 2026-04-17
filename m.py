class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


def main():
    e1 = Employee("Ali", 3000)
    e2 = Employee("Vali", 4000)

    employees = [e1, e2]

    for e in employees:
        e.increase_salary(10)
        e.display()
        print("------")


main()
