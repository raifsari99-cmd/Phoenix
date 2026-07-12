"""
PHOENIX 16 — Optimization Engine
Genetik algoritma ve Pareto optimizasyon mantığıyla en iyi hücre bileşimlerini evrimsel olarak bulan motor.
"""

import random
from typing import List, Dict, Any
from ai.predictor import BatteryAIPredictor
from core.reporter import ScientificDecisionEngine

class BatteryOptimizationEngine:
    """En iyi batarya DNA'larını bulmak için evrimsel genetik algoritmaları koşturur."""

    @staticmethod
    def _create_random_dna(elements: List[str]) -> Dict[str, float]:
        """Toplamları 1.0 olacak şekilde rastgele element oranları üretir."""
        raw_shares = [random.random() for _ in range(len(elements))]
        total = sum(raw_shares)
        return {elements[i]: round(raw_shares[i] / total, 2) for i in range(len(elements))}

    @staticmethod
    def run_genetic_optimization(elements: List[str], generations: int = 5, pop_size: int = 10) -> Dict[str, Any]:
        """Belirtilen nesil sayısı boyunca en iyi formülleri türetir ve optimize eder."""
        
        # 1. Başlangıç Popülasyonu (İlk Nesil Rastgele Adaylar)
        populasyon = [BatteryOptimizationEngine._create_random_dna(elements) for _ in range(pop_size)]
        
        best_overall_dna = None
        best_overall_score = -1.0
        
        print(f"🧬 Evrimsel Arama Başladı: {pop_size} adaylık popülasyon, {generations} nesil boyunca yarıştırılacak...\n")

        for gen in range(generations):
            skorlu_populasyon = []
            
            for dna in populasyon:
                # AI ve Ekonomik süzgeçleri birleştirip bir uygunluk (fitness) skoru üretiyoruz
                ai_perf = BatteryAIPredictor.predict_material_properties(dna)
                econ = ScientificDecisionEngine.evaluate_candidate(dna)
                
                # Hem yüksek enerji yoğunluğu hem de yüksek ekonomik puan isteyen hibrit skor
                fitness_score = (ai_perf["Tahmini Enerji Yoğunluğu (Wh/kg)"] * 0.1) + econ["NİHAİ PHOENIX SKORU"]
                skorlu_populasyon.append((fitness_score, dna))
                
                if fitness_score > best_overall_score:
                    best_overall_score = fitness_score
                    best_overall_dna = dna

            # Skorlara göre en iyileri sırala
            skorlu_populasyon.sort(key=lambda x: x[0], reverse=True)
            
            # Elitizm: En iyi 4 adayı doğrudan bir sonraki nesle taşıyoruz
            yeni_nesil = [skorlu_populasyon[i][1] for i in range(4)]
            
            # Çaprazlama ve Mutasyon ile yeni bireyler üretme
            while len(yeni_nesil) < pop_size:
                parent1 = skorlu_populasyon[random.randint(0, 3)][1]
                parent2 = skorlu_populasyon[random.randint(0, 4)][1]
                
                # Çocuk DNA üretimi (Çaprazlama)
                child_dna = {}
                for el in elements:
                    child_dna[el] = round((parent1[el] + parent2[el]) / 2, 2)
                
                # Toplamı 1.0'a normalize etme
                tot = sum(child_dna.values())
                if tot > 0:
                    child_dna = {k: round(v / tot, 2) for k, v in child_dna.items()}
                
                # Küçük Mutasyon Riski (%20 ihtimalle oran sapması)
                if random.random() < 0.2:
                    target_el = random.choice(elements)
                    child_dna[target_el] = round(max(child_dna[target_el] + random.choice([-0.05, 0.05]), 0.05), 2)
                    tot = sum(child_dna.values())
                    child_dna = {k: round(v / tot, 2) for k, v in child_dna.items()}

                yeni_nesil.append(child_dna)
                
            populasyon = yeni_nesil
            print(f"   ↳ Nesil #{gen+1} Tamamlandı. En İyi Anlık Skor: {round(skorlu_populasyon[0][0], 2)}")

        return {
            "En Optimize DNA": best_overall_dna,
            "En Yüksek Birleşik Skor": round(best_overall_score, 2)
        }