# 💰 Gold Tracker PRO - Dashboard Emas 24 Jam

Aplikasi komprehensif untuk monitoring dan trading emas dengan fitur canggih dan tampilan futuristik.

## 🎯 Fitur Utama

### 1. **📊 Dashboard Real-Time**
- Harga emas terkini dengan update otomatis
- Grafik interaktif dengan teknologi Plotly
- Statistik harga (tertinggi, terendah, rata-rata)
- Perubahan harga realtime dengan indikator warna

### 2. **📰 Berita & Analisis Emas**
- Feed berita terkini tentang emas
- Kategori: Geopolitik, Suku Bunga, Ekonomi, Pasar, Nilai Tukar
- Analisis dampak berita terhadap harga
- Form untuk menambah berita custom

### 3. **🔔 Price Alert - Price Target**
- Notifikasi otomatis saat harga mencapai target BELI
- Notifikasi otomatis saat harga mencapai target JUAL
- Manajemen multiple alerts per pengguna
- Database tersimpan di price_alerts.db

### 4. **📅 Jadwal Operasional Otomatis**
- **Senin-Jumat**: Website buka 24 jam
- **Sabtu-Minggu**: Website TUTUP untuk maintenance
- **Pembukaan Kembali**: Senin pukul 00:00 WIB
- Status real-time di dashboard

### 5. **📈 Chart Trading 24 Jam**
- Grafik pergerakan harga dalam 24 jam
- Interactive zoom & pan
- Hover untuk detail harga
- Support riwayat data hingga 100 entry

### 6. **🎨 Tampilan Futuristik**
- Tema dark dengan aksen emas
- Font modern "Orbitron" untuk header
- Animasi pulse pada status indicator
- Card design dengan shadow effect
- Gradient backgrounds

### 7. **📥 Export & Download**
- Download data ke format CSV
- Download data ke format Excel
- Ringkasan statistik lengkap

## 📋 File Struktur

```
update_harga emas/
├── app_emas.py              # Main Streamlit app (WEBSITE)
├── emas.py                  # Desktop app untuk update harga (BACKEND)
├── news_berita.py           # Module untuk berita emas
├── price_alert.py           # Module untuk price alert/notifikasi
├── operasi_schedule.py      # Module untuk jadwal operasional
├── requirements.txt         # Dependensi Python
├── riwayat_emas.db         # Database harga emas (auto-created)
├── price_alerts.db         # Database alerts (auto-created)
└── README.md               # File ini
```

## 🚀 Cara Instalasi & Menjalankan

### 1. **Instalasi Dependencies**

```bash
pip install -r requirements.txt
```

Jika ada error openpyxl:
```bash
pip install openpyxl
```

### 2. **Jalankan Desktop App (Backend)**

Terminal pertama - untuk update harga otomatis:
```bash
python emas.py
```

Aplikasi ini akan:
- Mengambil harga emas dari internet secara otomatis
- Menyimpan ke database `riwayat_emas.db`
- Update setiap interval tertentu

### 3. **Jalankan Website (Frontend)**

Terminal kedua - untuk dashboard web:
```bash
streamlit run app_emas.py
```

Website akan terbuka di: **http://localhost:8501**

> 💡 **Akses dari HP/Device Lain:**
> - Pastikan PC dan device terhubung WiFi yang sama
> - Buka: `http://[IP-PC]:8501`
> - Cari IP PC dengan: `ipconfig` (Windows) atau `ifconfig` (Linux/Mac)

## 📱 Menu & Navigasi

### Tab 1: 📊 Dashboard
- Harga terkini
- Grafik pergerakan 24 jam
- Statistik lengkap
- Tabel data terakhir

### Tab 2: 📰 Berita & Analisis
- News feed emas
- Filter berdasarkan kategori
- Analisis dampak bullish/bearish
- Form tambah berita custom

### Tab 3: 🔔 Price Alert
- Buat alert beli & jual
- Monitoring aktif alerts
- Alert trigger notification
- Support multiple users

### Tab 4: 📥 Download
- Export data ke CSV
- Export data ke Excel
- Statistik ringkas

### Tab 5: ⚙️ Pengaturan
- Status operasional
- Interval refresh
- Info sistem
- Tips & panduan

