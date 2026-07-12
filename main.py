"""
PHOENIX STUDIO — Enhanced Control Center
Gelişmiş raporlama, rol tahmini (Anot/Katot) ve borsa entegrasyon altyapılı son rötuş.
"""

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QTextEdit, 
                             QLineEdit, QGroupBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from core.optimization import BatteryOptimizationEngine
from ai.predictor import BatteryAIPredictor
from core.reporter import ScientificDecisionEngine

class PhoenixStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHOENIX STUDIO - Endüstriyel Elektrokimya & Keşif Laboratuvarı")
        self.setGeometry(100, 100, 950, 750)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        title_label = QLabel("⚡ PHOENIX ADANCED SIMULATION CORE v1.1")
        title_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Giriş Paneli
        input_group = QGroupBox("🧬 Elementer Uzay ve Borsa Entegrasyonu")
        input_layout = QHBoxLayout()
        
        input_layout.addWidget(QLabel("Element Seti:"))
        self.element_input = QLineEdit("Li, Ni, Mn")
        self.element_input.setStyleSheet("padding: 5px; font-size: 11pt;")
        input_layout.addWidget(self.element_input)
        
        self.run_btn = QPushButton("⚙️ MATRİS VE EVRİMİ TETİKLE")
        self.run_btn.setStyleSheet("background-color: #059669; color: white; font-weight: bold; padding: 6px;")
        self.run_btn.clicked.connect(self.execute_advanced_simulation)
        input_layout.addWidget(self.run_btn)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # Çıktı Paneli
        output_group = QGroupBox("🔬 Ar-Ge Karar ve Rol Optimizasyonu Raporu")
        output_layout = QVBoxLayout()
        
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFont(QFont("Consolas", 10))
        self.console_output.setStyleSheet("background-color: #0f172a; color: #10b981; padding: 12px;")
        output_layout.addWidget(self.console_output)
        
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        self.statusBar().showMessage("Masaüstü laboratuvarı hazır. Kalibrasyon datası aktif.")

    def execute_advanced_simulation(self):
        self.console_output.clear()
        raw_elements = self.element_input.text()
        elements = [el.strip() for el in raw_elements.split(",") if el.strip()]
        
        if not elements:
            return

        self.console_output.append("🔍 [LME INFO] Küresel maden borsası indeksleri simüle ediliyor...")
        self.console_output.append("🧬 [GENETIC CORE] Evrimsel algoritmalar çapraz popülasyon oluşturuyor...\n")
        
        opt_results = BatteryOptimizationEngine.run_genetic_optimization(elements, generations=3, pop_size=8)
        champion_dna = opt_results["En Optimize DNA"]
        formula_str = "".join([f"{el}({share})" for el, share in champion_dna.items()])
        
        ai_report = BatteryAIPredictor.predict_material_properties(champion_dna)
        econ_report = ScientificDecisionEngine.evaluate_candidate(champion_dna)
        
        # Gelecekte kuracağımız Rol ve Katalizör mekanizmasının ilk mantıksal prototipi
        ni_share = champion_dna.get("Ni", 0.0)
        li_share = champion_dna.get("Li", 0.0)
        
        if ni_share > 0.5:
            predicted_role = "KATOT (Yüksek Enerji Yoğunluklu İnterkalasyon Malzemesi)"
            catalyst_efficiency = "%88.5 (Nikel faz kararlılığı yüksek)"
        elif li_share > 0.6:
            predicted_role = "ANOT / KATALİZÖR (Hızlı İyon Transfer Arayüzü)"
            catalyst_efficiency = "%92.1 (Yüksek reaktivite katsayısı)"
        else:
            predicted_role = "DENGELİ MATRİS / KATALİZÖR DESTEK YAPISI"
            catalyst_efficiency = "%75.0 (Standart difüzyon hızı)"

        self.console_output.append("👑 ================= NİHAİ AR-GE ANALİZ RAPORU =================")
        self.console_output.append(f"🏆 Önerilen Optimize Formül : {formula_str}")
        self.console_output.append(f"🎯 Hedef Elektrokimyasal Rol: {predicted_role}")
        self.console_output.append(f"⚡ Tahmini Katalizör Verimi  : {catalyst_efficiency}")
        self.console_output.append("---")
        self.console_output.append(f"🔋 AI Enerji Yoğunluğu      : {ai_report['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
        self.console_output.append(f"🔄 AI Tahmini Çevrim Ömrü   : {ai_report['Tahmini Çevrim Ömrü (Cycle Life)']} Döngü")
        self.console_output.append(f"💰 Simüle Edilen Maliyet    : {econ_report['Hammadde Maliyet Endeksi ($/Ton)']} $/Ton")
        self.console_output.append("==================================================================")
        
        self.statusBar().showMessage("Raporlama tamamlandı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    studio = PhoenixStudio()
    studio.show()
    sys.exit(app.exec())