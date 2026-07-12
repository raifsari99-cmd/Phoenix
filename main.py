from core.simulation import BatterySimulationEngine
# validation klasöründen yeni dosyamızı import ediyoruz
from validation.validation_framework import ValidationFramework 

def main():
    print("==========================================================")
    print("       PHOENIX VALIDATION FRAMEWORK - SOHBET 11           ")
    print("==========================================================\n")

    cell_capacity_ah = 5.0

    print("🏃 Simülasyon motoru test verilerini üretiyor...")
    sim_1c = BatterySimulationEngine.run_discharge_profile(nominal_capacity_ah=cell_capacity_ah, c_rate=1.0, ambient_temp_c=25.0)
    sim_3c = BatterySimulationEngine.run_discharge_profile(nominal_capacity_ah=cell_capacity_ah, c_rate=3.0, ambient_temp_c=25.0)

    print("\n🔬 Gerçek Laboratuvar Verileriyle Karşılaştırma Başlatıldı...\n")

    # --- 1C Doğrulama ---
    val_1c = ValidationFramework.validate_scenario(
        c_rate_str="1C",
        sim_max_temp=sim_1c["Maksimum Hücre Sıcaklığı (°C)"],
        sim_final_voltage=sim_1c["Voltaj Değişim Eğrisi (V)"][-1]
    )
    print("📊 [1C DEŞARJ DOĞRULAMA SONUÇLARI]")
    print(f"   └─ Sıcaklık Sapması: {val_1c['Simülasyon Sıcaklık Sapması (°C)']} °C (Lab: {val_1c['Laboratuvar Ref Sıcaklık (°C)']} °C)")
    print(f"   └─ Voltaj Sapması: {val_1c['Simülasyon Voltaj Sapması (V)']} V (Lab: {val_1c['Laboratuvar Ref Voltaj (V)']} V)")
    print(f"   🎯 GÜVEN SKORU: %{val_1c['GÜVEN SKORU (%)']}")
    print(f"   🚨 Durum: {val_1c['Doğrulama Durumu']}\n")

    # --- 3C Doğrulama ---
    val_3c = ValidationFramework.validate_scenario(
        c_rate_str="3C",
        sim_max_temp=sim_3c["Maksimum Hücre Sıcaklığı (°C)"],
        sim_final_voltage=sim_3c["Voltaj Değişim Eğrisi (V)"][-1]
    )
    print("🔥 [3C DEŞARJ DOĞRULAMA SONUÇLARI]")
    print(f"   └─ Sıcaklık Sapması: {val_3c['Simülasyon Sıcaklık Sapması (°C)']} °C (Lab: {val_3c['Laboratuvar Ref Sıcaklık (°C)']} °C)")
    print(f"   └─ Voltaj Sapması: {val_3c['Simülasyon Voltaj Sapması (V)']} V (Lab: {val_3c['Laboratuvar Ref Voltaj (V)']} V)")
    print(f"   🎯 GÜVEN SKORU: %{val_3c['GÜVEN SKORU (%)']}")
    print(f"   🚨 Durum: {val_3c['Doğrulama Durumu']}\n")

    print("==========================================================")
    print("    SPRINT 3 TAMAMLANDI: VALIDATION SİSTEMİ MÜHÜRLÜ!     ")
    print("==========================================================")

if __name__ == "__main__":
    main()