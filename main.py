from core.optimization import BatteryOptimizationEngine
from ai.predictor import BatteryAIPredictor
from core.reporter import ScientificDecisionEngine

def main():
    print("==========================================================")
    print("       PHOENIX GENETIC OPTIMIZATION ENGINE - SOHBET 16    ")
    print("==========================================================\n")

    target_elements = ["Li", "Ni", "Mn"]
    
    # Genetik motoru tetikliyoruz: 5 nesil boyunca popülasyonu evrimleştirecek
    opt_results = BatteryOptimizationEngine.run_genetic_optimization(
        elements=target_elements,
        generations=5,
        pop_size=10
    )

    champion_dna = opt_results["En Optimize DNA"]
    formula_str = "".join([f"{el}({share})" for el, share in champion_dna.items()])

    # Şampiyonun detay analiz raporunu alıyoruz
    ai_report = BatteryAIPredictor.predict_material_properties(champion_dna)
    econ_report = ScientificDecisionEngine.evaluate_candidate(champion_dna)

    print("\n🔬 ================= EVRİMSEL ARAMA SONUCU =================")
    print(f"   🏆 Genetik Algoritma Şampiyonu: {formula_str}")
    print(f"   📊 Birleşik Evrim Skoru: {opt_results['En Yüksek Birleşik Skor']}")
    print(f"   🔋 AI Tahmini Enerji Yoğunluğu: {ai_report['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
    print(f"   🔄 AI Tahmini Çevrim Ömrü: {ai_report['Tahmini Çevrim Ömrü (Cycle Life)']} Döngü")
    print(f"   💰 Hammadde Maliyet Endeksi: {econ_report['Hammadde Maliyet Endeksi ($/Ton)']} $/Ton")
    print(f"   🛠️ Üretilebilirlik Endeksi: %{econ_report['Üretilebilirlik Skoru (%)']}")
    print("==================================================================")

if __name__ == "__main__":
    main()