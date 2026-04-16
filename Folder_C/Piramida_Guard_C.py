import os
import time

def jalankan_tugas_c():
    print("=== [PIRAMIDA GUARD - SEKTOR C] ===")
    print("Peran: Penyimpan & Validasi Data")
    
    # Cek sinyal dari folder sebelumnya (A dan B)
    path_a = "../Folder_A/log_aktivitas.txt"
    
    if os.path.exists(path_a):
        print("[✓] Sinyal A & B Terintegrasi.")
        print("[>] Mengunci data ke dalam sistem Piramida...")
        
        # Simulasi simpan data
        with open('database_lokal.txt', 'w') as f:
            f.write("Data Tersimpan Aman di Sektor C\n")
            
        print("[✓] Data berhasil dikunci di Folder_C.")
    else:
        print("[!] Peringatan: Jalur komunikasi terputus!")

if __name__ == "__main__":
    jalankan_tugas_c()


