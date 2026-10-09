class Employee:
    # Menggunakan list/array sebagai tempat penyimpanan data sementara
    employees = [
        {'id': 1, 'name': 'Andi', 'position': 'Staff', 'salary': 6000000},
        {'id': 2, 'name': 'Budi', 'position': 'Manager', 'salary': 9000000},
        {'id': 5, 'name': 'rizki', 'position': 'office boy', 'salary': 1000000}
    ]

    @classmethod
    def get_all(cls):
        return cls.employees

    @classmethod
    def add(cls, name, position, salary):
        new_id = max([e['id'] for e in cls.employees], default=0) + 1
        new_employee = {
            'id': new_id,
            'name': name,
            'position': position,
            'salary': float(salary)
        }
        cls.employees.append(new_employee)