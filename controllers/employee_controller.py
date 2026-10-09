# controllers/employee_controller.py
from flask import Blueprint, jsonify, request, render_template, redirect
from models.employee_model import EmployeeModel

print(__name__)

employee_bp = Blueprint("employee_bp", __name__)

# READ ALL -> GET /employees
@employee_bp.route("/employees", methods=["GET"])
def list_employees():
    return jsonify(EmployeeModel.employees), 200

# READ ONE -> GET /employees/3
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    employee = EmployeeModel.get_by_id(id)
    if employee:
        return jsonify(employee), 200
    return jsonify({"error": "Not found"}), 404

@employee_bp.route("/employees/new", methods=["GET"])
def show_form():
    return render_template("form.html", employees=EmployeeModel.employees)

# PROSES FORM -> POST /employees/new
@employee_bp.route("/employees/new", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    position = request.form.get("position", "Staff")
    salary = request.form.get("salary", 0)

    if not name:
        return "Nama wajib diisi!", 400

    new_id = max([e["id"] for e in EmployeeModel.employees], default=0) + 1
    new = {
        "id": new_id,
        "name": name,
        "position": position,
        "salary": int(salary) if salary else 0,
    }
    EmployeeModel.employees.append(new)

    return redirect("/employees/new")

# UPDATE FORM -> GET /employees/edit/<id>
@employee_bp.route("/employees/edit/<int:id>", methods=["GET"])
def edit_form(id):
    employee = EmployeeModel.get_by_id(id)
    return render_template("form.html", employee=employee)

# PROSES UPDATE -> POST /employees/update/<id>
@employee_bp.route("/employees/update/<int:id>", methods=["POST"])
def update_employee(id):
    name = request.form.get("name")
    position = request.form.get("position", "Staff")
    salary = request.form.get("salary", 0)

    EmployeeModel.update_employee(id, name, position, salary)
    return redirect("/employees/new")

# PROSES DELETE -> POST /employees/delete/<id>
@employee_bp.route("/employees/delete/<int:id>", methods=["POST"])
def delete_employee(id):
    EmployeeModel.delete_employee(id)
    return redirect("/employees/new")