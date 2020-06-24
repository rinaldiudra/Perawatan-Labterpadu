from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /ditugaskan
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/ditugaskan", methods=["GET"])
def tampilkan_halaman_laporanditugaskan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("ditugaskan.j2")


@app.route("/detailditugaskan", methods=["GET"])
def tampilkan_halaman_detailditugaskan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailditugaskan.j2")