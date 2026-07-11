"""
PHOENIX 19 — Scientific Decision Engine (Ön Analizör Modülü)
Malzemelerin ve alaşımların laboratuvar simülasyonu öncesi maliyet, 
bulunabilirlik ve üretilebilirlik kriterlerine göre süzgeçten geçirilmesi.
"""

from typing import Dict, Any
from core.material import Element, Alloy

# --- EVRENSEL TİCARİ VE LOJİSTİK VERİ TABANI ---
# Gerçekçi piyasa yaklaşımları (Örnek ham fiyat $/kg ve Tedarik Risk Skoru 1-10)
# Risk Skoru: 1 (Her yerde var, bol) -> 10 (Çok nadir, kritik kriz riski)
MARKET_DATA = {
    "Al": {"price_per_kg": 2.5, "supply_risk": 2},   # Alüminyum: Ucuz, bol
    "Mg": {"price_per_kg": 3.8, "supply_risk": 4},   # Magnezyum: Makul, hafif riskli
    "Li": {"price_per_kg": 18.0, "supply_risk": 8},  # Lityum: Pahalı, yüksek jeopolitik risk
    "Sn": {"price_per_kg": 25.0, "supply_risk": 6},  # Kalay: Orta/Yüksek maliyet
}

class MaterialAnalyzer:
    """Malzemelerin ticari, lojistik ve teorik uygunluğunu puanlayan motor."""

    @staticmethod
    def analyze_element(element: Element) -> Dict[str, Any]:
        """Tek bir saf elementin maliyet ve lojistik risk analizini yapar."""
        symbol = element.symbol
        # Eğer veri tabanında yoksa varsayılan ortalama bir değer ata
        data = MARKET_DATA.get(symbol, {"price_per_kg": 10.0, "supply_risk": 5})
        
        return {
            "Birim Maliyet ($/kg)": data["price_per_kg"],
            "Tedarik Zinciri Riski (1-10)": data["supply_risk"],
            "Elektriksel Avantaj (S/m)": element.electrical_conductivity
        }

    @staticmethod
    def analyze_alloy(alloy: Alloy) -> Dict[str, Any]:
        """
        Bir alaşımın kütlesel oranlarına göre ağırlıklı maliyetini,
        ortalama tedarik riskini ve nihai Üretilebilirlik Uygunluk Skorunu hesaplar.
        """
        total_cost_per_kg = 0.0
        weighted_risk = 0.0
        
        for element, ratio in alloy.components.items():
            data = MARKET_DATA.get(element.symbol, {"price_per_kg": 10.0, "supply_risk": 5})
            
            # Oransal maliyet ve risk biriktirme
            total_cost_per_kg += data["price_per_kg"] * ratio
            weighted_risk += data["supply_risk"] * ratio

        # --- ÜRETİLEBİLİRLİK VE UYGUNLUK SKORU (SUITABILITY SCORE) ---
        # Maliyet ve risk arttıkça skor düşer. Temel ideal puan: 100
        # Formül: Maliyet ve riske ağırlıklı cezalar kesilir
        cost_penalty = total_cost_per_kg * 1.5
        risk_penalty = weighted_risk * 5.0
        suitability_score = 100.0 - (cost_penalty + risk_penalty)
        
        # Skoru 0 ile 100 arasında sınırla
        suitability_score = max(0.0, min(100.0, suitability_score))

        return {
            "Alaşım Adı": alloy.name,
            "Hesaplanan Maliyet ($/kg)": round(total_cost_per_kg, 2),
            "Ağırlıklı Tedarik Riski (1-10)": round(weighted_risk, 2),
            "Üretilebilirlik Uygunluk Skoru (0-100)": round(suitability_score, 2)
        }