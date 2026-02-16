from datetime import datetime
import pytz

class OperasiSchedule:
    def __init__(self):
        self.hari_tutup = [5, 6]  # 5=Jumat, 6=Sabtu (dalam ISO: 0=Senin, 6=Minggu)
        # Sesuaikan dengan kebutuhan - jika mau Sabtu & Minggu tutup
        self.hari_tutup = [5, 6]  # Sabtu (5) dan Minggu (6)
        self.jam_buka = 0  # 00:00 Senin
        
    def is_operasional(self):
        """Cek apakah aplikasi beroperasi saat ini"""
        tz = pytz.timezone('Asia/Jakarta')
        now = datetime.now(tz)
        
        # Cek hari (0=Senin, 6=Minggu)
        hari_sekarang = now.weekday()  # Monday=0, Sunday=6
        
        # Jika hari Sabtu (4) atau Minggu (5) dalam format standard Python weekday
        # Sesuaikan dengan timezone Indonesia
        # Sabtu = hari ke-5 (0-indexed), Minggu = hari ke-6 (0-indexed)
        
        if hari_sekarang >= 5:  # Sabtu (5) dan Minggu (6)
            return False, f"Website TUTUP - Hari Libur. Buka lagi Senin jam 00:00 WIB"
        
        return True, "Website OPERASIONAL"
    
    def get_status_operasi(self):
        """Ambil status operasi detail"""
        is_open, pesan = self.is_operasional()
        tz = pytz.timezone('Asia/Jakarta')
        now = datetime.now(tz)
        
        return {
            "is_open": is_open,
            "pesan": pesan,
            "waktu_sekarang": now.strftime("%Y-%m-%d %H:%M:%S WIB"),
            "hari": now.strftime("%A"),
            "jam": now.strftime("%H:%M")
        }
    
    def get_waktu_buka_berikutnya(self):
        """Hitung waktu buka berikutnya"""
        tz = pytz.timezone('Asia/Jakarta')
        now = datetime.now(tz)
        
        hari_sekarang = now.weekday()
        
        # Jika hari Senin-Jumat & < jam 00:00, buka hari ini jam 00:00
        if hari_sekarang < 5:  # Senin-Jumat
            waktu_buka = now.replace(hour=0, minute=0, second=0, microsecond=0)
            if waktu_buka <= now:
                # Website sdh buka hari ini, buka bsk
                if hari_sekarang == 4:  # Jumat, buka Senin
                    hari_buka = (now.day + 3)
                    # Perlu handle bulan/tahun juga
                else:
                    hari_buka = now.day + 1
            return waktu_buka
        else:  # Sabtu atau Minggu
            # Mau buka Senin jam 00:00
            hari_ke_senin = (7 - hari_sekarang)
            from datetime import timedelta
            waktu_buka = now + timedelta(days=hari_ke_senin)
            waktu_buka = waktu_buka.replace(hour=0, minute=0, second=0, microsecond=0)
            return waktu_buka
