# 120140163-uts-pwl-backend

## Cara menjalankan

1. Clone repository ini
2. Buka terminal, lalu arahkan ke folder repository ini

## Menjalankan server grpc

1. Masuk ke folder server, lalu jalankan perintah `python3 -m venv env`
2. Aktifkan virtual environment dengan perintah `.\env\Scripts\activate` (Windows)
3. Install semua dependencies dengan perintah `.\env\Scripts\pip install -e .`
4. Lakukan migrasi database dengan perintah `.\env\Scripts\alembic upgrade head`
5. Generate grpc stub dengan perintah `.\env\Scripts\python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\proto\user.proto`
6. Jalankan server dengan perintah `.\env\Scripts\python3 server.py`

## Menjalankan client grpc

1. Masuk ke folder produk_client, lalu jalankan perintah `python3 -m venv env`
2. Aktifkan virtual environment dengan perintah `.\env\Scripts\activate` (Windows)
3. Install semua dependencies dengan perintah `.\env\Scripts\pip install -e .`
4. Generate grpc stub dengan perintah `.\env\Scripts\python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\proto\user.proto`
5. Jalankan client dengan perintah `.\env\Scripts\pserve development.ini --reload`

### Hasil

untuk melihat hasilnya, dapat dilihat di repostory frontend [disini](https://github.com/martatiaamanda/120140163-uts-pwl-frontend)
