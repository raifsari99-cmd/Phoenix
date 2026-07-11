from core.material import Element, Alloy
from core.discovery import CombinationEngine
from core.analyzer import MaterialAnalyzer
from core.reporter import DiscoveryReporter
from core.battery import BatteryComponent, BatteryCell  # 2. Aşama modülleri

def main():
    print("==========================================================")
    print("                PHOENIX FULL PIPELINE ENGINE              ")
    print("==========================================================\n")

    # --- 1. AŞAMA: MALZEME KEŞİF UZAYI ---
    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    li = Element("Lityum", "Li", 6.94, 534.0, 3582.0, 1.1e7)
    sn = Element("Kalay", "Sn", 118.71, 7310.0, 228.0, 0.9e7)
    
    element_pool = [al, mg, li, sn]
    generated_alloys = CombinationEngine.generate_alloys(element_pool, step=0.1)

    analyzed_alloys = []
    for alloy in generated_alloys:
        report = MaterialAnalyzer.analyze_alloy(alloy)
        analyzed_alloys.append(report)

    analyzed_alloys.sort(key=lambda x: x["Üretilebilirlik Uygunluk Skoru (0-100)"], reverse=True)

    # Raporu diske mühürle
    DiscoveryReporter.generate_markdown_report(analyzed_alloys, [el.symbol for el in element_pool])

    # --- 2. AŞAMA: BATARYA UYGULAMA UZAYI (TEST SENARYOLARI) ---
    print("🔋 --- 2. AŞAMA: ELEKTROKİMYASAL VE GEOMETRİK HÜCRE TESTLERİ ---")
    
    # Şampiyon 1. Alaşımı Al-Mg olarak seçiyoruz ve Anot yapmayı deniyoruz
    top_alloy_data = analyzed_alloys[0]
    # Gerçek nesnesini bulalım
    top_alloy = next(a for a in generated_alloys if a.name == top_alloy_data["Alaşım Adı"])
    
    anode_comp = BatteryComponent(name="Phoenix Gelişmiş Anot", material=top_alloy, role="Anode")
    
    # Hatalı bir senaryo denemek için saf Alüminyumu Katot yapmayı deniyoruz
    cathode_comp = BatteryComponent(name="Deneysel Saf Katot", material=al, role="Cathode")

    # 100 cm3'lük (0.0001 m3) bir deneysel hücre hücresi kuruyoruz
    cell = BatteryCell(name="Phoenix-X1 Hücresi", anode=anode_comp, cathode=cathode_comp, volume_m3=0.0001)
    
    # Hücre simülasyonunu ve güvenlik/uyum testini çalıştır
    cell_report = cell.run_safety_and_geometry_check()
    
    print(f"\n🔬 Hücre Test Merkezi Raporu:")
    print(f"   📦 Tasarım Adı: {cell_report['Hücre Adı']}")
    print(f"   ⚖️ Tahmini Hücre Ağırlığı: {cell_report['Teorik Hücre Kütlesi (kg)']} kg")
    print(f"   🚨 Genel Durum: {cell_report['Hücre Güvenlik/Uyum Onayı']}")
    print(f"   🪫 Anot Değerlendirmesi: {cell_report['Anot Durumu']}")
    print(f"   🔋 Katot Değerlendirmesi: {cell_report['Katot Durumu']}\n")

    print("==========================================================")
    print("       TÜM SÜREÇ BAŞARIYLA SİMÜLE EDİLDİ VE BİTTİ         ")
    print("==========================================================")

if __name__ == "__main__":
    main()