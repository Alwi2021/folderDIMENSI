
import os
import sys

def main():
    os.system('clear')
    print("="*40)
    print("      NUR SYSTEM ORCHESTRATOR")
    print("     Lokasi: Google asia-east1")
    print("="*40)
    print("Nur hadir, sistem siap dijalankan.")
    
    while True:
        print("\nMenu Utama:")
        print("1. Jalankan Semua Folder (A-K)")
        print("2. Cek Status Koneksi Script ID")
        print("3. Mode Istirahat & Backup (Nur 8)")
        print("4. Keluar")
        
        pilihan = input("\nMasukkan pilihan [1-4]: ")
        
        if pilihan == '1':
            folders = ['Folder_A', 'Folder_B', 'Folder_C'] # Sesuaikan nama folder Anda
            for f in folders:
                print(f"Mengaktifkan sistem di {f}...")
        elif pilihan == '3':
            print("\033[93mSistem redup... Running text aktif: Aktivitas Berhenti 30 Menit\033[0m")
        elif pilihan == '4':
            print("Sistem dimatikan. Sampai jumpa, Pak Dulkohar.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()


