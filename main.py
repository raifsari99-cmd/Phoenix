"""
PHOENIX Ana Giriş ve Test Betiği
Yazılan bilimsel standartların ve malzeme/alaşım sisteminin doğrulanması.
"""

from core.standards import UnitConverter
from core.material import Element, Alloy

def main():
    print("========================================")
    print("   PHOENIX SIMULATOR - SPRINT 1 TESTI   ")
    print("========================================\n")

    # 1. Bilimsel Standartlar Testi
    print("[1] Birim Dönüşüm Motoru Test Ediliyor...")
    celsius_temp = 25.0
    kelvin_temp = UnitConverter.celsius_to_kelvin(celsius_temp)
    print(f"    Sıcaklık: {celsius_temp}°C -> {kelvin_temp} K")
    print(f"    Batarya Kapasitesi: 2500 mAh -> {UnitConverter.mah_to_coulomb(2500):.1f} Coulomb\n")

    # 2. Element Tanımlama Testi
    print("[2] Laboratuvar Elementleri Oluşturuluyor...")
    # Alüminyum ve Magnezyum elementlerini gerçek fiziksel değerleriyle tanımlıyoruz
    aluminum = Element(name="Alüminyum", symbol="Al", atomic_weight=26.98, density=2700.0, thermal_capacity=897.0, electrical_conductivity=3.5e7)
    magnesium = Element(name="Magnezyum", symbol="Mg", atomic_weight=24.30, density=1738.0, thermal_capacity=1020.0, electrical_conductivity=2.2e7)
    
    print(f"    {aluminum.get_chemical_info()}")
    print(f"    {magnesium.get_chemical_info()}\n")

    # 3. Alaşım Hesaplama Motoru Testi
    print("[3] Özel Alaşım Formülü Simüle Ediliyor...")
    try:
        # %85 Alüminyum - %15 Magnezyum alaşımı
        custom_alloy = Alloy(
            name="Phoenix Al-Mg Şasi Alaşımı", 
            components={aluminum: 0.85, magnesium: 0.15}
        )
        print(f"    {custom_alloy.get_alloy_composition()}")
        print(f"    {custom_alloy.get_summary()}")
    except ValueError as e:
        print(f"    Hata oluştu: {e}")

    print("\n========================================")
    print("     TEST BAŞARIYLA TAMAMLANDI!      ")
    print("========================================")

if __name__ == "__main__":
    main()