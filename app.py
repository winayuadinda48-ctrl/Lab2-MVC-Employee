from flask import Flask
from controllers.employee_controller import index, create

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Mengatur routing (URL Rule) sesuai controller MVC
app.add_url_rule('/', 'employee_index', index)
app.add_url_rule('/employees/add', 'employee_create', create, methods=['POST'])

# Jalankan server lokal di port 5001 (biar aman di macOS)
if __name__ == '__main__':
    app.run(debug=True, port=5001)