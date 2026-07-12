from core.simulation import BatterySimulationEngine
from validation.validation_framework import ValidationFramework 
from visualization.plotter import BatteryVisualizer

def main():
    print("==========================================================")
    print("       PHOENIX 3D VISUALIZATION ENGINE - SOHBET 12        ")
    print("==========================================================\n")

    cell_capacity_ah = 5.0
    cell_width = 150.0
    cell_height = 100.0

    # 1. Kalibre Edilmiş Simülasyondan Gerçekçi Verileri Alıyoruz
    print("🏃 Simülasyon motoru kalibre edilmiş termal verileri üretiyor...")
    sim_3c = BatterySimulationEngine.run_discharge_profile(
        nominal_capacity_ah=cell_capacity_ah, 
        c_rate=3.0, 
        ambient_temp_c=25.0
    )
    
    max_temp = sim_3c["Maksimum Hücre Sıcaklığı (°C)"]
    print(f"🔥 Simülasyondan Gelen Tepe Sıcaklık (3C Rejimi): {max_temp} °C")

    # 2. 3B ISI HARİTASI RENDER KATMANI
    print("\n🖥️ 3B Yüzey Isı Haritası Dağılımı Hesaplanıyor...")
    heat_map = BatteryVisualizer.render_3d_heat_map(
        width_mm=cell_width,
        height_mm=cell_height,
        max_temp_c=max_temp,
        c_rate=3.0
    )
    
    print(f"   ├─ Çözünürlük: {heat_map['Grid_Boyutu']}")
    print(f"   ├─ Tepe Noktası: {heat_map['Tepe Noktası Termal Yükü']}")
    print("   └─ 3D Yüzey Sıcaklık Matrisi Dağılımı:")
    for row in heat_map["Yüzey Sıcaklık Matrisi (°C)"]:
        print(f"        {row}")

    # 3. İYON AKIŞ VAKTÖRLERİ SİMÜLASYONU
    print("\n🌌 Elektrotlar Arası İyon Akış Çizgileri Dinamiği:")
    flux_vectors = BatteryVisualizer.simulate_ion_flux_vectors(c_rate=3.0)
    for vector in flux_vectors[:3]: # İlk 3 örnek vektörü ekrana basıyoruz
        print(f"   ⚡ {vector}")
    print(f"   ... Toplam {len(flux_vectors)} aktif iyon akış vektör çizgisi render edildi.")

    print("\n==========================================================")
    print("   GÖRSELLEŞTİRME ENTEGRE EDİLDİ: SOHBET 12 MÜHÜRLÜ!      ")
    print("==========================================================")

if __name__ == "__main__":
    main()