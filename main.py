from core.simulation import BatterySimulationEngine

def main():
    print("==========================================================")
    print("       PHOENIX SIMULATION ENGINE (PyBaMM) - SOHBET 10     ")
    print("==========================================================\n")

    print("🚀 Hücre Dinamik Simülasyon Laboratuvarı Başlatılıyor...")
    
    # 5.0 Ah kapasiteli Phoenix-Gen1 prototip hücremizi tanımlıyoruz
    cell_capacity_ah = 5.0
    
    # SENARYO A: Standart Sürüş Deşarjı (1C Akım, 25°C Ortam Sıcaklığı)
    print("\n📊 [SENARYO A] Standart Deşarj Testi (1C Rate)...")
    sim_a = BatterySimulationEngine.run_discharge_profile(
        nominal_capacity_ah=cell_capacity_ah,
        c_rate=1.0,
        ambient_temp_c=25.0
    )
    
    print(f"   ⚡ Çekilen Akım: {sim_a['Test Akımı (A)']} A")
    print(f"   ⏱️ Test Süresi: {sim_a['Simülasyon Süresi (sn)']} saniye")
    print(f"   🌡️ Tepe Sıcaklık: {sim_a['Maksimum Hücre Sıcaklığı (°C)']} °C")
    print(f"   📈 Voltaj Eğrisi (Zamanla): {sim_a['Voltaj Değişim Eğrisi (V)']} V")
    print(f"   🚨 Termal Analiz: {sim_a['Termal Durum']}")

    # SENARYO B: Agresif Hızlı Şarj / Performans Deşarjı (3C Akım, 35°C Sıcaklık)
    print("\n🔥 [SENARYO B] Agresif Performans Testi (3C Hızlı Akım)...")
    sim_b = BatterySimulationEngine.run_discharge_profile(
        nominal_capacity_ah=cell_capacity_ah,
        c_rate=3.0,
        ambient_temp_c=35.0
    )
    
    print(f"   ⚡ Çekilen Akım: {sim_b['Test Akımı (A)']} A")
    print(f"   ⏱️ Test Süresi: {sim_b['Simülasyon Süresi (sn)']} saniye")
    print(f"   🌡️ Tepe Sıcaklık: {sim_b['Maksimum Hücre Sıcaklığı (°C)']} °C")
    print(f"   📈 Voltaj Eğrisi (Zamanla): {sim_b['Voltaj Değişim Eğrisi (V)']} V")
    print(f"   🚨 Termal Analiz: {sim_b['Termal Durum']}\n")

    print("==========================================================")
    print(" SIMÜLASYON MOTORU BAĞLANDI: SOHBET 10 BAŞARIYLA TAMAM!   ")
    print("==========================================================")

if __name__ == "__main__":
    main()