import os
import time

def jalankan_tugas_b():
    print("=== [PIRAMIDA GUARD - SEKTOR B] ===")
    print("Peran: Nur 2 - Pusat Diskusi & Olah Data")
    
    # Mengecek apakah Folder_A sudah mengirimkan sinyal aktif
    path_log_a = "../Folder_A/log_aktivitas.txt"
    
    if os.path.exists(path_log_a):
        print("[✓] Sinyal dari Folder_A terdeteksi.")
        print("[>] Mengolah data untuk persiapan Folder_C...")
        time.sleep(1)
        print("[✓] Sinkronisasi Folder_B Selesai.")
    else:
        print("[!] Peringatan: Folder_A belum mengirimkan sinyal.")

if __name__ == "__main__":
    jalankan_tugas_b()

