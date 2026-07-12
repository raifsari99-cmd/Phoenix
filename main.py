from core.discovery import BatteryDiscoveryEngine
from core.reporter import ScientificDecisionEngine

def main():
    print("==========================================================")
    print("       PHOENIX SCIENTIFIC DECISION ENGINE - SOHBET 14      ")
    print("==========================================================\n")

    target_elements = ["Li", "Ni", "Mn"]
    print(f"🧬 Tasarım uzayından alaşım kombinasyonları çekiliyor...")
    
    # Keşif motorundan süzülen 6 kararlı alaşım adayını alıyoruz
    discovery_results = BatteryDiscoveryEngine.screening_pipeline(target_elements)
    candidates = discovery_results["Şampiyon Adaylar Listesi"]

    print(f"🔬 Toplam {len(candidates)} kararlı aday Bilimsel Karar Süzgecine giriyor...\n")

    champion_formula = None
    champion_score = -1.0
    champion_report = {}

    for idx, formula in enumerate(candidates):
        formula_str = "".join([f"{el}({share})" for el, share in formula.items()])
        
        # Karar motorunu tetikliyoruz
        analysis = ScientificDecisionEngine.evaluate_candidate(formula)
        score = analysis["NİHAİ PHOENIX SKORU"]

        print(f"   📊 Aday #{idx+1} [{formula_str}] ➔ Skor: {score} | Maliyet: {analysis['Hammadde Maliyet Endeksi ($/Ton)']} $/Ton")

        # En yüksek puanlı adayı hafızada tutuyoruz
        if score > champion_score:
            champion_score = score
            champion_formula = formula_str
            champion_report = analysis

    print("\n👑 ==================== ŞAMPİYON ADAY SEÇİLDİ ====================")
    print(f"   🏆 En Optimize Formül: {champion_formula}")
    print(f"   🎯 Phoenix Skor Derecesi: {champion_score} / 100")
    print(f"   💰 Tahmini Hammadde Maliyeti: {champion_report['Hammadde Maliyet Endeksi ($/Ton)']} $/Ton")
    print(f"   🛠️ Üretilebilirlik Endeksi: %{champion_report['Üretilebilirlik Skoru (%)']}")
    print("==================================================================")

if __name__ == "__main__":
    main()