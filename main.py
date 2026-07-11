from core.material import Element, Alloy
from core.discovery import CombinationEngine
from core.analyzer import MaterialAnalyzer
from core.geometry import BatteryHull  # Yeni modülümüz

def main():
    print("==========================================================")
    print("        PHOENIX GEOMETRIC HULL DESIGN - SOHBET 07         ")
    print("==========================================================\n")

    # 1. Aşama Eleman ve Alaşım Altyapısı
    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    
    # Keşif motorundan şampiyon şasi alaşımımızı türetiyoruz (%90 Al, %10 Mg)
    # Yoğunluğu otomatik olarak malzeme kurallarına göre hesaplanıyor
    phoenix_structural_alloy = Alloy("Phoenix Al-Mg Şasi Alaşımı", {al: 0.90, mg: 0.10})
    print(f"🛠️ Gövde Malzemesi: {phoenix_structural_alloy.name}")
    print(f"⚖️ Alaşım Yoğunluğu: {round(phoenix_structural_alloy.density, 2)} kg/m³\n")

    # --- GEOMETRİK DIŞ KABUK (HULL) TANIMLAMA ---
    # 2.5 mm et kalınlığına ve 1.0 mm iç güvenlik boşluğuna sahip bir koruyucu kabuk tasarımı
    hull = BatteryHull(
        name="Phoenix AeroShield V1", 
        material=phoenix_structural_alloy, 
        wall_thickness_mm=2.5, 
        internal_clearance_mm=1.0
    )

    # İçerideki elektrot ve hücre bloğunun net fiziksel ölçüleri (Örn: 150mm x 100mm x 20mm kalınlığında hücre)
    cell_w = 150.0
    cell_h = 100.0
    cell_d = 20.0
    print(f"📦 İç Hücre Çekirdek Boyutları: {cell_w} x {cell_h} x {cell_d} mm")

    # Dış zarf ve hacimsel sınırları hesapla
    envelope = hull.calculate_envelope(inner_width_mm=cell_w, inner_height_mm=cell_h, inner_depth_mm=cell_d)

    print(f"\n📐 --- GEOMETRİK SINIR VE MEKANİK ZARF RAPORU ---")
    print(f"   🛡️ Muhafaza Adı: {hull.name}")
    print(f"   📏 Hesaplanan Dış Ölçüler: {envelope['Dış Boyutlar (G x Y x D mm)']} mm")
    print(f"   📊 Toplam Dış Hacim: {envelope['Toplam Dış Hacim (Litre)']} Litre")
    print(f"   ⚖️ Sadece Koruyucu Gövde Ağırlığı: {envelope['Koruyucu Gövde Ağırlığı (kg)']} kg")
    print(f"   🎯 Hacimsel Paketleme Verimliliği: %{envelope['Hacimsel Paketleme Verimliliği (%)']}\n")

    print("==========================================================")
    print(" SOHBET 07 BAŞARIYLA BAŞLATILDI: FİZİKSEL FORM OLUŞTU!    ")
    print("==========================================================")

if __name__ == "__main__":
    main()