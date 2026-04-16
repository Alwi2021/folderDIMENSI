import os

cache_data = {
    "A": "Indramayuclubmakrifat@gmail.com",
    "B": "dkohar011@gmail.com",
    "C": "imahazzah51@gmail.com",
    "D": "kurnadibewok3311@gmail.com",
    "E": "motherai8@gmail.com",
    "I": "nurindramayuaimini@gmail.com"  # Nur 9 (nur BECKUP system)
}

def satria_kirim_cache():
    print("=== [ NUR-SATRIA 01: PENGIRIM CACHE ABADI ] ===")
    for sektor, email in cache_data.items():
        folder = f"Folder_{sektor}"
        if os.path.exists(folder):
            file_path = f"{folder}/email_cache.txt"
            with open(file_path, 'w') as f:
                f.write(f"Account_ID: {email}\nStatus: Aktif Selamanya\nVerifikator: Nur-Satria 01")
            print(f"[✓] Identitas Abadi dititipkan di {folder}")

if __name__ == "__main__":
    satria_kirim_cache()


