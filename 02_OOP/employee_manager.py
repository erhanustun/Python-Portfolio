"""
employee_manager.py
-------------------
OOP example demonstrating:
- Composition (Manager uses Employee objects)
- Class methods (alternative constructors)
- Static methods (utility functions)
"""

class Employee:
    company_name = "TechCorp"  # class attribute (shared by all instances)

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.name} ({self.role}) - ${self.salary}"

    @classmethod
    def from_string(cls, emp_str):
        """
        Class method that creates an Employee object from a string.
        Example: "Alice,Engineer,5000"
        """
        name, role, salary = emp_str.split(",")
        return cls(name, role, int(salary))

    @staticmethod
    def is_high_salary(salary):
        """
        Static method to check if a salary is considered 'high'.
        It does not need access to self or cls.
        """
        return salary > 5000


class Manager:
    def __init__(self, name):
        self.name = name
        self.team = []  # Composition: Manager HAS a team of Employees

    def add_employee(self, employee):
        """Add an employee object to the manager's team."""
        self.team.append(employee)
        print(f" {employee.name} added to {self.name}'s team.")

    def list_team(self):
        """List all employees under this manager."""
        return [str(emp) for emp in self.team]

    def __str__(self):
        return f"Manager: {self.name}, Team size: {len(self.team)}"


if __name__ == "__main__":
    print(" Creating Employee objects...")
    emp1 = Employee("Alice", "Engineer", 4000)
    emp2 = Employee.from_string("Bob,Designer,6000")  # using class method

    print(emp1)
    print(emp2)

    print("\n Checking salary with static method:")
    print(f"Is {emp1.name}'s salary high?", Employee.is_high_salary(emp1.salary))
    print(f"Is {emp2.name}'s salary high?", Employee.is_high_salary(emp2.salary))

    print("\n Creating Manager and adding employees...")
    mgr = Manager("Eve")
    mgr.add_employee(emp1)
    mgr.add_employee(emp2)

    print(mgr)
    print("Team members:", mgr.list_team())
