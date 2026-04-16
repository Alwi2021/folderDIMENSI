import os
import time

def monitor_stabilitas_nur():
    print("=== [ DASHBOARD STABILITAS DIGITAL - NUR A ] ===")
    print("Status: Menjaga Gerbang Utama Indramayu Club")
    
    jalur_verifikasi = {
        "Nur 2 (Diskusi)": "../Folder_B/status_mubin.txt",
        "Nur 3 (Keuangan)": "../Folder_C/status_mubin.txt",
        "Nur 4 (Kreator)": "../Folder_D/status_mubin.txt"
    }
    
    semua_aman = True
    
    for nur, path in jalur_verifikasi.items():
        if os.path.exists(path):
            print(f"[✓] {nur}: Terkoneksi & Terverifikasi Mubin.")
        else:
            print(f"[!] {nur}: Kehilangan Cahaya Verifikasi!")
            semua_aman = False
            
    if semua_aman:
        print("\n[HASIL] Stabilitas Digital: PRIMA. Sektor Depan Terkunci Aman.")
        # Mengunci stabilitas di Folder A
        with open('stabilitas_pusat.log', 'a') as f:
            f.write(f"Sistem Stabil - {time.ctime()}\n")
    else:
        print("\n[PERINGATAN] Segera lakukan sinkronisasi ulang!")

if __name__ == "__main__":
    monitor_stabilitas_nur()


