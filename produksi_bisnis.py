# ==========================================
# MODUL PRODUKSI & BISNIS - MANDALA T26
# Fungsi: Ngitung Efisiensi Produksi & Kauntungan Bersih Nyata
# ==========================================

class ManajemenBisnis:
    def __init__(self, nama_usaha: str):
        self.nama_usaha = nama_usaha
        self.catatan_produksi = []

    def tambah_laporan_harian(self, tanggal: str, target: int, terealisasi: int, omset: float, biaya_operasional: float) -> dict:
        """
        Fungsi praktis pikeun ngitung efisiensi produksi jeung untung bersih harian.
        """
        # Ngitung persentase efisiensi produksi dunya nyata
        efisiensi = (terealisasi / target) * 100 if target > 0 else 0
        
        # Ngitung untung bersih (Omset - Biaya)
        untung_bersih = omset - biaya_operasional
        
        laporan = {
            "tanggal": tanggal,
            "efisiensi_produksi": f"{efisiensi:.1f}%",
            "untung_bersih": untung_bersih,
            "status_target": "TERCAPAI" if efisiensi >= 100 else "EVALUASI"
        }
        
        self.catatan_produksi.append(laporan)
        return laporan

    def tampilkeun_ringkesan(self):
        print(f"\n=== RINGKESAN BISNIS: {self.nama_usaha.upper()} ===")
        for lap in self.catatan_produksi:
            print(f"Tanggal: {lap['tanggal']}")
            print(f"  - Efisiensi Produksi : {lap['efisiensi_produksi']} [{lap['status_target']}]")
            print(f"  - Kauntungan Bersih  : Rp {lap['untung_bersih']:,}")
        print("==========================================")

if __name__ == "__main__":
    # Tés fungsionalitas usaha nyata
    bisnis_urang = ManajemenBisnis("Produksi Mandala Kreatif")
    
    print("=== UJI COBA MODUL PRODUKSI & BISNIS ===")
    
    # Asupkeun data produksi harian (Tanggal, Target Unit, Realisasi Unit, Omset, Biaya)
    bisnis_urang.tambah_laporan_harian("2026-07-14", 100, 105, 5000000, 2000000)
    bisnis_urang.tambah_laporan_harian("2026-07-15", 100, 90, 4200000, 2000000)
    
    # Tampilkeun hasil analisa
    bisnis_urang.tampilkeun_ringkesan()
