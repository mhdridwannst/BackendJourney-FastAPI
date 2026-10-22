# Belajar FastAPI

Isi repo ini adalah kumpulan kode latihan saya selama belajar FastAPI. Tujuan utamanya untuk memahami dasar-dasar backend web development pakai Python.

## Struktur Folder Saat Ini
* `main.py` - File utama untuk menjalankan aplikasi.
* `routers/` - Folder pemisah endpoint (sementara ada `users.py` dan `items.py`).

## Cara Menjalankan di Lokal

1. Aktifkan virtual environment Anda:
   ```bash
   .venv\Scripts\activate
   ```

2. Install library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan server lokal:
   ```bash
   uvicorn main:app --reload
   ```

Setelah server jalan, dokumentasi API bisa dibuka di: `http://127.0.0:8000`
