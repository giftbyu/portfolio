from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI() # <-- Pastikan baris ini ada dan nama variabelnya adalah 'app'
# Path ke direktori 'static'
static_dir = os.path.join(os.path.dirname(__file__), "static")

# 1. Sajikan file-file statis (CSS, JS, Gambar, dll.)
#    Ini akan membuat semua file di dalam folder 'static' dapat diakses melalui URL '/static'
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 2. Sajikan file index.html untuk halaman utama
@app.get("/")
async def read_root():
    """
    Endpoint ini akan menyajikan file index.html saat seseorang mengunjungi
    URL root (halaman utama).
    """
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))