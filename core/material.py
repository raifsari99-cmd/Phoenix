"""
PHOENIX 04 — Evrensel Veri Modeli / Malzeme Sistemi
Evrendeki tüm elementlerin, alaşımların ve kompozitlerin türeyeceği 
temel Material sınıfı ve Element alt yapısı.
"""

from typing import Dict, Any

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
        self.atomic_weight = atomic_weight  # Atom Ağırlığı [g/mol]
        self.electrical_conductivity = electrical_conductivity  # Elektriksel İletkenlik [S/m]

    def get_chemical_info(self) -> str:
        """Elementin kimyasal kimlik bilgilerini döner."""
        return f"Element: {self.name} ({self.symbol}) | Atom Ağırlığı: {self.atomic_weight} g/mol | İletkenlik: {self.electrical_conductivity} S/m"