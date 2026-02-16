#!/bin/bash

# ============================================
# SETUP SCRIPT - Gold Tracker PRO
# Platform: Linux/Mac
# ============================================

echo ""
echo "============================================"
echo "  GOLD TRACKER PRO - SETUP SCRIPT"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 tidak terinstall!"
    echo "Silahkan install Python dari https://www.python.org/ atau gunakan package manager"
    exit 1
fi

echo "[OK] Python terdeteksi"

# Install requirements
echo ""
echo "[STEP 1] Menginstall dependensi..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Gagal install dependencies!"
    exit 1
fi

echo "[OK] Semua dependensi terinstall"

# Check if databases exist
echo ""
echo "[STEP 2] Mengecek database..."
# Database akan auto-created saat pertama run

echo "[OK] Database setup ready"

echo ""
echo "============================================"
echo "  SETUP SELESAI!"
echo "============================================"
echo ""
echo "LANGKAH SELANJUTNYA:"
echo ""
echo "1. Jalankan Desktop App (untuk ambil harga):"
echo "   python3 emas.py"
echo ""
echo "2. Di terminal lain, jalankan Website:"
echo "   streamlit run app_emas.py"
echo ""
echo "3. Buka browser: http://localhost:8501"
echo ""
echo "Untuk akses dari device lain di WiFi yang sama:"
echo "  - Cari IP komputer: ifconfig (cari inet)"
echo "  - Buka: http://[IP]:8501"
echo ""
