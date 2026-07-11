"""
PHOENIX 13 — Battery Discovery Engine (1. Aşama: Gelişmiş Kombinasyon Motoru)
Verilen element listesinden matematiksel olarak olası tüm n-li alaşım 
kombinasyonlarını ve kütlesel oranları dinamik olarak türetir.
"""

import itertools
from typing import List, Dict
from core.material import Element, Alloy

class CombinationEngine:
    """Her büyüklükteki element havuzundan varyasyonlar üreten evrensel motor."""

    @staticmethod
    def generate_alloys(elements: List[Element], step: float = 0.1) -> List[Alloy]:
        """
        Verilen element listesindeki elemanların 2'li, 3'lü ve daha fazla kombinasyonunu
        belirtilen adım hassasiyetiyle dinamik olarak türetir.
        """
        alloys = []
        n = len(elements)
        if n < 2:
            return alloys

        # Adım çözünürlüğüne göre paylaştırılacak tam sayı tamsayı parça sayısı (Örn: 0.1 için 10 parça)
        num_steps = int(round(1.0 / step))

        # 2'li kombinasyonlardan başlayıp havuzun toplam eleman sayısına kadar tüm kombinasyon boyutlarını tara
        for r in range(2, n + 1):
            for combo in itertools.combinations(elements, r):
                # combo: seçilen r adet Element nesnesini içerir (Örn: (Al, Mg, Sn))
                
                # Toplamı num_steps olan ve r adet pozitif tam sayı barındıran tüm bölme olasılıkları
                for partitions in itertools.product(range(1, num_steps), repeat=r):
                    if sum(partitions) == num_steps:
                        # Tam sayı parçaları tekrar float oranlara (%..) dönüştürüyoruz
                        components = {}
                        name_parts = []
                        
                        for el, part in zip(combo, partitions):
                            ratio = round(part * step, 2)
                            components[el] = ratio
                            name_parts.append(f"{el.symbol}{int(ratio*100)}")
                        
                        try:
                            alloy_name = f"Alaşım_{'_'.join(name_parts)}"
                            alloys.append(Alloy(alloy_name, components))
                        except ValueError:
                            continue
        return alloys