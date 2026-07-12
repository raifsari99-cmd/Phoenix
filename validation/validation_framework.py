"""
PHOENIX 11 — Validation Framework
Simülasyon sonuçlarının gerçek literatür/laboratuvar verileriyle 
kıyaslanması ve Güven Skoru (Confidence Score) üretimi.
"""

from typing import Dict, Any

class ValidationFramework:
    """Simülasyon çıktılarını gerçek laboratuvar test referanslarıyla kıyaslar."""

    LAB_REFERENCE_DATA = {
        "1C": {
            "max_temp_c": 26.8,
            "final_voltage_v": 2.90
        },
        "3C": {
            "max_temp_c": 43.5,
            "final_voltage_v": 2.75
        }
    }

    @staticmethod
    def validate_scenario(
        c_rate_str: str, 
        sim_max_temp: float, 
        sim_final_voltage: float
    ) -> Dict[str, Any]:
        
        if c_rate_str not in ValidationFramework.LAB_REFERENCE_DATA:
            return {"Hata": "Bu C-rate için laboratuvar referans verisi bulunamadı."}

        ref = ValidationFramework.LAB_REFERENCE_DATA[c_rate_str]
        
        temp_error = abs(sim_max_temp - ref["max_temp_c"])
        voltage_error = abs(sim_final_voltage - ref["final_voltage_v"])

        # 100 puan üzerinden ceza puanı algoritması
        penalty = (temp_error * 10.0) + (voltage_error * 150.0)
        confidence_score = max(100.0 - penalty, 0.0)

        if confidence_score >= 90.0:
            status = "YÜKSEK DOĞRULUK (Simülasyon laboratuvarla tam uyumlu)"
        elif confidence_score >= 70.0:
            status = "KABUL EDİLEBİLİR (Hafif kalibrasyon gerekebilir)"
        else:
            status = "DÜŞÜK DOĞRULUK (Fizik motoru parametreleri revize edilmeli)"

        return {
            "Laboratuvar Ref Sıcaklık (°C)": ref["max_temp_c"],
            "Simülasyon Sıcaklık Sapması (°C)": round(temp_error, 2),
            "Laboratuvar Ref Voltaj (V)": ref["final_voltage_v"],
            "Simülasyon Voltaj Sapması (V)": round(voltage_error, 3),
            "GÜVEN SKORU (%)": round(confidence_score, 2),
            "Doğrulama Durumu": status
        }