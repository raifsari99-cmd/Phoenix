"""
PHOENIX 14 — Scientific Decision & Reporting Engine
Keşfedilen batarya DNA kombinasyonlarını maliyet, üretilebilirlik ve fizik/kimya süzgecinden geçirerek skorlar.
"""

from typing import Dict, Any, List

class ScientificDecisionEngine:
    """Alaşım adaylarını endüstriyel ve bilimsel kriterlere göre puanlayan karar mekanizması."""

    # Ton başına ortalama elementel maliyet indeksleri (Dolar cinsinden teorik piyasa verisi)
    ELEMENT_COST_INDEX = {
        "Li": 45000.0,  # Lityum: Stratejik ve pahalı
        "Ni": 18000.0,  # Nikel: Performans artırır, maliyeti orta-yüksek
        "Mn": 2500.0,   # Manganez: Ucuz ve kararlı
    }

    @staticmethod
    def evaluate_candidate(formula: Dict[str, float]) -> Dict[str, Any]:
        """Bir formül adayının maliyetini, üretilebilirliğini ve nihai bilimsel skorunu hesaplar."""
        
        # 1. Hammadde Maliyet Hesabı (Ağırlıklı Ortalama)
        raw_material_cost_score = 0.0
        for element, share in formula.items():
            cost = ScientificDecisionEngine.ELEMENT_COST_INDEX.get(element, 10000.0)
            raw_material_cost_score += cost * share

        # 2. Üretilebilirlik Skoru (Örn: Çok yüksek Lityum oranı üretimi zorlaştırır/hassastır)
        # Dengeli formüller endüstriyel olarak daha rahat üretilir.
        li_share = formula.get("Li", 0.0)
        if li_share > 0.5:
            manufacturability_score = 60.0  # Yüksek reaktivite riskinden dolayı düşük puan
        else:
            manufacturability_score = 90.0  # Kararlı üretim aralığı

        # 3. Elektrokimyasal Performans Projeksiyonu (Teorik Enerji Yoğunluğu Çarpanı)
        # Nikel oranı enerji yoğunluğunu artırırken, Manganez ömrü ve kararlılığı artırır.
        ni_share = formula.get("Ni", 0.0)
        mn_share = formula.get("Mn", 0.0)
        performance_score = (ni_share * 100.0) + (mn_share * 50.0) + (li_share * 80.0)

        # 4. Nihai Phoenix Skoru (Scientific Score)
        # Performans ve üretilebilirlik yüksek, maliyet düşük olmalı.
        # Maliyeti 0-100 arasına normalize eden basit ters orantı
        cost_penalty = min((raw_material_cost_score / 50000.0) * 100, 40)
        final_score = (performance_score * 0.4) + (manufacturability_score * 0.4) - cost_penalty

        return {
            "Hammadde Maliyet Endeksi ($/Ton)": round(raw_material_cost_score, 2),
            "Üretilebilirlik Skoru (%)": round(manufacturability_score, 2),
            "Teorik Performans Skoru": round(performance_score, 2),
            "NİHAİ PHOENIX SKORU": round(max(final_score, 0.0), 2)
        }