@echo off
REM ============================================
REM SETUP SCRIPT - Gold Tracker PRO
REM Platform: Windows
REM ============================================

echo.
echo ============================================
echo   GOLD TRACKER PRO - SETUP SCRIPT
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python tidak terinstall!
    echo Silahkan install Python dari https://www.python.org/
    pause
    exit /b 1
)

echo [OK] Python terdeteksi

REM Create virtual environment (optional)
REM echo [STEP 1] Membuat virtual environment...
REM python -m venv venv
REM call venv\Scripts\activate.bat

REM Install requirements
echo.
echo [STEP 1] Menginstall dependensi...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Gagal install dependencies!
    pause
    exit /b 1
)

echo [OK] Semua dependensi terinstall

REM Check if databases exist
echo.
echo [STEP 2] Mengecek database...
REM Database akan auto-created saat pertama run

echo [OK] Database setup ready

echo.
echo ============================================
echo   SETUP SELESAI!
echo ============================================
echo.
echo LANGKAH SELANJUTNYA:
echo.
echo 1. Jalankan Desktop App (untuk ambil harga):
echo    python emas.py
echo.
echo 2. Di terminal lain, jalankan Website:
echo    streamlit run app_emas.py
echo.
echo 3. Buka browser: http://localhost:8501
echo.
echo Untuk akses dari device lain di WiFi yang sama:
echo   - Cari IP komputer: ipconfig (cari IPv4)
echo   - Buka: http://[IP]:8501
echo.
pause
