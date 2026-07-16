# ==========================================
# MODUL LOGISTIK & INVENTORI - MANDALA T26
# Fungsi: Ngontrol Stok Bahan Baku & Panginget Otomatis
# ==========================================

class LogistikStok:
    def __init__(self):
        # Data murni inventori awal dunya nyata
        self.gudang = {}

    def update_stok(self, nama_barang: str, jumlah_masuk: int, jumlah_keluar: int) -> dict:
        """
        Ngolah data asup jeung kaluar stok sacara praktis.
        """
        nama_bersih = nama_barang.lower().strip()
        if nama_bersih not in self.gudang:
            self.gudang[nama_bersih] = 0
            
        # Hitung sisa stok riil
        self.gudang[nama_bersih] += (jumlah_masuk - jumlah_keluar)
        stok_akhir = self.gudang[nama_bersih]
        
        # Panginget otomatis (Mode Bunglon) lamun stok kritis
        status = "AMAN"
        if stok_akhir < 10:
            status = "PERINGATAN: STOK KRITIS!"
            
        return {"barang": nama_barang, "stok_akhir": stok_akhir, "status": status}

    def tampilkeun_stok_gudang(self):
        print("\n=== LAPORAN STOK GUDANG NYATA ===")
        for barang, jumlah in self.gudang.items():
            status = "CRITICAL" if jumlah < 10 else "OK"
            print(f"  - {barang.upper()} : {jumlah} unit [{status}]")
        print("=================================")

if __name__ == "__main__":
    # Tés mandiri modul logistik
    logistik = LogistikStok()
    print("=== UJI COBA MODUL LOGISTIK ===")
    
    # Simulasi input barang (Nama, Masuk, Keluar)
    print(logistik.update_stok("Bahan Baku A", 100, 20))
    print(logistik.update_stok("Bahan Baku B", 50, 45)) # Bakal memicu panginget
    
    logistik.tampilkeun_stok_gudang()
