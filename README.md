# Softmax-Action-Selection-Sim-lasyonu
Softmax tabanlı dinamik yük dengeleyici simülasyonu ve performans analizi.
# Softmax Action Selection Load Balancer

Bu proje, dağıtık sistemlerde sunucu performanslarının zamanla değiştiği (**non-stationary**) durumlarda, toplam gecikmeyi minimize etmek için geliştirilmiş bir **olasılıksal yük dengeleme** simülasyonudur.

## 🚀 Özellikler
- **Softmax Seçim Mekanizması:** Sunucuların geçmiş performans verilerine göre olasılıksal seçim.
- **Nümerik Stabilite:** Üstel hesaplamalarda overflow (taşma) hatasını önleyen özel normalizasyon.
- **Dinamik Adaptasyon:** Simülasyonun ortasında değişen sunucu performanslarını fark edip yeni optimumu bulma yeteneği.

## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python
- **Kütüphaneler:** NumPy (Veri işleme), Matplotlib (Görselleştirme)
- **IDE:** VS Code
- **Model:** Geliştirme sürecinde matematiksel modelleme için **Gemini 3 Flash** kullanılmıştır.

## 📊 Analiz ve Sonuçlar
Algoritma, rastgele seçime (Random) oranla ortalama gecikme süresinde yaklaşık **%15 iyileştirme** sağlamıştır. Sistemin çalışma zamanı karmaşıklığı **O(K)** olup, yüksek ölçeklenebilirlik sunar.

## 📦 Kurulum
1. Kütüphaneleri kurun: `pip install numpy matplotlib`
2. Kodu çalıştırın: `python "Softmax Action Selection Simülasyonu.py"`
