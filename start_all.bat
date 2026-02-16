REM ============================================
REM START SCRIPT - Gold Tracker PRO
REM Jalankan kedua app sekaligus
REM ============================================

@echo off
echo.
echo ============================================
echo   GOLD TRACKER PRO - STARTING...
echo ============================================
echo.

REM Start desktop app di window baru
echo [1/2] Memulai Desktop App (emas.py)...
start "Desktop App - Gold Tracker" python emas.py

REM Wait 3 seconds
timeout /t 3 /nobreak

REM Start web app
echo [2/2] Memulai Website (app_emas.py)...
streamlit run app_emas.py

echo.
echo ============================================
echo   APLIKASI DIJALANKAN
echo ============================================
echo.
echo Akses website: http://localhost:8501
echo.
pause
