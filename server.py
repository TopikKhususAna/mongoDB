import asyncio
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types
from database import MongoDBManager

# 1. Inisialisasi Server MCP
server = Server("mongodb-mcp-server")
db_manager = MongoDBManager()

# 2. Daftarkan "Tools" (Alat yang bisa dipakai AI)
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="cari_user",
            description="Mencari data mahasiswa dari MongoDB berdasarkan nama",
            inputSchema={
                "type": "object",
                "properties": {
                    "nama": {"type": "string", "description": "Nama mahasiswa yang dicari"},
                },
                "required": ["nama"],
            },
        )
    ]

# 3. Logika apa yang terjadi saat AI memanggil tool tersebut
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name == "cari_user":
        nama = arguments.get("nama")
        user = db_manager.get_user_by_name(nama)
        
        if user:
            # MongoDB mengembalikan data dengan _id (ObjectId) yang tidak bisa langsung jadi teks
            # Kita bersihkan sedikit datanya
            return [types.TextContent(type="text", text=f"Data ditemukan: {str(user)}")]
        else:
            return [types.TextContent(type="text", text=f"User dengan nama '{nama}' tidak ditemukan.")]
    
    raise ValueError(f"Tool tidak ditemukan: {name}")

# 4. Menjalankan server menggunakan standar I/O
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mongodb-mcp-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())