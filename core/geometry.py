"""
PHOENIX 07 — Geometric Trimesh Layer & Hull Design
Batarya hücrelerinin ve paketinin dış gövde (Hull) geometrisini, 
çeper kalınlıklarını ve hacimsel yerleşim sınırlarını hesaplayan modül.
"""

from typing import Dict, Any
from core.material import Material

class BatteryHull:
    """Batarya hücresini veya paketini koruyan dış kabuk (Enclosure) sınıfı."""
    
    def __init__(self, name: str, material: Material, wall_thickness_mm: float, internal_clearance_mm: float):
        self.name = name
        self.material = material                 # Gövde alaşımı (Örn: Phoenix Al-Mg Alaşımı)
        self.wall_thickness_mm = wall_thickness_mm  # Çeper et kalınlığı
        self.internal_clearance_mm = internal_clearance_mm # İçerideki güvenlik boşluğu payı

    def calculate_envelope(self, inner_width_mm: float, inner_height_mm: float, inner_depth_mm: float) -> Dict[str, Any]:
        """
        İçerideki batarya hücresinin net boyutlarına göre, koruyucu gövdenin 
        dış sınır kutusunu (Bounding Box), hacmini ve gövde ağırlığını hesaplar.
        """
        # İç boşluk payını ekliyoruz
        clearance_total = self.internal_clearance_mm * 2
        net_inner_w = inner_width_mm + clearance_total
        net_inner_h = inner_height_mm + clearance_total
        net_inner_d = inner_depth_mm + clearance_total
        
        # İç net hacim (m³ cinsinden)
        inner_volume_m3 = (net_inner_w * 1e-3) * (net_inner_h * 1e-3) * (net_inner_d * 1e-3)

        # Dış boyutlar (Çeper kalınlığı iki taraftan eklenir)
        shell_addition = self.wall_thickness_mm * 2
        outer_width_mm = net_inner_w + shell_addition
        outer_height_mm = net_inner_h + shell_addition
        outer_depth_mm = net_inner_d + shell_addition
        
        # Dış toplam hacim (m³ cinsinden)
        outer_volume_m3 = (outer_width_mm * 1e-3) * (outer_height_mm * 1e-3) * (outer_depth_mm * 1e-3)
        
        # Sadece gövde kabuğunun (katı metalin) kapladığı hacim
        hull_material_volume_m3 = outer_volume_m3 - inner_volume_m3
        
        # Gövdenin kendi ağırlığı (Hacim * Malzeme Yoğunluğu)
        hull_mass_kg = hull_material_volume_m3 * self.material.density
        
        # Hacimsel Verimlilik: İç net hacmin, toplam kaplanan dış hacme oranı
        volumetric_efficiency = (inner_volume_m3 / outer_volume_m3) * 100

        return {
            "Dış Boyutlar (G x Y x D mm)": f"{round(outer_width_mm, 1)} x {round(outer_height_mm, 1)} x {round(outer_depth_mm, 1)}",
            "Toplam Dış Hacim (Litre)": round(outer_volume_m3 * 1000, 3),
            "Koruyucu Gövde Ağırlığı (kg)": round(hull_mass_kg, 4),
            "Hacimsel Paketleme Verimliliği (%)": round(volumetric_efficiency, 2)
        }