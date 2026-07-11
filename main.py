from core.material import Element, Alloy
from core.geometry import BatteryHull
import core.physics # Doğrudan modülü import ederek import hatasını bypass ediyoruz

def main():
    print("==========================================================")
    print("      PHOENIX DISCOVERY & PHYSICS CORE - SOHBET 07       ")
    print("==========================================================\n")

    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    phoenix_structural_alloy = Alloy("Phoenix Al-Mg Şasi Alaşımı", {al: 0.90, mg: 0.10})

    hull = BatteryHull(name="Phoenix AeroShield V1", material=phoenix_structural_alloy, wall_thickness_mm=2.5, internal_clearance_mm=1.0)
    
    cell_w, cell_h, cell_d = 150.0, 100.0, 20.0
    envelope = hull.calculate_envelope(inner_width_mm=cell_w, inner_height_mm=cell_h, inner_depth_mm=cell_d)
    plate_area = (cell_w * 1e-3) * (cell_h * 1e-3)

    print(f"📦 Muhafaza Zarfı ve Geometrisi Hazır: {envelope['Dış Boyutlar (G x Y x D mm)']} mm")
    print("⚡ Fizik Motoru Çekirdeği Ateşleniyor (İyon akışı ve Elektron dinamiği)...")

    # Modül üzerinden güvenli çağrı yapıyoruz
    physics_data = core.physics.ElectroChemicalPhysicsEngine.calculate_cell_dynamics(
        anode_thickness_um=50.0,
        cathode_thickness_um=70.0,
        plate_area_m2=plate_area,
        temperature_k=298.15,
        target_current_a=5.0
    )

    print(f"\n🔬 Elektrokimyasal Fizik Çıktıları:")
    print(f"   🔋 Hücre İç Direnci: {physics_data['İç Direnç (Ohm)']} Ohm")
    print(f"   🔄 Mol İyon Akış Hızı: {physics_data['İyon Akısı (mol/s)']} mol/s")
    print(f"   📉 Ohmik Voltaj Düşümü: -{physics_data['Ohmik Voltaj Düşümü (V)']} V")
    print(f"   🔥 Termal Aktivasyon Kaybı: -{physics_data['Aktivasyon Kaybı (V)']} V")
    print(f"   🎯 Yük Altındaki Net Voltaj: {physics_data['Yük Altındaki Anlık Voltaj (V)']} V\n")

    print("==========================================================")
    print(" FİZİK MOTORU ÇEKİRDEĞE İŞLENDİ: SOHBET 07 TAMAMLANDI!   ")
    print("==========================================================")

if __name__ == "__main__":
    main()