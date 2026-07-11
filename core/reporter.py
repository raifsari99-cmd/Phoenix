"""
PHOENIX 19 - Raporlama Motoru (Gelişmiş Versiyon)
Keşif ve geometrik tasarım süreçlerinin sonuçlarını profesyonel dokümantasyon formatında kaydeder.
"""

import os
from datetime import datetime

class DiscoveryReporter:
    """Sonuçları analiz ederek docs/ klasörü altında şık raporlar üretir."""

    @staticmethod
    def generate_markdown_report(analyzed_alloys: list, pool_symbols: list) -> str:
        os.makedirs("docs", exist_ok=True)
        filename = "docs/PHOENIX_DISCOVERY_REPORT_STAGE_1.md"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 🔬 PHOENIX DISCOVERY - 1. AŞAMA KEŞİF RAPORU\n\n")
            f.write(f"**Rapor Tarihi:** {current_time}  \n")
            f.write(f"**Analiz Edilen Element Havuzu:** {', '.join(pool_symbols)}  \n")
            f.write(f"**Toplam Taranan Varyasyon Sayısı:** {len(analyzed_alloys)}\n\n")
            f.write("---\n\n")
            f.write("## 🏆 TOP 5 ŞAMPİYON FORMÜL\n\n")
            f.write("| Sıra | Alaşım Adı | Maliyet ($/kg) | Tedarik Riski (1-10) | UYGUNLUK SKORU |\n")
            f.write("| :--- | :--- | :---: | :---: | :---: |\n")
            for index, res in enumerate(analyzed_alloys[:5], 1):
                f.write(f"| {index} | **{res['Alaşım Adı']}** | {res['Hesaplanan Maliyet ($/kg)']} | {res['Ağırlıklı Tedarik Riski (1-10)']} | **{res['Üretilebilirlik Uygunluk Skoru (0-100)']}/100** |\n")
        return filename

    @staticmethod
    def generate_geometry_report(hull_name: str, alloy_name: str, density: float, inner_dim: str, envelope: dict) -> str:
        """Sohbet 07 kapsamında fiziksel muhafaza ve mekanik zarf raporunu üretir."""
        os.makedirs("docs", exist_ok=True)
        filename = "docs/PHOENIX_GEOMETRIC_HULL_REPORT.md"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 🛡️ PHOENIX GEOMETRIC HULL DESIGN REPORT (SOHBET 07)\n\n")
            f.write(f"**Rapor Tarihi:** {current_time}  \n")
            f.write(f"**Mekanik Tasarım Standardı:** FEA (Sonlu Elemanlar Analizi) Ön Girdisi  \n\n")
            f.write("---\n\n")
            
            f.write("## 🔩 1. MALZEME VE FİZİKSEL ÖZELLİKLER\n")
            f.write(f"* **Seçilen Şasi Alaşımı:** {alloy_name}\n")
            f.write(f"* **Hesaplanan Alaşım Yoğunluğu:** {round(density, 2)} kg/m³\n")
            f.write(f"* **Zırh Tipi / Muhafaza Adı:** {hull_name}\n\n")
            
            f.write("---\n\n")
            f.write("## 📐 2. GEOMETRİK MEKANİK ZARF VE HACİM VERİLERİ\n\n")
            f.write("| Parametre | Simülasyon Çıktısı |\n")
            f.write("| :--- | :--- |\n")
            f.write(f"| **İç Hücre Çekirdek Boyutları** | {inner_dim} mm |\n")
            f.write(f"| **Hesaplanan Dış Ölçüler** | {envelope['Dış Boyutlar (G x Y x D mm)']} mm |\n")
            f.write(f"| **Toplam Dış Hacim** | {envelope['Toplam Dış Hacim (Litre)']} Litre |\n")
            f.write(f"| **Sadece Koruyucu Gövde Ağırlığı** | {envelope['Koruyucu Gövde Ağırlığı (kg)']} kg |\n")
            f.write(f"| **Hacimsel Paketleme Verimliliği** | **%{envelope['Hacimsel Paketleme Verimliliği (%)']}** |\n\n")
            
            f.write("---\n\n")
            f.write("## 💡 3. MÜHENDİSLİK DEĞERLENDİRME NOTU\n")
            f.write(f"> PHOENIX-Gen1 hücresi için tasarlanan **{hull_name}** dış muhafazası, metalurjik hafiflik avantajı ")
            f.write(f"sayesinde **{envelope['Koruyucu Gövde Ağırlığı (kg)']} kg** gibi son derece optimize bir ek yük ile hücreyi sarmalamıştır. ")
            f.write(f"**%{envelope['Hacimsel Paketleme Verimliliği (%)']}** seviyesindeki paketleme verimliliği, modüler şasi yerleşimi ")
            f.write("ve CARLA simülasyon ortamındaki araç ağırlık dağılımı testleri için mükemmel bir geometrik taban sunmaktadır.\n")
            
        return filename