## 🔔 Cara Menggunakan Price Alert

### Membuat Alert Baru:

1. Buka Tab **🔔 Price Alert**
2. Isi nama Anda
3. Set harga target untuk **BELI** (biasanya lebih rendah)
4. Set harga target untuk **JUAL** (biasanya lebih tinggi)
5. Klik "🔔 Buat Alert"

### Contoh Setup:

| Skenario | Harga Beli | Harga Jual |
|----------|-----------|-----------|
| **Conservative** | 650,000 | 750,000 |
| **Moderate** | 680,000 | 720,000 |
| **Aggressive** | 700,000 | 710,000 |

> ⚠️ Harga akan di-cek otomatis ketika sistem running

## 📊 Cara Menambah Berita

1. Buka Tab **📰 Berita & Analisis**
2. Scroll ke bagian "➕ Tambah Berita Baru"
3. Isi judul berita
4. Pilih kategori (atau buat kategori baru)
5. Isi deskripsi
6. Pilih dampak: Positif / Negatif / Netral
7. Klik "📤 Tambahkan Berita"

## 📅 Jadwal Operasional

```
SENIN-JUMAT:
✅ OPERASIONAL 24 JAM

SABTU-MINGGU:
🔴 TUTUP untuk Maintenance
↓
Dibuka Ulang Senin 00:00 WIB
```

## 📊 Database

### riwayat_emas.db
Menyimpan:
- `id` - ID unik
- `waktu` - Timestamp harga
- `harga` - Harga emas (Rupiah)

### price_alerts.db
Menyimpan:
- `id` - Alert ID unik
- `nama_pengguna` - Nama user
- `harga_beli` - Target harga beli
- `harga_jual` - Target harga jual
- `status` - Aktif/Nonaktif
- `tanggal_buat` - Kapan alert dibuat

## ⚙️ Konfigurasi Lanjutan

### Ubah Jadwal Libur
Edit file `operasi_schedule.py`:
```python
self.hari_tutup = [5, 6]  # 5=Sabtu, 6=Minggu dalam format ISO
```

### Ubah Sumber Harga Emas
Edit file `emas.py`:
```python
url = "https://www.hargaemas.com/"  # Ubah ke sumber lain
```

### Ubah Interval Update
Edit `app_emas.py`:
```python
@st.cache_data(ttl=300)  # ttl dalam detik (300 = 5 menit)
```

## 🐛 Troubleshooting

### "Database Kosong"
**Solusi:** Jalankan `emas.py` terlebih dahulu untuk populate data dari internet

### "Error ambil harga"
**Solusi:** Cek koneksi internet dan pastikan website sumber tidak berubah

### "Error Plotly Graph"
**Solusi:** Update plotly `pip install --upgrade plotly`

### "Can't access dari HP"
**Solusi:** 
1. Jalankan server dengan: `streamlit run app_emas.py --server.address 0.0.0.0`
2. Cek IP dengan `ipconfig` (cari IPv4 Address)
3. Buka di HP: `http://[IP]:8501`

## 📈 Tips Trading Emas

1. **Monitor Berita** - Geopolitik & suku bunga mempengaruhi harga
2. **Set Alert** - Jangan menunggu, biarkan sistem notif Anda
3. **Analisa Trend** - Lihat grafik 24 jam untuk pola
4. **Diversifikasi** - Jangan set alert terlalu rapat
5. **Update Rutin** - Cek dashboard minimal 1x sehari

## 🎨 Kustomisasi CSS

Edit bagian CSS di `app_emas.py` untuk mengubah warna & tema:
```python
# Ubah warna emas yang ada
#FFD700  -> Warna utama
#00d084  -> Warna positif (hijau)
#ff6b6b  -> Warna negatif (merah)
```

## 📞 Support & Development

- **Issue database?** Hapus file .db dan jalankan ulang
- **Perlu fitur tambahan?** Edit modul sesuai kebutuhan
- **Ingin integrasi API?** Tambahkan request ke API emas

## 📄 Lisensi

Aplikasi ini dibuat untuk keperluan personal dan komersial.
Free to use dan modify sesuai kebutuhan.

---

**Happy Trading! 💰📈**

*Last Updated: 2026-02-08*
*Version: 2.0 Pro Edition*
