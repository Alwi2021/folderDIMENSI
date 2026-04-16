import os
import time

def jalankan_tugas_d():
    print("=== [PIRAMIDA GUARD - SEKTOR D] ===")
    print("Peran: Distributor & Jalur Komunikasi")
    
    path_c = "../Folder_C/database_lokal.txt"
    
    if os.path.exists(path_c):
        print("[✓] Database Sektor C Terdeteksi.")
        with open('sinyal_distribusi.txt', 'w') as f:
            f.write("Jalur Komunikasi Terbuka - Sektor D Aktif")
        print("[✓] Jalur komunikasi siap digunakan.")
    else:
        print("[!] Peringatan: Data dari Sektor C belum diterima!")

if __name__ == "__main__":
    # Pastikan nama di bawah ini SAMA PERSIS dengan nama def di atas
    jalankan_tugas_d()





