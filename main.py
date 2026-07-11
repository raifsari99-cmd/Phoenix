from core.material import Element, Alloy
from core.geometry import BatteryHull
import core.physics
import core.chemistry  # Yol haritasına uygun Kimya Motoru modülü

def main():
    print("==========================================================")
    print("       PHOENIX CHEMICAL KINETICS ENGINE - SOHBET 08       ")
    print("==========================================================\n")

    # 1. Temel Geometri ve Fizik Girdileri
    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    phoenix_structural_alloy = Alloy("Phoenix Al-Mg Şasi Alaşımı", {al: 0.90, mg: 0.10})

    hull = BatteryHull(name="Phoenix AeroShield V1", material=phoenix_structural_alloy, wall_thickness_mm=2.5, internal_clearance_mm=1.0)
    cell_w, cell_h, cell_d = 150.0, 100.0, 20.0
    plate_area = (cell_w * 1e-3) * (cell_h * 1e-3)

    # 2. Fizik Çekirdeğinden Voltaj Çıktısını Alıyoruz
    physics_data = core.physics.ElectroChemicalPhysicsEngine.calculate_cell_dynamics(
        anode_thickness_um=50.0,
        cathode_thickness_um=70.0,
        plate_area_m2=plate_area,
        temperature_k=298.15,
        target_current_a=5.0
    )
    
    working_voltage = physics_data['Yük Altındaki Anlık Voltaj (V)']
    print(f"⚡ Fizik Çekirdeği Voltajı: {working_voltage} V")
    print("🧪 Kimya Motoru Devreye Giriyor (Reaksiyon kinetikleri ve dendrit analizi)...")

    # 3. --- KİMYA MOTORU SİMÜLASYONU ---
    # Hücreyi 150. çevrimde (cycle), %100 dolulukta (SoC) ve 5A akımda simüle ediyoruz
    chemistry_data = core.chemistry.BatteryChemistryEngine.simulate_reaction_kinetics(
        voltage=working_voltage,
        current_a=5.0,
        cycle_count=150,
        soc_percent=100.0
    )

    print(f"\n🔬 Elektrokimyasal Kimya Çıktıları:")
    print(f"   ⚗️ Yan Reaksiyon Hızı: %{chemistry_data['Yan Reaksiyon Hızı (%)']}")
    print(f"   📈 SEI Tabakası Büyüme Katsayısı: {chemistry_data['SEI Tabakası Büyüme Katsayısı']}")
    print(f"   ⚠️ Dendrit Oluşum Riski: {chemistry_data['Dendrit Oluşum Riski (0-100)']}/100")
    print(f"   🚨 Kimyasal Kararlılık Durumu: {chemistry_data['Kimyasal Kararlılık Durumu']}\n")

    print("==========================================================")
    print("  KİMYA MOTORU ÇEKİRDEĞE İŞLENDİ: SOHBET 08 TAMAMLANDI!   ")
    print("==========================================================")

if __name__ == "__main__":
    main()