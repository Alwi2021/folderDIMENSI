# Folder_A/tugas_A.py
import os

def urai_data_lokal():
    print("=== [Piramida Guard - Jalur Folder A] ===")
    # Misi: Mencari file teks lokal untuk diurai
    if not os.path.exists('data_sumber.txt'):
        with open('data_sumber.txt', 'w') as f:
            f.write("Data Indramayu Club - Folder A\n")
            f.write("Status: Sinkronisasi Offline")
        print("[!] File data_sumber.txt baru saja dibuat.")
    
    with open('data_sumber.txt', 'r') as f:
        isi = f.read()
        print(f"[✓] Berhasil Mengurai:\n{isi}")

if __name__ == "__main__":
    urai_data_lokal()


