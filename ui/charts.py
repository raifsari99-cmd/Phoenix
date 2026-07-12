"""
PHOENIX STUDIO — Advanced Electrochemical Simulation & Charting UI
Anot, katot ve katalizör verimlilik eğrilerini canlı olarak çizen grafik motoru.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class ElectrochemicalAnalysisDialog(QDialog):
    def __init__(self, formula_str, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"🔬 Elektrokimyasal Spektrum ve Kararlılık Analizi — {formula_str}")
        self.resize(800, 600)
        
        # Layout kurulumu
        layout = QVBoxLayout(self)
        
        # Bilgi başlığı
        info_label = QLabel(
            f"<b>Formül Matrisi:</b> {formula_str} | "
            f"<b>Teorik Rol:</b> {data['role']} | "
            f"<b>Katalizör Verimi:</b> {data['efficiency']}"
        )
        info_label.setStyleSheet("font-size: 11pt; color: #f8fafc; padding: 5px;")
        layout.addWidget(info_label)
        
        # Matplotlib Figür ve Canvas kurulumu
        self.figure, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        self.figure.patch.set_facecolor('#0f172a') # Koyu arka plan
        
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        # Grafikleri çiz
        self.plot_electrochemical_curves(data)
        
        # Kapatma butonu
        btn_layout = QHBoxLayout()
        close_btn = QPushButton("Analizi Kapat")
        close_btn.setStyleSheet("background-color: #ef4444; color: white; font-weight: bold; padding: 6px;")
        close_btn.clicked.connect(self.accept)
        btn_layout.addStretch()
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)

    def plot_electrochemical_curves(self, data):
        # Grafik 1: Akım-Potansiyel (Tafel) Eğrisi (Anot/Katot Kinetiği)
        self.ax1.set_facecolor('#1e293b')
        voltage = np.linspace(-3.5, 2.0, 200)
        
        # Formüldeki potansiyel ağırlığına göre akım cevabı simülasyonu
        v_offset = data['potential']
        current = np.sinh(voltage - v_offset) + np.random.normal(0, 0.05, 200)
        
        self.ax1.plot(voltage, current, color='#38bdf8', linewidth=2, label='Voltametri Eğrisi')
        self.ax1.axvline(v_offset, color='#f59e0b', linestyle='--', label=f'Hücre Potansiyeli ({v_offset}V)')
        
        self.ax1.set_title("Polarizasyon & Akım Kinetiği", color='white', fontsize=10)
        self.ax1.set_xlabel("Potansiyel (V vs. SHE)", color='white')
        self.ax1.set_ylabel("Akım Yoğunluğu (A/cm²)", color='white')
        self.ax1.tick_params(colors='white')
        self.ax1.grid(True, color='#334155', linestyle=':')
        self.ax1.legend(facecolor='#0f172a', labelcolor='white')

        # Grafik 2: Katalizör Aktivasyon Enerjisi Bariyeri
        self.ax2.set_facecolor('#1e293b')
        reaction_coordinate = np.linspace(0, 1, 100)
        
        # Katalizör verimliliğine göre aktivasyon enerjisi düşüşü
        eff_val = float(data['efficiency'].replace('%', '')) / 100.0
        base_barrier = 2.5
        lowered_barrier = base_barrier * (1 - eff_val * 0.4)
        
        # Reaksiyon yolları
        path_without_cat = np.sin(reaction_coordinate * np.pi) * base_barrier
        path_with_cat = np.sin(reaction_coordinate * np.pi) * lowered_barrier
        
        self.ax2.plot(reaction_coordinate, path_without_cat, color='#94a3b8', linestyle='--', label='Katalizörsüz')
        self.ax2.plot(reaction_coordinate, path_with_cat, color='#10b981', linewidth=2.5, label='Phoenix Katalizör Reaksiyonu')
        
        self.ax2.set_title("Katalizör Aktivasyon Enerjisi", color='white', fontsize=10)
        self.ax2.set_xlabel("Reaksiyon Koordinatı", color='white')
        self.ax2.set_ylabel("Serbest Enerji (eV)", color='white')
        self.ax2.tick_params(colors='white')
        self.ax2.grid(True, color='#334155', linestyle=':')
        self.ax2.legend(facecolor='#0f172a', labelcolor='white')
        
        self.figure.tight_layout()
        self.canvas.draw()