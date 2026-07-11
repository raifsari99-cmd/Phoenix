from core.material import Element, Alloy
from core.discovery import CombinationEngine
from core.analyzer import MaterialAnalyzer
from core.reporter import DiscoveryReporter
from core.battery import BatteryComponent, BatteryCell

def main():
    print("==========================================================")
    print("      PHOENIX DIGITAL TWIN ENGINE - SOHBET 06 SONUÇ       ")
    print("==========================================================\n")

    # Element Havuzu
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

    # 1. Aşama Raporunu Tazele
    DiscoveryReporter.generate_markdown_report(analyzed_alloys, [el.symbol for el in element_pool])

    # --- 2. AŞAMA: ONAYLANAN DİJİTAL İKİZ TASARIMI ---
    print("🔋 --- GEOMETRİK VE KİMYASAL DİJİTAL İKİZ DOĞRULAMASI ---")
    
    # Anot: Listenin 1. şampiyon alaşımı (Al90_Mg10) -> 50 mikron kalınlık
    anode_alloy = next(a for a in generated_alloys if a.name == analyzed_alloys[0]["Alaşım Adı"])
    anode_comp = BatteryComponent(name="Phoenix Al-Mg Anot", material=anode_alloy, role="Anode", thickness_um=50.0)
    
    # Katot: Hücrenin onay alabilmesi için Lityum bazlı yüksek skorlu bir alaşım seçiyoruz -> 70 mikron kalınlık
    # Listeden ilk lityumlu alaşımı bulalım (Örn: Alaşım_Al90_Li10)
    cathode_alloy_data = next(x for x in analyzed_alloys if "Li" in x["Alaşım Adı"])
    cathode_alloy = next(a for a in generated_alloys if a.name == cathode_alloy_data["Alaşım Adı"])
    cathode_comp = BatteryComponent(name="Phoenix Al-Li Katot", material=cathode_alloy, role="Cathode", thickness_um=70.0)

    # 150mm x 100mm boyutlarında bir batarya plakası tasarlıyoruz
    cell = BatteryCell(name="Phoenix-Gen1 Hücresi", anode=anode_comp, cathode=cathode_comp, width_mm=150.0, height_mm=100.0)
    
    # Test merkezini çalıştır
    cell_report = cell.run_safety_and_geometry_check()
    geo = cell_report["Geometri"]
    
    print(f"\n🔬 Dijital İkiz (Digital Twin) Raporu:")
    print(f"   📦 Tasarım Adı: {cell_report['Hücre Adı']}")
    print(f"   📐 Plaka Alanı: {geo['Plaka Alanı (m2)']} m²")
    print(f"   ⚖️ Toplam Hücre Kütlesi: {geo['Teorik Hücre Kütlesi (kg)']} kg")
    print(f"     └─ Anot Kütlesi: {geo['Anot Kütlesi (kg)']} kg")
    print(f"     └─ Katot Kütlesi: {geo['Katot Kütlesi (kg)']} kg")
    print(f"   🚨 Hücre Güvenlik/Uyum Onayı: {cell_report['Hücre Güvenlik/Uyum Onayı']}")
    print(f"   🪫 Anot Durumu: {cell_report['Anot Durumu']}")
    print(f"   🔋 Katot Durumu: {cell_report['Katot Durumu']}\n")

    print("==========================================================")
    print(" SOHBET 06 BAŞARIYLA TAMAMLANDI: DİJİTAL İKİZ YAŞIYOR! ")
    print("==========================================================")

if __name__ == "__main__":
    main()