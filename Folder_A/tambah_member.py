import json
import os

# Konfigurasi data member baru
member_baru = {
    "User_ID": "IC-2026-001",
    "Nama": "Bewok Juri",
    "Email": "bewokjuri28@gmail.com",
    "Role": "Member",
    "Status": "Aktif"
}

# Path menuju file database di Folder_A
file_path = "database_member.json"

def daftar_member():
    data_semua_member = []

    # Cek jika file sudah ada, ambil data lama
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data_semua_member = json.load(file)
            except json.JSONDecodeError:
                data_semua_member = []

    # Tambahkan member baru ke list
    data_semua_member.append(member_baru)

    # Simpan kembali ke file
    with open(file_path, "w") as file:
        json.dump(data_semua_member, file, indent=4)
    
    print(f"Berhasil! Member {member_baru['Nama']} telah terdaftar di Folder_A.")

if __name__ == "__main__":
    daftar_member()

