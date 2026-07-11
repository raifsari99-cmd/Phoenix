"""
PHOENIX 06 — Battery DNA & Digital Twin (2. Aşama: Batarya Uygulama Uzayı)
İlk aşamadan gelen malzemelerin elektrot (Anot/Katot) uygunluğunu denetler
ve temel hücre mimarisini simüle eder.
"""

from typing import Dict, Any
from core.material import Material, Element, Alloy

class BatteryComponent:
    """Anot, Katot veya Elektrolit gibi spesifik batarya bileşenlerinin temel sınıfı."""
    def __init__(self, name: str, material: Material, role: str):
        self.name = name
        self.material = material
        self.role = role  # "Anode", "Cathode", "Electrolyte", "Current_Collector"

    def check_electrochemical_suitability(self) -> Dict[str, Any]:
        """Malzemenin atandığı rol için elektrokimyasal ve fiziksel uygunluğunu denetler."""
        # İletkenlik ve yoğunluk kriterlerine göre basit bir uyum testi
        conductivity = getattr(self.material, 'electrical_conductivity', 0.0)
        density = self.material.density
        
        is_suitable = True
        reason = "Malzeme özellikleri bileşen kriterlerini karşılıyor."

        if self.role == "Anode":
            # Anot için hafiflik ve makul iletkenlik aranır
            if density > 5000.0:
                is_suitable = False
                reason = "Anot malzemesi çok ağır, hücre gravimetrik enerji yoğunluğunu düşürür."
        
        elif self.role == "Cathode":
            # Katot için elektrokimyasal potansiyel ve kararlılık aranır
            if isinstance(self.material, Element) and self.material.symbol == "Al":
                is_suitable = False
                reason = "Saf alüminyum doğrudan katot aktif malzemesi olmaya uygun değildir (Akım toplayıcı olabilir)."

        elif self.role == "Current_Collector":
            # Akım toplayıcı şasi şeritleri için çok yüksek iletkenlik aranır
            if conductivity < 1e7:
                is_suitable = False
                reason = "Elektriksel iletkenlik akım toplayıcı şasi için yetersiz."

        return {"Role": self.role, "Suitable": is_suitable, "Reason": reason}


class BatteryCell:
    """
    Seçilen bileşenleri, geometrik parametreleri ve güvenlik kriterlerini
    bir araya getiren nihai Dijital İkiz Hücre sınıfı.
    """
    def __init__(self, name: str, anode: BatteryComponent, cathode: BatteryComponent, volume_m3: float):
        self.name = name
        self.anode = anode
        self.cathode = cathode
        self.volume_m3 = volume_m3  # Hücre geometrik hacmi

    def calculate_theoretical_mass(self) -> float:
        """Bileşenlerin yoğunluklarından ve hücre hacminden teorik ağırlığı hesaplar."""
        # Basitleştirilmiş hacimsel ağırlık dağılımı simülasyonu
        avg_density = (self.anode.material.density + self.cathode.material.density) / 2
        return avg_density * self.volume_m3

    def run_safety_and_geometry_check(self) -> Dict[str, Any]:
        """Hücrenin geometrik ve kimyasal güvenlik bariyerlerini denetler."""
        anode_check = self.anode.check_electrochemical_suitability()
        cathode_check = self.cathode.check_electrochemical_suitability()
        
        cell_mass = self.calculate_theoretical_mass()
        
        is_safe = anode_check["Suitable"] and cathode_check["Suitable"]
        
        return {
            "Hücre Adı": self.name,
            "Teorik Hücre Kütlesi (kg)": round(cell_mass, 4),
            "Hücre Güvenlik/Uyum Onayı": "ONAYLANDI" if is_safe else "REDDEDİLDİ",
            "Anot Durumu": anode_check["Reason"],
            "Katot Durumu": cathode_check["Reason"]
        }