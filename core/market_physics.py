"""
PHOENIX — Market Intelligence & Electrochemical Role Engine
Londra Metal Borsası (LME) tabanlı fiyat simülasyonu ve atomik özelliklere göre Anot/Katot/Katalizör tespiti.
"""

from typing import Dict, Any, List

class MarketAndPhysicsCore:
    # Londra Metal Borsası ve Fastmarkets verileri tabanlı ton başına güncel hammadde endeksi ($/Ton)
    REAL_MARKET_PRICES = {
        "Li": 18500.0,   # Lityum
        "Ni": 16200.0,   # Nikel
        "Mn": 2100.0,    # Manganez
        "Co": 28000.0,   # Kobalt (Çok pahalı ve kritik)
        "Au": 75000000.0,# Altın (Gerçek ton fiyatı - artık manipüle edilemez!)
        "Cu": 9300.0,    # Bakır
        "Al": 2400.0,    # Alüminyum
        "C": 1200.0      # Grafit / Karbon
    }

    # Elementlerin standart indirgenme potansiyelleri (Volt vs. SHE) - Rol tayini için fiziksel veri
    ELECTRODE_POTENTIALS = {
        "Li": -3.04,  # İnanılmaz güçlü anot adayı
        "C": -0.10,   # Standart anot/interkalasyon
        "Mn": -1.18,
        "Ni": -0.25,
        "Co": -0.28,
        "Au": 1.50    # Çok kararlı, inert / katalizör yüzey adayı
    }

    @staticmethod
    def calculate_market_cost(formula: Dict[str, float]) -> float:
        """Bileşimin gerçek borsa fiyatlarına göre ağırlıklı ton maliyetini hesaplar."""
        total_cost = 0.0
        for element, share in formula.items():
            # Eğer borsa listesinde yoksa nadir/değerli element muamelesi yap (Güvenlik Filtresi)
            cost = MarketAndPhysicsCore.REAL_MARKET_PRICES.get(element, 50000.0)
            total_cost += cost * share
        return round(total_cost, 2)

    @staticmethod
    def determine_electrochemical_role(formula: Dict[str, float]) -> Dict[str, Any]:
        """Alaşımın elementer potansiyel ağırlığına göre en verimli olacağı rolü ve katalizör kararlılığını belirler."""
        weighted_potential = 0.0
        has_precious = "Au" in formula or "Pt" in formula
        
        for element, share in formula.items():
            potential = MarketAndPhysicsCore.ELECTRODE_POTENTIALS.get(element, 0.0)
            weighted_potential += potential * share

        # Fiziksel kurallara göre rol tayini
        if weighted_potential < -1.5:
            role = "ANOT (Yüksek Voltaj Kapasiteli Negatif Elektrot)"
            efficiency_multiplier = 0.95
        elif -1.5 <= weighted_potential <= 0.2:
            if has_precious:
                role = "YÜKSEK VERİMLİ KATALİZÖR (Hızlı Elektron Reaksiyon Yüzeyi)"
                efficiency_multiplier = 0.98
            else:
                role = "DENGELİ MATRİS / KATALİZÖR DESTEK YAPISI"
                efficiency_multiplier = 0.82
        else:
            role = "KATOT (Pozitif İnterkalasyon / Enerji Depolama Merkez Katmanı)"
            efficiency_multiplier = 0.89

        return {
            "Teorik Hücre Potansiyel Ağırlığı (V)": round(weighted_potential, 2),
            "Önerilen Elektrokimyasal Rol": role,
            "Tahmini Reaksiyon/Katalizör Verimi": f"%{round(efficiency_multiplier * 100, 1)}"
        }