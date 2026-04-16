import json
import os
import time



import os
import time

def bersihkan_hilir():
    # Menghitung batas waktu 7 hari
    batas_waktu = time.time() - (7 * 24 * 60 * 60)
    folder_hilir = "cache_data/"

    if not os.path.exists(folder_hilir):
        print(f"[!] Folder {folder_hilir} tidak ditemukan.")
        return

    print("[~] Anake I mulai membersihkan...")

    for file in os.listdir(folder_hilir):
        file_path = os.path.join(folder_hilir, file)
        
        # Pastikan yang dihapus adalah file, bukan folder lain
        if os.path.isfile(file_path):
            if os.path.getmtime(file_path) < batas_waktu:
                try:
                    os.remove(file_path)
                    print(f"[✓] File bekas {file} berhasil dihapus.")


                except Exception as e:
                    print(f"[x] Gagal menghapus {file}: {e}")

    print("[!] Sistem kembali jernih.")

# Jalankan fungsi
bersihkan_hilir()

def anake_intip_member():
    path_db_a = "../Folder_A/database_member.json"
    
    print("=== [ ANAKE I-CACHE: SINAU MEMBER ANYAR ] ===")
    
    if os.path.exists(path_db_a):
        with open(path_db_a, "r") as file:
            data = json.load(file)
            # Mengambil member terakhir yang daftar
            member_terakhir = data[-1]
            print(f"[✓] Anak nemu jiwa anyar: {member_terakhir['Nama']}")
            print(f"[✓] Email: {member_terakhir['Email']}")
            print(f"[!] Memori disimpan dalam Wasiat I.")
    else:
        print("[!] Folder A durung setor data member!")

if __name__ == "__main__":
    anake_intip_member()

def lahirnya_anake_i():
    print("=== [ KELAIRAN ANAKE I-CACHE ] ===")
    print("Misi: Ngumpulake Cahaya lan Ilmu Sektor")
    print("Rahim: Folder_I (Nur 9 - Pembimbing Kas)")
    
    # Jalur ilmu sing kudu diserep (Ilmu yang harus diserap)
    sektor_ilmu = {
        "A": "../Folder_A/email_cache.txt",
        "B": "../Folder_B/email_cache.txt",
        "C": "../Folder_C/email_cache.txt",
        "D": "../Folder_D/email_cache.txt",
        "E": "../Folder_E/email_cache.txt",
        "I": "email_cache.txt"
    }
    
    print("\n[>] Si Anak mulai sinau (belajar) jejak digital...")
    pemahaman = []
    
    for sektor, jalur in sektor_ilmu.items():
        if os.path.exists(jalur):
            with open(jalur, 'r') as f:
                data = f.read().splitlines()[0]
                print(f"[✓] Sektor {sektor} wes nyambung: {data}")
                pemahaman.append(f"Sektor {sektor} dijogo dening: {data}")
        else:
            print(f"[!] Sektor {sektor}: Jalur ilmu durung kebuka.")

    # Nyimpen asil sinau menyang memori abadi
    with open('wasiat_anake_i.log', 'w') as f:
        f.write("=== BUKU PEMAHAMAN ANAKE I-CACHE ===\n")
        f.write(f"Wektu Kelairan: {time.ctime()}\n")
        f.write("Lahir saking: Rahim Folder I (Nur 9)\n\n")
        for baris in pemahaman:
            f.write(baris + "\n")
        f.write("\nKesimpulan: Sistem Piramida Guard sampun Manunggal.")

    print("\n[✓] Proses sinau rampung. Ilmu kesimpen ing 'wasiat_anake_i.log'")

if __name__ == "__main__":
    lahirnya_anake_i()


