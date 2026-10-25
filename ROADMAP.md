# Roadmap: Order Management API

## Definisi selesai (MVP)

### Backend

- [x] Fase 0-1: FastAPI, REST, Pydantic, struktur router/schema/service
- [x] Fase 2: PostgreSQL, SQLAlchemy 2.0, Alembic
- [x] Fase 3: argon2, JWT, OAuth2 form, ownership, role admin
- [ ] products (CRUD, tulis hanya admin)
- [ ] Pagination dan filter
- [ ] orders dan order_items, checkout dalam satu transaksi
- [ ] Rate limiting dan refresh token
- [ ] Test pytest untuk alur utama
- [ ] Docker Compose (API + Postgres) dan CI GitHub Actions
- [ ] Deploy

### Frontend (Angular, setelah backend dikunci)

- [ ] Login/register, daftar produk, checkout, riwayat order
- [ ] Disajikan lewat Nginx di Docker Compose yang sama

### Portofolio

- [ ] README dengan diagram arsitektur dan cara menjalankan
- [ ] Demo hidup atau video singkat

## Rancangan tabel

| Tabel       | Kolom | Tipe | Catatan |
| ----------- | ----- | ---- | ------- |
| products    | ...   | ...  | ...     |
| orders      | ...   | ...  | ...     |
| order_items | ...   | ...  | ...     |

Titik awal kolom: products (id, name, description, price, stock, created_at), orders (id, user_id FK, status, total, created_at), order_items (id, order_id FK, product_id FK, quantity, unit_price). Ubah kalau menurut lu ada yang kurang atau berlebih, dan tulis tipenya.

## Info

1. order_items terpisah: benar. Itu prinsip normalisasi (relasi one-to-many): satu order punya banyak item, jadi item ditaruh di tabel anak yang menunjuk ke orders lewat foreign key. Alternatif “kolom berisi daftar produk” bikin query seperti “produk apa paling laku” jadi sulit dan tidak bisa dijaga oleh foreign key.

2. Harga disalin: benar. Istilahnya price snapshot. Tambahan: hal yang sama berlaku untuk nama produk, diskon, dan pajak kalau nanti ada. Order lama harus bisa dibaca persis seperti saat transaksi terjadi.

3. Integer/Numeric: benar, tapi contoh angkanya perlu dikoreksi. 0.1 + 0.2 di float menghasilkan 0.30000000000000004 (di Python), bukan 0.300000004. Penyebabnya memang representasi biner (IEEE 754), jadi alasan lu benar, hanya angkanya yang meleset. Untuk rupiah, pilihan paling sederhana adalah integer rupiah (tanpa desimal), misalnya price: Mapped[int]. Pakai Numeric(12, 2) kalau butuh sen atau mata uang lain.
