"""
PHOENIX 19 - Raporlama Motoru
Keşif süreçlerinin sonuçlarını profesyonel dokümantasyon formatında diske kaydeder.
"""

import os
from datetime import datetime

class DiscoveryReporter:
    """Malzeme keşif sonuçlarını Markdown tabanlı rapor dosyalarına dönüştüren sınıf."""

    @staticmethod
    def generate_markdown_report(analyzed_alloys: list, pool_symbols: list) -> str:
        """Sonuçları analiz ederek docs/ klasörü altında şık bir rapor üretir."""
        
        # docs klasörünün varlığından emin olalım
        os.makedirs("docs", exist_ok=True)
        
        filename = "docs/PHOENIX_DISCOVERY_REPORT_STAGE_1.md"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 🔬 PHOENIX DISCOVERY - 1. AŞAMA KEŞİF RAPORU\n\n")
            f.write(f"**Rapor Tarihi:** {current_time}  \n")
            f.write(f"**Analiz Edilen Element Havuzu:** {', '.join(pool_symbols)}  \n")
            f.write(f"**Toplam Taranan Varyasyon / Kombinasyon Sayısı:** {len(analyzed_alloys)}\n\n")
            f.write("---\n\n")
            
            f.write("## 🎯 Proje Sahibi Mühendislik Vizyonu Manifestosu\n")
            f.write("> **Stratejik Yaklaşım:** Ele alınan elementler doğrudan batarya hücresine aktarılmadan önce, ")
            f.write("metalurjik, lojistik ve ticari (maliyet/bulunabilirlik) süzgeçlerden geçirilmiştir. ")
            f.write("Bu ön süzgeç, sürdürülebilir üretim ve tasarım optimizasyonu için temel teşkil eder.\n\n")
            
            f.write("---\n\n")
            f.write("## 🏆 Üretilebilirlik ve Maliyet Açısından TOP 5 ŞAMPİYON FORMÜL\n\n")
            f.write("| Sıra | Alaşım / Karışım Adı | Maliyet ($/kg) | Tedarik Riski (1-10) | UYGUNLUK SKORU |\n")
            f.write("| :--- | :--- | :---: | :---: | :---: |\n")
            
            for index, res in enumerate(analyzed_alloys[:5], 1):
                f.write(f"| {index} | **{res['Alaşım Adı']}** | {res['Hesaplanan Maliyet ($/kg)']} | {res['Ağırlıklı Tedarik Riski (1-10)']} | **{res['Üretilebilirlik Uygunluk Skoru (0-100)']}/100** |\n")
                
            f.write("\n\n---\n\n")
            f.write("## 💡 Karar Motoru Stratejik Analiz Notu\n")
            top_1 = analyzed_alloys[0]['Alaşım Adı']
            f.write(f"Sistem simülasyonu sonucunda, lojistik risk bariyerleri ve maliyet parametreleri dikkate alındığında ")
            f.write(f"**{top_1}** kombinasyonu en yüksek sürdürülebilirlik puanını toplayarak liderliği almıştır. ")
            f.write("Bu aşamadan başarıyla geçen alaşımlar, **2. Aşama: Batarya Uygulama Uzayı** simülasyonlarına (Anot/Katot kimyasal kararlılık testleri) aktarılmaya hazırdır.\n")
            
        return filename