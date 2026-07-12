import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QTextEdit, 
                             QLineEdit, QGroupBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from core.optimization import BatteryOptimizationEngine
from ai.predictor import BatteryAIPredictor
from core.market_physics import MarketAndPhysicsCore
from ui.charts import ElectrochemicalAnalysisDialog

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

        title_label = QLabel("⚡ PHOENIX LIVE EXPERIMENT PLATFORM v2.5")
        title_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Giriş Paneli
        input_group = QGroupBox("🧬 Elementer Uzay Kontrol Merkezi")
        input_layout = QHBoxLayout()
        
        input_layout.addWidget(QLabel("Element Seti:"))
        self.element_input = QLineEdit("Li, Ni, Au")
        self.element_input.setStyleSheet("padding: 5px; font-size: 11pt;")
        input_layout.addWidget(self.element_input)
        
        self.run_btn = QPushButton("🚀 ANALİZ VEYA ROL TESPİTİNİ TETİKLE")
        self.run_btn.setStyleSheet("background-color: #2563eb; color: white; font-weight: bold; padding: 6px;")
        self.run_btn.clicked.connect(self.execute_live_simulation)
        input_layout.addWidget(self.run_btn)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # Çıktı Paneli
        output_group = QGroupBox("🔬 Ar-Ge Karar ve Katalizör Raporu")
        output_layout = QVBoxLayout()
        
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFont(QFont("Consolas", 10))
        self.console_output.setStyleSheet("background-color: #0f172a; color: #38bdf8; padding: 12px;")
        output_layout.addWidget(self.console_output)
        
        # YENİ: Grafik Penceresini Açma Butonu (Başlangıçta inaktif)
        self.view_charts_btn = QPushButton("📊 ELEKTROKİMYASAL SPEKTRUM VE GRAFİKLERİ GÖSTER")
        self.view_charts_btn.setEnabled(False)
        self.view_charts_btn.setStyleSheet("background-color: #1e293b; color: #94a3b8; font-weight: bold; padding: 8px;")
        self.view_charts_btn.clicked.connect(self.open_analysis_charts)
        output_layout.addWidget(self.view_charts_btn)
        
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        self.last_sim_data = None
        self.statusBar().showMessage("Sistem hazır. Keşif arayüzü kalibre edildi.")

    def execute_live_simulation(self):
        self.console_output.clear()
        raw_elements = self.element_input.text()
        elements = [el.strip() for el in raw_elements.split(",") if el.strip()]
        
        if not elements:
            return

        self.console_output.append("⚙️ Genetik matris optimize ediliyor...")
        
        opt_results = BatteryOptimizationEngine.run_genetic_optimization(elements, generations=3, pop_size=6)
        champion_dna = opt_results["En Optimize DNA"]
        self.formula_str = "".join([f"{el}({share})" for el, share in champion_dna.items()])
        
        ai_report = BatteryAIPredictor.predict_material_properties(champion_dna)
        real_cost = MarketAndPhysicsCore.calculate_market_cost(champion_dna)
        role_report = MarketAndPhysicsCore.determine_electrochemical_role(champion_dna)

        # Sonuçları grafik ekranına aktarmak üzere önbelleğe alıyoruz
        self.last_sim_data = {
            "role": role_report['Önerilen Elektrokimyasal Rol'],
            "efficiency": role_report['Tahmini Reaksiyon/Katalizör Verimi'],
            "potential": role_report['Teorik Hücre Potansiyel Ağırlığı (V)']
        }

        self.console_output.append("👑 ================= NİHAİ ENDÜSTRİYEL ANALİZ RAPORU =================")
        self.console_output.append(f"🏆 Keşfedilen Formül         : {self.formula_str}")
        self.console_output.append(f"🎯 Saptanan Kimyasal Rol     : {self.last_sim_data['role']}")
        self.console_output.append(f"⚡ Optimize Katalizör Verimi  : {self.last_sim_data['efficiency']}")
        self.console_output.append(f"🔋 AI Enerji Yoğunluğu      : {ai_report['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
        self.console_output.append(f"💰 SİMUEL EDİLEN MALİYET     : {real_cost} $/Ton")
        self.console_output.append("=======================================================================")
        
        # Grafik butonunu aktifleştir ve parlat
        self.view_charts_btn.setEnabled(True)
        self.view_charts_btn.setStyleSheet("background-color: #10b981; color: white; font-weight: bold; padding: 8px;")
        self.statusBar().showMessage("Analiz tamamlandı. Grafikler görüntülenebilir.")

    def open_analysis_charts(self):
        if self.last_sim_data:
            dialog = ElectrochemicalAnalysisDialog(self.formula_str, self.last_sim_data, self)
            dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    studio = PhoenixStudio()
    studio.show()
    sys.exit(app.exec())