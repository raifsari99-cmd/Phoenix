from core.standards import UnitConverter
from core.material import Element, Alloy
from core.analyzer import MaterialAnalyzer

def main():
    print("==================================================")
    print("   PHOENIX - BİLİMSEL KARAR MOTORU ÖN TESTİ       ")
    print("==================================================\n")

    # Elementleri Tanımla
    al = Element("Alüminyum", "Al", 26.98, 2700.0, 897.0, 3.5e7)
    mg = Element("Magnezyum", "Mg", 24.30, 1738.0, 1020.0, 2.2e7)
    li = Element("Lityum", "Li", 6.94, 534.0, 3582.0, 1.1e7)

    # 1. Senaryo: Senin Düşündüğün Ekonomik Al-Mg Alaşımı
    alloy_phoenix = Alloy("Phoenix Hafif Şasi Alaşımı", {al: 0.85, mg: 0.15})
    analysis_phoenix = MaterialAnalyzer.analyze_alloy(alloy_phoenix)

    # 2. Senaryo: Teorik Olarak Harika Ama Ticari Olarak Çılgın Bir Lityum Alaşımı
    alloy_crazy = Alloy("Teorik Yüksek Riskli Alaşım", {al: 0.30, li: 0.70})
    analysis_crazy = MaterialAnalyzer.analyze_alloy(alloy_crazy)

    # SONUÇLARI KIYASLA
    print(f"🔬 MATERYAL 1: {analysis_phoenix['Alaşım Adı']}")
    print(f"   💰 Tahmini Maliyet: {analysis_phoenix['Hesaplanan Maliyet ($/kg)']} $/kg")
    print(f"   ⚠️ Tedarik Riski: {analysis_phoenix['Ağırlıklı Tedarik Riski (1-10)']}/10")
    print(f"   🎯 UYGUNLUK SKORU: {analysis_phoenix['Üretilebilirlik Uygunluk Skoru (0-100)']}/100\n")

    print(f"🔬 MATERYAL 2: {analysis_crazy['Alaşım Adı']}")
    print(f"   💰 Tahmini Maliyet: {analysis_crazy['Hesaplanan Maliyet ($/kg)']} $/kg")
    print(f"   ⚠️ Tedarik Riski: {analysis_crazy['Ağırlıklı Tedarik Riski (1-10)']}/10")
    print(f"   🎯 UYGUNLUK SKORU: {analysis_crazy['Üretilebilirlik Uygunluk Skoru (0-100)']}/100\n")

    if analysis_phoenix['Üretilebilirlik Uygunluk Skoru (0-100)'] > analysis_crazy['Üretilebilirlik Uygunluk Skoru (0-100)']:
        print("💡 Karar Motoru Raporu: Sürdürülebilir üretim için 1. Malzeme (Phoenix Alaşımı) çok daha avantajlı!")
    else:
        print("💡 Karar Motoru Raporu: Risk yüksek olsa da 2. Malzeme performans için seçilebilir.")

if __name__ == "__main__":
    main()