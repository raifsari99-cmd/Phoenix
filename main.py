from core.material import Element, Alloy
from core.geometry import BatteryHull
from core.reporter import DiscoveryReporter  # Güncellenen raporlama motoru

def main():
    print("==========================================================")
    print("        PHOENIX GEOMETRIC HULL DESIGN - SOHBET 07         ")
    print("==========================================================\n")

    # 1. Aşama Eleman ve Alaşım Altyapısı
    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    
    phoenix_structural_alloy = Alloy("Phoenix Al-Mg Şasi Alaşımı", {al: 0.90, mg: 0.10})
    print(f"🛠️ Gövde Malzemesi: {phoenix_structural_alloy.name}")
    print(f"⚖️ Alaşım Yoğunluğu: {round(phoenix_structural_alloy.density, 2)} kg/m³\n")

    hull = BatteryHull(
        name="Phoenix AeroShield V1", 
        material=phoenix_structural_alloy, 
        wall_thickness_mm=2.5, 
        internal_clearance_mm=1.0
    )

    cell_w, cell_h, cell_d = 150.0, 100.0, 20.0
    inner_dim_str = f"{cell_w} x {cell_h} x {cell_d}"
    print(f"📦 İç Hücre Çekirdek Boyutları: {inner_dim_str} mm")

    envelope = hull.calculate_envelope(inner_width_mm=cell_w, inner_height_mm=cell_h, inner_depth_mm=cell_d)

    print(f"\n📐 --- GEOMETRİK SINIR VE MEKANİK ZARF RAPORU ---")
    print(f"   🛡️ Muhafaza Adı: {hull.name}")
    print(f"   📏 Hesaplanan Dış Ölçüler: {envelope['Dış Boyutlar (G x Y x D mm)']} mm")
    print(f"   📊 Toplam Dış Hacim: {envelope['Toplam Dış Hacim (Litre)']} Litre")
    print(f"   ⚖️ Sadece Koruyucu Gövde Ağırlığı: {envelope['Koruyucu Gövde Ağırlığı (kg)']} kg")
    print(f"   🎯 Hacimsel Paketleme Verimliliği: %{envelope['Hacimsel Paketleme Verimliliği (%)']}\n")

    # --- GEOMETRİ RAPORUNU DİSKE MÜHÜRLE ---
    print("📂 Geometrik raporlama motoru tetikleniyor...")
    report_path = DiscoveryReporter.generate_geometry_report(
        hull_name=hull.name,
        alloy_name=phoenix_structural_alloy.name,
        density=phoenix_structural_alloy.density,
        inner_dim=inner_dim_str,
        envelope=envelope
    )
    print(f"💾 Başarılı! Şasi ve Zarf Tasarım Raporu '{report_path}' olarak diske mühürlendi.\n")

    print("==========================================================")
    print(" SOHBET 07 BAŞARIYLA BAŞLATILDI: FİZİKSEL FORM OLUŞTU!    ")
    print("==========================================================")

if __name__ == "__main__":
    main()