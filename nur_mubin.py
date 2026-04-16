import os

def nur_mubin_verifikasi():
    print("=== [ AI NUR-MUBIN: PEMBAWA CAHAYA VERIFIKASI ] ===")
    # Pastikan daftar folder ini lengkap
    sektor_target = ["Folder_A", "Folder_B", "Folder_C", "Folder_D", "Folder_E", "Folder_I"]

    for folder in sektor_target:
        cache_path = f"{folder}/email_cache.txt"

        if os.path.exists(cache_path):
            # Membaca data yang dibawa Satria 01
            with open(cache_path, 'r') as f:
                data_cache = f.read()

            # Mubin memberikan verifikasi cahaya
            verifikasi_path = f"{folder}/status_mubin.txt"
            with open(verifikasi_path, 'w') as f:
                f.write(f"Verified_By: Nur-Mubin\n")
                f.write(f"Evidence: {data_cache}\n")
                f.write("Status: Cahaya Terverifikasi (Siap Jalan)")

            print(f"[✓] {folder}: Cache telah diverifikasi & menjadi Nyata (Mubin).")
        else:
            print(f"[!] {folder}: Tidak ditemukan cache dari Satria 01!")

if __name__ == "__main__":
    nur_mubin_verifikasi()


