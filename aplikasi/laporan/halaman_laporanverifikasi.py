from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /verifikasi
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/verifikasi", methods=["GET"])
def tampilkan_halaman_laporanverifikasi():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("verifikasi.j2")


@app.route("/detailverifikasi", methods=["GET"])
def tampilkan_halaman_detailverifikasi():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailverifikasi.j2")