"""
PHOENIX 04 — Evrensel Veri Modeli / Malzeme Sistemi
Evrendeki tüm elementlerin, alaşımların ve kompozitlerin türeyeceği 
temel Material sınıfı ve Element alt yapısı.
"""

import math
from typing import Dict

class Material:
    """ Phoenix Evrenindeki tüm maddelerin ortak atası olan temel sınıf. """
    def __init__(self, name: str, density: float, thermal_capacity: float):
        self.name = name
        self.density = density  # Kütlesel Yoğunluk [kg/m^3]
        self.thermal_capacity = thermal_capacity  # Özgül Isı Kapasitesi [J/(kg*K)]
        
    def get_summary(self) -> str:
        """Malzemenin temel fiziksel özelliklerinin özetini döner."""
        return f"Malzeme: {self.name} | Yoğunluk: {self.density} kg/m³ | Isı Kapasitesi: {self.thermal_capacity} J/(kg*K)"


class Element(Material):
    """
    Periyodik tablodaki saf elementleri temsil eden alt sınıf.
    Malzeme özelliklerine ek olarak kimyasal ve atomik parametreler barındırır.
    """
    def __init__(self, 
                 name: str, 
                 symbol: str, 
                 atomic_weight: float, 
                 density: float, 
                 thermal_capacity: float,
                 electrical_conductivity: float):
        
        # Üst sınıfın (Material) kurucu fonksiyonunu çağırıyoruz
        super().__init__(name=name, density=density, thermal_capacity=thermal_capacity)
        
        self.symbol = symbol  # Kimyasal Simge (Örn: Al, Mg, Li)
        self.atomic_weight = atomic_weight  # Atom Ağıvalığı [g/mol]
        self.electrical_conductivity = electrical_conductivity  # Elektriksel İletkenlik [S/m]

    def get_chemical_info(self) -> str:
        """Elementin kimyasal kimlik bilgilerini döner."""
        return f"Element: {self.name} ({self.symbol}) | Atom Ağırlığı: {self.atomic_weight} g/mol | İletkenlik: {self.electrical_conductivity} S/m"


class Alloy(Material):
    """
    Birden fazla elementin fiziksel olarak birleşmesiyle oluşan alaşım sınıfı.
    Karışım oranlarına göre teorik yoğunluk ve iletkenlik hesaplamaları yapar.
    """
    def __init__(self, name: str, components: Dict[Element, float]):
        """
        components: Sözlük yapısında Element nesnesi ve kütlesel oranı barındırır.
                    Örn: {alüminyum_nesnesi: 0.85, magnezyum_nesnesi: 0.15}
        """
        self.components = components
        
        # Karışım oranlarının toplamının 1.0 (yani %100) olduğunu doğrula
        total_ratio = sum(components.values())
        if not math.isclose(total_ratio, 1.0, rel_tol=1e-5):
            raise ValueError(f"Hata: Alaşım oranları toplamı 1.0 olmalıdır! Mevcut: {total_ratio}")
            
        # Teorik yoğunluk ve ısı kapasitesini hesapla
        calculated_density = self._calculate_mixture_density()
        calculated_thermal = self._calculate_mixture_thermal()
        
        # Üst sınıfı hesaplanan bu dinamik değerlerle başlat
        super().__init__(name=name, density=calculated_density, thermal_capacity=calculated_thermal)

    def _calculate_mixture_density(self) -> float:
        """Kütlesel oranlara göre alaşımın teorik yoğunluğunu hesaplar."""
        # Tersi oranların toplamı üzerinden (1 / Yoğunluk) formülü
        inverse_density_sum = sum(ratio / element.density for element, ratio in self.components.items())
        return 1.0 / inverse_density_sum

    def _calculate_mixture_thermal(self) -> float:
        """Kütlesel oranlara göre alaşımın ortalama özgül ısı kapasitesini hesapla."""
        return sum(element.thermal_capacity * ratio for element, ratio in self.components.items())

    def get_alloy_composition(self) -> str:
        """Alaşımın içindeki elementleri ve yüzdelik oranlarını listeler."""
        comp_text = ", ".join([f"%{ratio*100:.1f} {element.symbol}" for element, ratio in self.components.items()])
        return f"Alaşım: {self.name} [{comp_text}] | Hesaplanan Yoğunluk: {self.density:.2f} kg/m³"