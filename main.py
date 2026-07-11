from core.geometry import BatteryGeometryEngine

def main():
    print("==========================================================")
    print("       PHOENIX GEOMETRY MESH ENGINE - SOHBET 09           ")
    print("==========================================================\n")

    print("📐 3B Trimesh Geometri Motoru başlatılıyor...")
    
    # 150mm x 100mm boyutlarında bir hücre şablonu
    geo_engine = BatteryGeometryEngine(width_mm=150.0, height_mm=100.0)

    # Parametre ismini tam olarak yazıyoruz: cathode_thick_um=70.0
    mesh_results = geo_engine.generate_electrode_layers(anode_thick_um=50.0, cathode_thick_um=70.0)

    anode_m = mesh_results["Anot 3B Mesh"]
    cathode_m = mesh_results["Katot 3B Mesh"]

    print(f"\n🔬 3B Elektrot Mesh Analiz Çıktıları:")
    print(f"   🟥 ANOT KATMANI (3B):")
    print(f"     └─ Düğüm Noktası (Vertex): {anode_m['Vertex_Count']}")
    print(f"     └─ Üçgen Yüzey (Face): {anode_m['Face_Count']}")
    print(f"     └─ Toplam Yüzey Alanı: {anode_m['Total_Surface_Area_mm2']} mm²")
    
    print(f"   🟦 KATOT KATMANI (3B):")
    print(f"     └─ Düğüm Noktası (Vertex): {cathode_m['Vertex_Count']}")
    print(f"     └─ Üçgen Yüzey (Face): {cathode_m['Face_Count']}")
    print(f"     └─ Toplam Yüzey Alanı: {cathode_m['Total_Surface_Area_mm2']} mm²")

    print(f"\n   ⚙️ Toplam Hücre İçi Düğüm Çözünürlüğü: {mesh_results['Toplam Mesh Düğüm Noktası (Hücre İçi)']} Nokta\n")

    print("==========================================================")
    print("    MESH ENTEGRASYONU TAMAM: SOHBET 09 MÜHÜRLENDİ!       ")
    print("==========================================================")

if __name__ == "__main__":
    main()