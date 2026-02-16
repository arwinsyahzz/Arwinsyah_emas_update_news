# Deploy Otomatis ke Render (Panduan Singkat)

1. Buat repository di GitHub dan push seluruh folder project ini.
2. Di Render (https://render.com), buat "Web Service" baru dan hubungkan ke repo GitHub Anda.
   - Pilih branch `main`.
   - Build command: kosongkan (Render akan menggunakan repo), atau `pip install -r requirements.txt`.
   - Start command: `bash start.sh` atau `streamlit run app_emas.py --server.port $PORT --server.address 0.0.0.0 --server.enableCORS false`
3. Di GitHub repo → Settings → Secrets → Actions, tambahkan dua secrets:
   - `RENDER_API_KEY` : API Key dari Render (Account → API Keys)
   - `RENDER_SERVICE_ID` : Service ID dari Web Service yang Anda buat di Render
4. Setelah secrets terpasang, setiap push ke `main` akan memicu workflow `.github/workflows/deploy_render.yml` yang membuat deploy baru di Render.

Catatan penting:
- File `riwayat_emas.db` dan file `.db` lainnya dimasukkan ke `.gitignore`. Untuk data persisten gunakan Render PostgreSQL atau layanan eksternal.
- Jika ingin deploy ke Streamlit Community Cloud: hubungkan repo di https://share.streamlit.io lalu pilih `app_emas.py` sebagai entrypoint.
