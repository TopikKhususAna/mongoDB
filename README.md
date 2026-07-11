# MongoDB MCP Server (Python Edition)

Proyek ini adalah implementasi sederhana dari Model Context Protocol (MCP) menggunakan Python untuk menghubungkan AI agent dengan database MongoDB. Tujuan utamanya adalah memungkinkan alat seperti GitHub Copilot atau Claude untuk membaca dan memanipulasi data dari MongoDB melalui tool yang terdefinisi.

## Fitur Utama
- Integrasi dengan MongoDB menggunakan library `pymongo`
- Menyediakan tool `cari_user` untuk pencarian data berdasarkan nama
- Mendukung pengujian otomatis dengan `pytest`
- Dapat diintegrasikan ke VS Code melalui konfigurasi MCP

## Struktur Folder
- `database.py`: berisi logika koneksi ke MongoDB dan operasi CRUD dasar
- `server.py`: implementasi server MCP yang mengekspor tool ke AI client
- `read_data.py`: skrip sederhana untuk melihat data dari MongoDB di terminal
- `test_database.py`: file pengujian untuk memverifikasi fungsi database
- `.vscode/`: konfigurasi untuk integrasi dengan VS Code

## Persyaratan
Pastikan perangkat Anda sudah memiliki:
- Python 3.10+
- MongoDB berjalan di `localhost:27017`
- Paket Python berikut:

```bash
py -m pip install pymongo pytest mcp
```

## Cara Menjalankan
### 1. Jalankan MongoDB
Pastikan server MongoDB sudah aktif.

### 2. Jalankan pengujian
```bash
py -m pytest test_database.py
```

### 3. Jalankan server MCP
```bash
py server.py
```

## Contoh Integrasi dengan VS Code
Tambahkan konfigurasi berikut ke file `.vscode/settings.json`:

```json
{
  "mcp.servers": {
    "mongodb-python": {
      "command": "py",
      "args": ["D:/mcp_server/server.py"]
    }
  }
}
```

## Catatan
Project ini cocok untuk dipakai sebagai contoh dasar implementasi MCP dengan database NoSQL, terutama untuk pembelajaran integrasi AI dengan MongoDB.
