class Employee:
    """
    The Employee class represents an individual employee with the following attributes:
    name: The name of the employee.
    age: The age of the employee.
    salary: The salary of the employee.
    """
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name} at age of {self.age} earning {self.salary}$"        

    def __repr__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary})"     

employee_1 = Employee("John", 32, 50_000) 
employee2 = Employee("Harry", 42, 80_000)
employee3 = Employee("Bob", 26, 55000)
#print(isinstance(employee_1, Employee)) 


class EmployeeManager:
    """
    The EmployeesManager class is responsible for managing a list of employees. It offers functionalities to:

    Add a new employee to the list.
    List all existing employees.
    Delete employees within a specified age range.
    Find an employee by their name.
    Update an employee's salary by name.

    """
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)     

    def list_employees(self):
        return self.employees

    # 1. Get a start and end age parametrs
    # 2. If employee.age in range(start, end)
    # 3. employees.remove(employee)    
    def delete_employee_by_age_range(self, start: int, end: int):
        for employee in self.employees[:]: # makes shallow copy of list, cause mutating list while looping is bad practice
            #print(f"Currently Checking Employee Age: {employee.age}") # For Debugging and Code Visualization

            if employee.age in range(start, end+1):
                print(f"Given employee - {employee} gonna be deleted.")
                self.employees.remove(employee)  

    def get_employee_by_name(self, name: str):
        for employee in self.employees:
            if name == employee.name:
                return employee
            
        return f"Employee with specified name '{name}' doesn't exist"  

    def update_salary_by_name(self, name, new_salary):
        employee = self.get_employee_by_name(name)
        if employee is not None:
            employee.salary = new_salary
            return f"{employee.name} got new salary: {employee.salary}$"  
                            
        return f"Employee with specified name '{name}' doesn't exist"  


manager = EmployeeManager()
#print(manager.list_employees()) # There object passes itself as argument automatically using 'self' keyword
#print(EmployeeManager.list_employees(manager)) # Does same thing, but here we need to pass the object as argument

# Verifying methods functionality
manager.add_employee(employee_1) 
manager.add_employee(employee2) 
manager.add_employee(employee3) 
#print(manager.list_employees())
#manager.delete_employee_by_age_range(25, 32)
#print(manager.list_employees())

print(manager.get_employee_by_name("John"))
print(manager.get_employee_by_name("Ron"))
print(manager.update_salary_by_name("Bob", 80_000))

# Logic for creating Class Objects from User Input                     
# 1. ask user how much Employee objects to create
# 2. loop till the number (for i in range(n) or using while loop)
# 3. Ask the user for the corresponding object parametrs
# 4. Assign the acquired parametr values to some variable name
# 5. append the employee variable name to employees list
"""employees_objects = []

desired_employee_num = int(input("How much Employees do you wanna create?: "))

for i in range(desired_employee_num):
    employee_name = str(input("Enter the Employee name: "))
    employee_age = int(input("Enter the Employee age: "))
    employee_salary = int(input("Enter the Employee salary: "))

    employee = Employee(employee_name, employee_age, employee_salary)
    employees_objects.append(employee)"""