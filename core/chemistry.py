"""
PHOENIX 08 — Kimya Motoru (Chemical Engine)
Oksidasyon, redüksiyon, yan reaksiyonlar ve dendrit oluşumu hesaplamaları.
"""

from typing import Dict, Any

class BatteryChemistryEngine:
    """Hücre içi kimyasal reaksiyon kinetiklerini ve yaşlanma faktörlerini simüle eder."""

    @staticmethod
    def simulate_reaction_kinetics(
        voltage: float, 
        current_a: float, 
        cycle_count: int,
        soc_percent: float = 100.0
    ) -> Dict[str, Any]:
        """
        Anlık voltaj, akım ve çevrim sayısına göre oksidasyon kararlılığını,
        yan reaksiyon hızını ve dendrit büyüme riskini hesaplar.
        """
        # 1. Oksidasyon ve Redüksiyon Kararlılığı (Deneysel model)
        # Voltaj 4.2V üzerine çıkarsa veya deşarjda çok düşerse yan reaksiyonlar tetiklenir
        side_reaction_rate = 0.01  # Baz yan reaksiyon hızı (%)
        
        if voltage > 4.1:
            side_reaction_rate += (voltage - 4.1) * 0.5
        elif voltage < 3.0:
            side_reaction_rate += (3.0 - voltage) * 0.3

        # Çevrim sayısı arttıkça yan reaksiyon birikimi artar
        se_layer_growth_factor = (cycle_count * 0.002) + (side_reaction_rate * 0.1)

        # 2. Dendrit Oluşum Riski Hesaplaması (0 - 100 Skoru)
        # Yüksek akım yoğunluğu (C-rate) ve yüksek şarj seviyelerinde (SoC) dendrit riski katlanır
        dendrite_risk = (current_a * 5.0) + (soc_percent * 0.3) + (cycle_count * 0.05)
        
        # Risk sınırlandırması
        dendrite_risk = min(max(dendrite_risk, 0.0), 100.0)

        # Durum Analizi
        if dendrite_risk > 75:
            status = "TEHLİKELİ (Dendrit kısa devresi riski yüksek!)"
        elif dendrite_risk > 40:
            status = "RİSKLİ (Mikro-dendrit oluşumu gözleniyor)"
        else:
            status = "KARARLI (Kimyasal yüzey homojen)"

        return {
            "Yan Reaksiyon Hızı (%)": round(side_reaction_rate * 100, 3),
            "SEI Tabakası Büyüme Katsayısı": round(se_layer_growth_factor, 4),
            "Dendrit Oluşum Riski (0-100)": round(dendrite_risk, 2),
            "Kimyasal Kararlılık Durumu": status
        }