class Employee:
    def __init__(self, emp_id, name, salary, performance):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.performance = performance.capitalize()

    def bonus_calculate(self):
        if self.performance == "Excellent":
            bonus = self.salary * 0.20
        elif self.performance == "Good":
            bonus = self.salary * 0.10
        elif self.performance == "Average":
            bonus = self.salary * 0.05
        else:
            bonus = 0
        return bonus

    def display(self):
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Performance:", self.performance)
        print("Employee Bonus:", self.bonus_calculate())


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = int(input("Enter Employee Salary: "))
performance = input("Enter Employee Performance (Excellent/Good/Average): ")

emp = Employee(emp_id, name, salary, performance)
emp.display()