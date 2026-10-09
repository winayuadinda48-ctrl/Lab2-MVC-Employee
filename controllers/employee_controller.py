from flask import render_template, request, redirect, url_for
from models.employee_model import Employee

def index():
    employees = Employee.get_all()
    return render_template('form.html', employees=employees)

def create():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = float(request.form['salary'])
        Employee.add(name, position, salary)
        return redirect(url_for('employee_index'))