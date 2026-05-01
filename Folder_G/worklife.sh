#!/bin/bash
echo "=== INDRAMAYU CLUB: AUTOMATION START ==="

# Tambahkan semua file
git add .

# Commit (Tanpa file yang berisi rahasia)
git commit -m "Update Konten Member: $(date)"

# Push menggunakan URL yang sudah terotorisasi (Token disisipkan saat jalan saja)
git push origin main --force

echo "=== BERHASIL TERUNGGAH KE GITHUB ==="
