"""
PHOENIX 06 — Battery DNA & Digital Twin (2. Aşama: Hücre Anatomisi ve Geometri)
Bileşenlerin elektrot uygunluğunu denetler, katmanlı hücre geometrisini
ve hacimsel/gravimetrik ağırlıkları simüle eder.
"""

from typing import Dict, Any
from core.material import Material, Element, Alloy

class BatteryComponent:
    """Anot, Katot veya Elektrolit gibi spesifik batarya bileşenlerinin temel sınıfı."""
    def __init__(self, name: str, material: Material, role: str, thickness_um: float):
        self.name = name
        self.material = material
        self.role = role  # "Anode", "Cathode", "Separator", "Current_Collector"
        self.thickness_um = thickness_um  # Mikron cinsinden katman kalınlığı

    def check_electrochemical_suitability(self) -> Dict[str, Any]:
        """Malzemenin atandığı rol için elektrokimyasal ve fiziksel uygunluğunu denetler."""
        conductivity = getattr(self.material, 'electrical_conductivity', 0.0)
        density = self.material.density
        
        is_suitable = True
        reason = "Malzeme özellikleri bileşen kriterlerini karşılıyor."

        if self.role == "Anode":
            if density > 5000.0:
                is_suitable = False
                reason = "Anot malzemesi çok ağır, hücre gravimetrik enerji yoğunluğunu düşürür."
        
        elif self.role == "Cathode":
            # Katot aktif malzemesi testleri (Alaşım veya belirli elementler)
            if isinstance(self.material, Element) and self.material.symbol == "Al":
                is_suitable = False
                reason = "Saf alüminyum doğrudan katot aktif malzemesi olmaya uygun değildir."

        elif self.role == "Current_Collector":
            if conductivity < 1e7:
                is_suitable = False
                reason = "Elektriksel iletkenlik akım toplayıcı şasi için yetersiz."

        return {"Role": self.role, "Suitable": is_suitable, "Reason": reason}


class BatteryCell:
    """
    Seçilen bileşenleri, plaka geometrisini ve güvenlik kriterlerini
    bir araya getiren nihai Dijital İkiz Hücre sınıfı.
    """
    def __init__(self, name: str, anode: BatteryComponent, cathode: BatteryComponent, width_mm: float, height_mm: float):
        self.name = name
        self.anode = anode
        self.cathode = cathode
        self.width_mm = width_mm      # Plaka genişliği (mm)
        self.height_mm = height_mm    # Plaka yüksekliği (mm)
        
    def calculate_cell_geometry(self) -> Dict[str, Any]:
        """Katman kalınlıklarından toplam plaka alanını ve teorik kütleyi hesaplar."""
        # Tek bir çift katmanın toplam kalınlığı (metre cinsinden)
        total_thickness_m = (self.anode.thickness_um + self.cathode.thickness_um) * 1e-6
        plate_area_m2 = (self.width_mm * 1e-3) * (self.height_mm * 1e-3)
        
        # Hacimsel kütle hesabı
        anode_mass = self.anode.material.density * (plate_area_m2 * (self.anode.thickness_um * 1e-6))
        cathode_mass = self.cathode.material.density * (plate_area_m2 * (self.cathode.thickness_um * 1e-6))
        total_mass_kg = anode_mass + cathode_mass
        
        return {
            "Plaka Alanı (m2)": round(plate_area_m2, 6),
            "Teorik Hücre Kütlesi (kg)": round(total_mass_kg, 4),
            "Anot Kütlesi (kg)": round(anode_mass, 4),
            "Katot Kütlesi (kg)": round(cathode_mass, 4)
        }

    def run_safety_and_geometry_check(self) -> Dict[str, Any]:
        """Hücrenin geometrik ve kimyasal güvenlik bariyerlerini denetler."""
        anode_check = self.anode.check_electrochemical_suitability()
        cathode_check = self.cathode.check_electrochemical_suitability()
        
        geo_data = self.calculate_cell_geometry()
        is_safe = anode_check["Suitable"] and cathode_check["Suitable"]
        
        return {
            "Hücre Adı": self.name,
            "Geometri": geo_data,
            "Hücre Güvenlik/Uyum Onayı": "ONAYLANDI" if is_safe else "REDDEDİLDİ",
            "Anot Durumu": anode_check["Reason"],
            "Katot Durumu": cathode_check["Reason"]
        }