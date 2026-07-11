# MongoDB MCP Server (Python Edition)

Proyek ini adalah implementasi **Model Context Protocol (MCP)** menggunakan **Python** untuk menghubungkan AI (seperti GitHub Copilot/Claude) dengan database **MongoDB**. Proyek ini mendemonstrasikan integrasi database NoSQL dalam ekosistem AI Agent.

## 🚀 Fitur Utama
- **NoSQL Integration**: Menggunakan MongoDB sebagai penyimpanan data fleksibel (Berorientasi Dokumen).
- **Automated Testing**: Pengujian koneksi dan fungsi CRUD menggunakan `pytest`.
- **MCP Protocol**: Menyediakan *tool* `cari_user` agar AI bisa melakukan query ke database secara langsung.
- **Python-Based**: Menggunakan library `pymongo` dan `mcp` SDK.

## 📁 Struktur Folder
- `database.py`: Logika utama koneksi dan fungsi CRUD MongoDB.
- `server.py`: Implementasi server MCP untuk diekspos ke AI Client.
- `test_database.py`: Script pengujian otomatis.
- `read_data.py`: Script sederhana untuk verifikasi data di terminal.
- `.vscode/settings.json`: Konfigurasi integrasi ke VS Code.

## 🛠️ Persiapan Lingkungan

1. **Instalasi MongoDB**: Pastikan MongoDB Community Edition dan MongoDB Compass sudah terinstal di port `27017`.
2. **Instalasi Library**:
   ```bash
   py -m pip install pymongo pytest mcp


## 🧪 Cara Menjalankan Testing
Sebelum menjalankan server, pastikan database berfungsi dengan benar:
```bash
py -m pytest test_database.py

🤖 Integrasi dengan VS Code (Copilot)
Tambahkan konfigurasi berikut pada .vscode/settings.json:

{
    "mcp.servers": {
        "mongodb-python": {
            "command": "py",
            "args": ["D:/mcp_server/server.py"]
        }
    }
}
