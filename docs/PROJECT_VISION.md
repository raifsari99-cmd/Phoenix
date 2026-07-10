# PHOENIX: EVRENSEL OPTİMİZASYON VE KEŞİF SİMÜLATÖRÜ
## MÜHENDİSLİK MANİFESTOSU VE PROJE ANAYASASI (v2.0)

## 00. VİZYON, MİSYON VE AMAC
Phoenix; fizik, kimya, termodinamik, akışkanlar mekaniği ve yapay zekanın kesişim noktasında duran evrensel bir keşif ve parametrik optimizasyon platformudur. Temel amacı, bilinen fiziksel yasalar çerçevesinde mevcut enerji depolama ve malzeme sistemlerini (Digital Twin) yüksek doğrulukla simüle etmek; bu kurallar dahlinde insanın ömrü boyunca aklına gelemeyecek trilyonlarca kombinasyonu tarayarak geleceğin teknolojilerini (Battery Discovery Engine) keşfetmektir.

## 01. PHOENIX ALTIN KURALLARI VE GELİŞTİRME FELSEFESİ
* **Amaca Bağlılık:** Yazılan her dosyanın, klasörün ve kod satırının net bir bilimsel veya mimari amacı olacaktır. "Belki lazım olur" mantığıyla tek bir satır kod eklenmeyecektir.
* **Bilimsel Hassasiyet:** Sistem içindeki tüm matematiksel ve fiziksel hesaplamalarda kesin olarak SI Birim Sistemi (Mesafe: metre, Kütle: kg, Sıcaklık: Kelvin) kullanılacak, kullanıcı arayüzünde (Phoenix Studio) lokal dönüşümler yapılacaktır.
* **Modüler Sürdürülebilirlik:** Çekirdek (Core) yapı asla değiştirilmeden, eklentiler (Plugin) ve yeni modüller vasıtasıyla platform 10 yıllık gelişim planı boyunca kesintisiz büyütülebilecek şekilde tasarlanacaktır.

## 02. SİSTEM MİMARİSİ VE MODÜLER KATMANLAR (01 - 20)

### 2.1. Altyapı ve Yazılım Çatısı (Modüller 01 - 03)
* **PHOENIX 01 — Geliştirme Ortamı:** VS Code, Python (3.14.3+), Git ve izole Sanal Ortam (.venv) entegrasyonu.
* **PHOENIX 02 — Yazılım Mimarisi:** Katmanlı, modüler, bağımlılıkları yönetilmiş plugin/paket mantığı ve PascalCase/snake_case kod standartları.
* **PHOENIX 03 — Bilimsel Standartlar:** SI birimleri, fizik sabitleri, hata payı yönetimi ve bilimsel kaynak kalibrasyonları.

### 2.2. Dijital Evren ve Fiziksel Çekirdek (Modüller 04 - 07)
* **PHOENIX 04 — Evrensel Veri Modeli:** Projenin kalbi olan Element, Alaşım, Gaz, Elektrolit, Nanomalzeme ve Kompozit özellikleri barındıran evrensel `Material` sistemi.
* **PHOENIX 05 & 06 — Fizik & Kimya Motorları:** Elektron akışı, iyon difüzyonu, termodinamik, ısı transferi, çoklu fizik (multiphysics) ile oksidasyon, redüksiyon ve dendrit bozulma reaksiyonları.
* **PHOENIX 07 — Geometri Motoru:** Hücre/elektrot geometrileri, mesh (örgü) yapısı, parametrik tasarım ve topoloji optimizasyonu (Trimesh entegrasyonu).

### 2.3. Simülasyon, Doğrulama ve Arayüz (Modüller 08 - 13)
* **PHOENIX 08 & 09 — Dijital İkiz ve Hazır Şablonlar:** Anot, katot, separatör ve BMS modelleri ile Li-Ion, Li-Air, Al-Air, Solid-State gibi hazır batarya/yakıt hücresi tarifleri.
* **PHOENIX 10 & 11 — Simülasyon Motoru & Validation:** Şarj, deşarj, termal test ve yaşlanma senaryolarının gerçek laboratuvar verileriyle karşılaştırılıp Güven Skoru (Confidence Score) üretilmesi.
* **PHOENIX 12 & 13 — Visualization & Phoenix Studio:** PyVista tabanlı gerçek zamanlı 3B iyon/ısı haritalama editörü ve masaüstü kontrol paneli (PyQt6).

### 2.4. Keşif, Akıllı Eleme ve Optimizasyon (Modüller 14 - 16)
* **PHOENIX 14 — Battery Discovery Engine:** Batarya DNA dizilimleri oluşturarak tasarım uzayında kombinasyonlar üreten ana keşif motoru.
* **PHOENIX 19 — Scientific Decision Engine (Bilimsel Karar Motoru):** Keşif motoru ile simülasyon arasında filtre görevi gören; fiziksel/kimyasal olarak imkansız, aşırı pahalı, güvensiz veya üretilemez kombinasyonları simülasyona gitmeden önce eleyen akıllı süzgeç katmanı.
* **PHOENIX 15 & 16 — Yapay Zekâ & Optimizasyon:** Makine öğrenmesi, aktif öğrenme (Active Learning), Pareto analizi, Genetik ve Bayesian algoritmalarıyla parametre tarama.

### 2.5. Gelecek Vizyonu ve Genişleme (Modüller 17 - 20)
* **PHOENIX 17 — Evrensel Araştırma Platformu:** Yakıt hücreleri, süperkapasitörler, hidrojen sistemleri ve yeni alaşım keşifleri.
* **PHOENIX 18, 20 — Gelecek ve 10 Yıllık Plan:** Robotik deney laboratuvarı entegrasyonu, otomatik literatür tarama, Materials Project API ve bulut tabanlı dağıtık simülasyon sistemleri.