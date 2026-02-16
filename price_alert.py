import sqlite3
from datetime import datetime
import json

class PriceAlert:
    def __init__(self, db_name="price_alerts.db"):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Inisialisasi database untuk alert"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_pengguna TEXT,
                harga_beli INTEGER,
                harga_jual INTEGER,
                status TEXT,
                tanggal_buat TEXT,
                notifikasi_terkirim INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()
    
    def tambah_alert(self, nama_pengguna, harga_beli, harga_jual):
        """Tambah alert baru"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        waktu_skrg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO alerts (nama_pengguna, harga_beli, harga_jual, status, tanggal_buat)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_pengguna, harga_beli, harga_jual, "Aktif", waktu_skrg))
        
        conn.commit()
        alert_id = cursor.lastrowid
        conn.close()
        return alert_id
    
    def get_semua_alerts(self):
        """Ambil semua alert"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alerts WHERE status = "Aktif"')
        alerts = cursor.fetchall()
        conn.close()
        return alerts
    
    def get_alerts_by_pengguna(self, nama_pengguna):
        """Ambil alert berdasarkan pengguna"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alerts WHERE nama_pengguna = ? AND status = "Aktif"', (nama_pengguna,))
        alerts = cursor.fetchall()
        conn.close()
        return alerts
    
    def hapus_alert(self, alert_id):
        """Hapus alert"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('UPDATE alerts SET status = "Nonaktif" WHERE id = ?', (alert_id,))
        conn.commit()
        conn.close()
    
    def check_alert(self, harga_saat_ini):
        """Cek apakah ada alert yang terpicu"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nama_pengguna, harga_beli, harga_jual FROM alerts 
            WHERE status = "Aktif"
        ''')
        alerts = cursor.fetchall()
        conn.close()
        
        triggered = []
        for alert in alerts:
            alert_id, nama, beli, jual = alert
            if harga_saat_ini <= beli:
                triggered.append({
                    "id": alert_id,
                    "pengguna": nama,
                    "tipe": "BELI",
                    "harga": beli,
                    "pesan": f"Harga emas mencapai Rp {beli:,} - Waktu yang tepat untuk BELI!"
                })
            elif harga_saat_ini >= jual:
                triggered.append({
                    "id": alert_id,
                    "pengguna": nama,
                    "tipe": "JUAL",
                    "harga": jual,
                    "pesan": f"Harga emas mencapai Rp {jual:,} - Waktu yang tepat untuk JUAL!"
                })
        
        return triggered
