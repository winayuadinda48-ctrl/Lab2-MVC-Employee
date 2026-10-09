# models/employee_model.py

class EmployeeModel:
    employees = [
        {"id": 1, "name": "Andi", "position": "Staff", "salary": 5000000},
        {"id": 2, "name": "Budi", "position": "Manager", "salary": 9000000},
        {"id": 3, "name": "Citra", "position": "VP", "salary": 12000000}
    ]

    @classmethod
    def get_by_id(cls, emp_id):
        for emp in cls.employees:
            if emp['id'] == emp_id:
                return emp
        return None

    @classmethod
    def update_employee(cls, emp_id, name, position, salary):
        for emp in cls.employees:
            if emp['id'] == emp_id:
                emp['name'] = name
                emp['position'] = position
                emp['salary'] = salary
                return True
        return False

    @classmethod
    def delete_employee(cls, emp_id):
        cls.employees = [emp for emp in cls.employees if emp['id'] != emp_id]
        return True