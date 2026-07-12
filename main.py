from core.discovery import BatteryDiscoveryEngine

def main():
    print("==========================================================")
    print("       PHOENIX BATTERY DISCOVERY ENGINE - SOHBET 13        ")
    print("==========================================================\n")

    # Keşif motoruna test etmek istediğimiz element kombinasyon setini veriyoruz
    # Örn: Lityum (Li), Nikel (Ni), Manganez (Mn) tabanlı deneysel bir alaşım arayışı
    target_elements = ["Li", "Ni", "Mn"]
    
    print(f"🧬 Elementer Uzay Taraması Başlatılıyor: {target_elements}...")
    
    discovery_results = BatteryDiscoveryEngine.screening_pipeline(target_elements)
    
    print(f"\n📊 Keşif Hattı (Pipeline) Özet Çıktıları:")
    print(f"   ├─ Toplam Matematiksel Kombinasyon: {discovery_results['Toplam Üretilen Formül Uzayı']} adet")
    print(f"   └─ Filtreden Geçen Kararlı Alaşım Adayı: {discovery_results['Filtreden Geçen Alaşım Adayı Sayısı']} adet")
    
    print("\n🔬 Keşfedilen ve Test Edilmeye Hazır Batarya DNA'ları (İlk Örnekler):")
    for idx, candidate in enumerate(discovery_results["Şampiyon Adaylar Listesi"]):
        # Formülü şık bir string haline getiriyoruz (Örn: Li(0.2)Ni(0.4)Mn(0.4))
        formula_str = "".join([f"{el}({share})" for el, share in candidate.items()])
        print(f"   🎯 DNA #{idx+1}: {formula_str}")

    print("\n==========================================================")
    print("   DISCOVERY ENGINE DEVREDE: SOHBET 13 BAŞARIYLA TAMAM!   ")
    print("==========================================================")

if __name__ == "__main__":
    main()