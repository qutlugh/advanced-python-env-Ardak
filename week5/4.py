class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary 

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):  
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):  
        return "Manager"

    def get_bonus(self): 
        return self.bonus

def print_employee_details(employee_list):
    print("\n--- Task 4 Output ---")
    for emp in employee_list:
        role = emp.get_role()
        salary = emp.get_salary()
        print(f"Name: {emp.name} | Role: {role} | Salary: ${salary}")

emp1 = Employee("Alice", 50000)
mgr1 = Manager("Bob", 80000, 10000)
print_employee_details([emp1, mgr1])