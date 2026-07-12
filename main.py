import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QTextEdit, 
                             QLineEdit, QGroupBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from core.optimization import BatteryOptimizationEngine
from ai.predictor import BatteryAIPredictor
from core.market_physics import MarketAndPhysicsCore
from core.elemental_db import QuantumElementalAPI
from ui.charts import ElectrochemicalAnalysisDialog

class PhoenixStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHOENIX STUDIO - Küresel Malzeme Keşif Ağı")
        self.setGeometry(100, 100, 1000, 850)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        title_label = QLabel("🌀 PHOENIX UNIVERSAL UNRESTRICTED CORE v4.0")
        title_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Giriş Paneli
        input_group = QGroupBox("🧬 Sırsız ve Kısıtsız Elementer Giriş (Tüm Periyodik Tablo Aktif)")
        input_layout = QHBoxLayout()
        
        input_layout.addWidget(QLabel("İstediğiniz Elementleri Girin (Örn: Dy, Ir, Pt, Nd, Li, Any):"))
        self.element_input = QLineEdit("Dy, Ir")
        self.element_input.setStyleSheet("padding: 5px; font-size: 11pt;")
        input_layout.addWidget(self.element_input)
        
        self.run_btn = QPushButton("🪐 EVRENSEL TARAMAYI BAŞLAT")
        self.run_btn.setStyleSheet("background-color: #dc2626; color: white; font-weight: bold; padding: 6px;")
        self.run_btn.clicked.connect(self.execute_universal_discovery)
        input_layout.addWidget(self.run_btn)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # Çıktı Paneli
        output_group = QGroupBox("🔬 Materials Project & USGS Kuantum/Jeopolitik Analiz Çıktısı")
        output_layout = QVBoxLayout()
        
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFont(QFont("Consolas", 10))
        self.console_output.setStyleSheet("background-color: #030712; color: #fca5a5; padding: 12px;")
        output_layout.addWidget(self.console_output)
        
        self.view_charts_btn = QPushButton("📊 ELEKTROKİMYASAL REAKSİYON EĞRİLERİNİ AÇ")
        self.view_charts_btn.setEnabled(False)
        self.view_charts_btn.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; padding: 8px;")
        self.view_charts_btn.clicked.connect(self.open_analysis_charts)
        output_layout.addWidget(self.view_charts_btn)
        
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        self.last_sim_data = None
        self.statusBar().showMessage("Sığ kısıtlamalar kaldırıldı. Tüm periyodik tablo API kontrolünde.")

    def execute_universal_discovery(self):
        self.console_output.clear()
        raw_elements = self.element_input.text()
        elements = [el.strip() for el in raw_elements.split(",") if el.strip()]
        
        if not elements:
            return

        self.console_output.append("📡 Canlı Kuantum API bağlantısı kuruluyor... Elementer veriler çekiliyor...\n")
        
        # Artık koda gömülü listeye bakmıyor, her elementi API motoruna gönderiyor!
        for el in elements:
            info = QuantumElementalAPI.query_material_science_api(el)
            self.console_output.append(f"⚛️ Element: {el}")
            self.console_output.append(f"   ├─ Kristal Kafes Yapısı : {info['Kafes_Yapisi']}")
            self.console_output.append(f"   ├─ Kıtlık & Jeopolitik  : {info['Kitlik_Indeksi']}")
            self.console_output.append(f"   └─ İş Fonksiyonu Bariyeri: {info['Is_Fonksiyonu_eV']} eV\n")
            
        self.console_output.append("🧬 [EVRİMSEL MOTOR] Genetik varyasyonlar hesaplanıyor...")
        opt_results = BatteryOptimizationEngine.run_genetic_optimization(elements, generations=3, pop_size=6)
        champion_dna = opt_results["En Optimize DNA"]
        self.formula_str = "".join([f"{el}({share})" for el, share in champion_dna.items()])
        
        ai_report = BatteryAIPredictor.predict_material_properties(champion_dna)
        real_cost = MarketAndPhysicsCore.calculate_market_cost(champion_dna)
        role_report = MarketAndPhysicsCore.determine_electrochemical_role(champion_dna)
        
        # Alaşım fazlarının atomik sırları ve uyuşmazlığı
        phase_secret = QuantumElementalAPI.calculate_phase_coexistence(champion_dna)

        self.last_sim_data = {
            "role": role_report['Önerilen Elektrokimyasal Rol'],
            "efficiency": role_report['Tahmini Reaksiyon/Katalizör Verimi'],
            "potential": role_report['Teorik Hücre Potansiyel Ağırlığı (V)']
        }

        self.console_output.append("\n👑 ================= NİHAİ DİNAMİK AR-GE RAPORU =================")
        self.console_output.append(f"🏆 Keşfedilen Formül         : {self.formula_str}")
        self.console_output.append(f"🎯 Saptanan Elektrokimyasal Rol: {self.last_sim_data['role']}")
        self.console_output.append(f"⚡ Optimize Katalizör Verimi  : {self.last_sim_data['efficiency']}")
        self.console_output.append(f"🔮 Alaşım Fazlarının Sırrı   : {phase_secret}")
        self.console_output.append(f"🔋 AI Tahmini Enerji Yoğunluğu: {ai_report['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
        self.console_output.append(f"💰 İNTERNET TABANLI MALİYET  : {real_cost} $/Ton")
        self.console_output.append("=======================================================================")
        
        self.view_charts_btn.setEnabled(True)
        self.view_charts_btn.setStyleSheet("background-color: #dc2626; color: white; font-weight: bold; padding: 8px;")
        self.statusBar().showMessage("Evrensel keşif tamamlandı.")

    def open_analysis_charts(self):
        if self.last_sim_data:
            dialog = ElectrochemicalAnalysisDialog(self.formula_str, self.last_sim_data, self)
            dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    studio = PhoenixStudio()
    studio.show()
    sys.exit(app.exec())