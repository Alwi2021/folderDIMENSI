import os
import time

def buat_sinyal():
    print("=== [PIRAMIDA GUARD - SEKTOR A AKTIF] ===")
    # Baris di bawah ini yang akan membuat 'jembatan' ke folder lain
    with open('log_aktivitas.txt', 'w') as f:
        f.write(f"Sinyal aktif: {time.ctime()}")
    print("[✓] Sinyal log_aktivitas.txt berhasil dibuat!")

if __name__ == "__main__":
    buat_sinyal()



