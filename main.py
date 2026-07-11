from core.material import Element
from core.discovery import CombinationEngine
from core.analyzer import MaterialAnalyzer
from core.reporter import DiscoveryReporter  # Yeni modülü içe aktarıyoruz

def main():
    print("==========================================================")
    print(" PHOENIX DISCOVERY - 1. AŞAMA: GENİŞLETİLMİŞ MALZEME UZAYI ")
    print("==========================================================\n")

    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    li = Element("Lityum", "Li", 6.94, 534.0, 3582.0, 1.1e7)
    sn = Element("Kalay", "Sn", 118.71, 7310.0, 228.0, 0.9e7)
    
    element_pool = [al, mg, li, sn]
    pool_symbols = [el.symbol for el in element_pool]
    
    generated_alloys = CombinationEngine.generate_alloys(element_pool, step=0.1)

    analyzed_alloys = []
    for alloy in generated_alloys:
        report = MaterialAnalyzer.analyze_alloy(alloy)
        analyzed_alloys.append(report)

    analyzed_alloys.sort(key=lambda x: x["Üretilebilirlik Uygunluk Skoru (0-100)"], reverse=True)

    # Önce terminale yazdırıyoruz
    print("🏆 --- ÜRETİLEBİLİRLİK VE MALİYET SÜZGECİNDEN GEÇEN TOP 5 ŞAMPİYON ---")
    for index, res in enumerate(analyzed_alloys[:5], 1):
        print(f"{index}. {res['Alaşım Adı']}")
        print(f"   💰 Maliyet: {res['Hesaplanan Maliyet ($/kg)']} $/kg | ⚠️ Tedarik Riski: {res['Ağırlıklı Tedarik Riski (1-10)']}/10")
        print(f"   🎯 UYGUNLUK SKORU: {res['Üretilebilirlik Uygunluk Skoru (0-100)']}/100\n")

    # --- ŞİMDİ DİSKE PROFESYONEL RAPORU YAZIYORUZ ---
    print("📂 Raporlama motoru devreye giriyor...")
    report_path = DiscoveryReporter.generate_markdown_report(analyzed_alloys, pool_symbols)
    print(f"💾 Başarılı! 1. Aşama Keşif Raporu '{report_path}' olarak diske mühürlendi.\n")

    print("==========================================================")
    print(" 1. AŞAMA BAŞARIYLA TAMAMLANDI: ELENEN VE KAZANANLAR HAZIR ")
    print("==========================================================")

if __name__ == "__main__":
    main()