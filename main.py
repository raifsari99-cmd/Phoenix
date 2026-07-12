from core.discovery import BatteryDiscoveryEngine
from core.reporter import ScientificDecisionEngine
from ai.predictor import BatteryAIPredictor

def main():
    print("==========================================================")
    print("       PHOENIX AI PREDICTOR ENGINE - SOHBET 15            ")
    print("==========================================================\n")

    target_elements = ["Li", "Ni", "Mn"]
    print("🧬 Tasarım uzayından formüller üretiliyor ve AI süzgecine gönderiliyor...")
    
    discovery_results = BatteryDiscoveryEngine.screening_pipeline(target_elements)
    candidates = discovery_results["Şampiyon Adaylar Listesi"]

    print(f"🤖 Yapay Zekâ Modeli {len(candidates)} farklı adayı analiz ediyor...\n")

    for idx, formula in enumerate(candidates):
        formula_str = "".join([f"{el}({share})" for el, share in formula.items()])
        
        # 1. Yapay Zekâ Tahminlerini Alıyoruz
        ai_predictions = BatteryAIPredictor.predict_material_properties(formula)
        
        # 2. Klasik Bilimsel/Ekonomik Skorlamayı Alıyoruz
        economic_analysis = ScientificDecisionEngine.evaluate_candidate(formula)

        print(f"📊 [Aday #{idx+1} - {formula_str}]")
        print(f"   ├─ 🔋 AI Enerji Yoğunluğu: {ai_predictions['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
        print(f"   ├─ 🔄 AI Çevrim Ömrü: {ai_predictions['Tahmini Çevrim Ömrü (Cycle Life)']} Döngü")
        print(f"   ├─ 🎯 AI Model Güveni (R²): %{ai_predictions['AI Tahmin Güven İndeksi (R²)'] * 100}")
        print(f"   └─ 💰 Ekonomik Skor: {economic_analysis['NİHAİ PHOENIX SKORU']} Puan\n")

    print("==========================================================")
    print("    YAPAY ZEKÂ MOTORU BAĞLANDI: SOHBET 15 TAMAMLANDI!      ")
    print("==========================================================")

if __name__ == "__main__":
    main()