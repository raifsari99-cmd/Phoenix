"""
PHOENIX STUDIO — Ultimate UI Control Center
Tüm fizik, kimya, AI ve optimizasyon motorlarını tek bir masaüstü arayüzünde birleştiren ana panel.
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
        self.setWindowTitle("PHOENIX STUDIO - Elektrokimyasal Keşif & Simülasyon Paneli")
        self.setGeometry(100, 100, 900, 700)
        self.init_ui()

    def init_ui(self):
        # Ana Arayüz Düzeni
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Başlık Bölümü
        title_label = QLabel("🔥 PHOENIX STUDIO v1.0")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Üst Panel: Element Girişleri
        input_group = QGroupBox("🧬 Elementer Uzay Ayarları")
        input_layout = QHBoxLayout()
        
        input_layout.addWidget(QLabel("Hedef Elementler (Virgülle ayırın):"))
        self.element_input = QLineEdit("Li, Ni, Mn")
        self.element_input.setStyleSheet("padding: 5px; font-size: 11pt;")
        input_layout.addWidget(self.element_input)
        
        self.run_btn = QPushButton("🚀 KEŞİF & EVRİMİ BAŞLAT")
        self.run_btn.setStyleSheet("background-color: #2563eb; color: white; font-weight: bold; padding: 6px;")
        self.run_btn.clicked.connect(self.execute_optimization)
        input_layout.addWidget(self.run_btn)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # Alt Panel: Sonuç Ekranı ve Raporlama
        output_group = QGroupBox("📊 Canlı Simülasyon ve Bilimsel Karar Çıktıları")
        output_layout = QVBoxLayout()
        
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFont(QFont("Courier New", 10))
        self.console_output.setStyleSheet("background-color: #0f172a; color: #38bdf8; padding: 10px;")
        output_layout.addWidget(self.console_output)
        
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        # Durum Çubuğu
        self.statusBar().showMessage("Sistem Hazır. Baş Mühendis Raif komutu bekleniyor...")

    def execute_optimization(self):
        self.console_output.clear()
        self.statusBar().showMessage("Evrimsel optimizasyon ve AI süzgeci çalıştırılıyor...")
        
        # Kullanıcının arayüze yazdığı elementleri dinamik olarak alıyoruz (Artık kısıtlama bitti!)
        raw_elements = self.element_input.text()
        elements = [el.strip() for el in raw_elements.split(",") if el.strip()]
        
        if not elements:
            self.console_output.append("❌ Hata: Lütfen geçerli element simgeleri girin.")
            return

        self.console_output.append(f"🔮 DİNAMİK ARAMA BAŞLATILDI: Giriş kümesi {elements} taranıyor...\n")
        
        # 1. Genetik Algoritma Motorunu tetikleme
        opt_results = BatteryOptimizationEngine.run_genetic_optimization(
            elements=elements, generations=5, pop_size=10
        )
        
        champion_dna = opt_results["En Optimize DNA"]
        formula_str = "".join([f"{el}({share})" for el, share in champion_dna.items()])
        
        # 2. AI ve Ekonomik Süzgeç Sonuçları
        ai_report = BatteryAIPredictor.predict_material_properties(champion_dna)
        econ_report = ScientificDecisionEngine.evaluate_candidate(champion_dna)
        
        # 3. Sonuçları Arayüze Canlı Basma
        self.console_output.append("👑 ================= EVRİMSEL ARAMA ŞAMPİYONU =================")
        self.console_output.append(f"🏆 Optimize Batarya DNA'sı: {formula_str}")
        self.console_output.append(f"🎯 Birleşik Skor Derecesi : {opt_results['En Yüksek Birleşik Skor']}")
        self.console_output.append(f"🔋 AI Enerji Yoğunluğu    : {ai_report['Tahmini Enerji Yoğunluğu (Wh/kg)']} Wh/kg")
        self.console_output.append(f"🔄 AI Tahmini Çevrim Ömrü : {ai_report['Tahmini Çevrim Ömrü (Cycle Life)']} Döngü")
        self.console_output.append(f"💰 Hammadde Maliyeti     : {econ_report['Hammadde Maliyet Endeksi ($/Ton)']} $/Ton")
        self.console_output.append(f"🛠️ Üretilebilirlik Endeksi: %{econ_report['Üretilebilirlik Skoru (%)']}")
        self.console_output.append("==================================================================")
        
        self.statusBar().showMessage("Simülasyon mühürlendi ve arayüze aktarıldı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    studio = PhoenixStudio()
    studio.show()
    sys.exit(app.exec())