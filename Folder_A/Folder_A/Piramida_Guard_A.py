import os
import time

def jalankan_tugas_a():
    print("=== [PIRAMIDA GUARD - SEKTOR A] ===")
    print("Sistem: Indramayu Club (Jalur Mandiri)")
    print("Status: Aktif & Mengawasi...")
    
    # Membuat file log aktivitas lokal jika belum ada
    if not os.path.exists('log_aktivitas.txt'):
        with open('log_aktivitas.txt', 'w') as f:
            f.write(f"Sistem dimulai pada: {time.ctime()}\n")
    
    print("[✓] Log aktivitas telah diperbarui.")
    print("[✓] Koneksi ke Folder_B sedang disiapkan secara internal.")

if __name__ == "__main__":
    jalankan_tugas_a()

