from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /dashboard
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/dashboard", methods=["GET"])
def tampilkan_halaman_dashboard():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("dashboard.j2")