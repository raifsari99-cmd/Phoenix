"""
PHOENIX 03 — Bilimsel Standartlar Modülü
Proje genelinde kullanılacak evrensel fiziksel sabitler ve SI birim dönüşüm motoru.
Geliştirme Standartları: Birimler kesinlikle SI (m, kg, s, K, A, mol) tabanlıdır.
"""

import math

# --- EVRENSEL FİZİKSEL VE KİMYASAL SABİTLER (SI BİRİMLERİNDE) ---
R_GAS_CONSTANT = 8.314462618  # İdeal Gaz Sabiti [J / (mol*K)]
F_FARADAY = 96485.33212      # Faraday Sabiti [C / mol]
N_AVOGADRO = 6.02214076e23    # Avogadro Sayısı [1 / mol]
K_BOLTZMANN = 1.380649e-23    # Boltzmann Sabiti [J / K]
E_CHARGE = 1.602176634e-19    # Elementer Elektron Yükü [C]
T_ABSOLUTE_ZERO = 273.15      # Celsius - Kelvin dönüşüm sabiti

class UnitConverter:
    """SI Birim dönüşümlerini güvenli ve hassas şekilde yapan motor sınıfı."""
    
    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Santigrat dereceyi Kelvin'e dönüştürür."""
        return celsius + T_ABSOLUTE_ZERO

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Kelvin'i Santigrat dereceye dönüştürür."""
        return kelvin - T_ABSOLUTE_ZERO

    @staticmethod
    def mm_to_meter(mm: float) -> float:
        """Milimetreyi metreye dönüştürür (Geometri motoru girdileri için)."""
        return mm / 1000.0

    @staticmethod
    def meter_to_mm(meter: float) -> float:
        """Metreyi milimetreyi dönüştürür."""
        return meter * 1000.0

    @staticmethod
    def mah_to_coulomb(mah: float) -> float:
        """Miliamper-saat (mAh) değerini Coulomb (C) yük birimine dönüştürür."""
        # 1 mAh = 0.001 A * 3600 s = 3.6 Coulomb
        return mah * 3.6

    @staticmethod
    def coulomb_to_mah(coulomb: float) -> float:
        """Coulomb yük birimini miliamper-saat (mAh) değerine dönüştürür."""
        return coulomb / 3.6