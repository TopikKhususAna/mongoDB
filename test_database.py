import pytest
from database import MongoDBManager

def test_mongodb_connection():
    # Inisialisasi manager
    manager = MongoDBManager()
    
    # Data dummy untuk ditest
    test_user = {
        "nama": "Testing Python",
        "jurusan": "Teknik",
        "status": "Trial"
    }

    # Test 1: Apakah bisa insert data?
    inserted_id = manager.insert_user(test_user)
    assert inserted_id is not None

    # Test 2: Apakah data yang tadi dimasukkan bisa dicari lagi?
    found_user = manager.get_user_by_name("Testing Python")
    assert found_user is not None
    assert found_user["jurusan"] == "Teknik"

    manager.close_connection()