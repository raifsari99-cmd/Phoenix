"""
PHOENIX 13 — Battery Discovery Engine
Girdi element kümesinden kombinasyon uzayı üreten ve optimize batarya DNA adayları oluşturan motor.
"""

from typing import List, Dict, Any

class BatteryDiscoveryEngine:
    """Farklı elementlerin stokiyometrik kombinasyonlarını üreterek hücre DNA adayları keşfeder."""

    @staticmethod
    def generate_material_combinations(elements: List[str], step_size: float = 0.1) -> List[Dict[str, float]]:
        """Elementlerin toplamı 1.0 (yani %100) olacak şekilde tüm olası oran kombinasyonlarını üretir."""
        if not elements:
            return []
            
        combinations: List[Dict[str, float]] = []
        
        # Sadece 2 veya 3 elementli kombinasyonlar için kontrollü bir tarama uzayı
        def backtrack(index: int, current_comb: Dict[str, float], remaining_share: float):
            if index == len(elements) - 1:
                # Son elemente kalan tüm payı veriyoruz
                if remaining_share >= 0:
                    current_comb[elements[index]] = round(remaining_share, 2)
                    combinations.append(current_comb.copy())
                return

            # Adım boyutuyla kombinasyon dallanması
            steps = int(round(remaining_share / step_size)) + 1
            for i in range(steps):
                share = i * step_size
                current_comb[elements[index]] = round(share, 2)
                backtrack(index + 1, current_comb, remaining_share - share)

        backtrack(0, {}, 1.0)
        return combinations

    @staticmethod
    def screening_pipeline(elements: List[str]) -> Dict[str, Any]:
        """Üretilen ham kombinasyonları filtreler ve kararlı alaşım adaylarını ayıklar."""
        raw_combinations = BatteryDiscoveryEngine.generate_material_combinations(elements, step_size=0.2)
        filtered_candidates: List[Dict[str, float]] = []

        for comb in raw_combinations:
            # Mühendislik Filtresi: Herhangi bir elementin %0 olması veya tek bir elementin %100 baskın olmasını istemiyoruz (Alaşım Arıyoruz)
            has_pure_element = any(share >= 1.0 for share in comb.values())
            has_empty_element = any(share <= 0.0 for share in comb.values())
            
            if not has_pure_element and not has_empty_element:
                filtered_candidates.append(comb)

        return {
            "Toplam Üretilen Formül Uzayı": len(raw_combinations),
            "Filtreden Geçen Alaşım Adayı Sayısı": len(filtered_candidates),
            "Şampiyon Adaylar Listesi": filtered_candidates
        }