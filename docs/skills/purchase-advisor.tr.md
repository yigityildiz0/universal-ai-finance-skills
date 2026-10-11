# purchase-advisor

[English](purchase-advisor.en.md) · [Türkçe](purchase-advisor.tr.md) · [Library](../../README.tr.md)

**Reklam sıralaması yerine ürün uygunluğunu, kanıtı ve gerçek toplam maliyeti karşılaştırır.**

## Örnek istek

> Bu iki ürünü gerçek kullanımım ve bütçem için karşılaştır.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Purchase and price-value advisor for products, services and subscriptions: current dated price checks, total cost, alternatives and cheaper equivalents, value-for-money verdicts, and evidence checks for health products such as supplements, creams, braces, tapes, massagers, TENS/EMS devices and rehab aids (ingredients, regulatory status, SGK). Turkish triggers: alayım mı, fiyatı iyi mi, almaya değer mi, muadili var mı, en ucuz/kaliteli hangisi, işe yarar mı, 10 üzerinden kaç, zararlı mı. More triggers: SGK karşılıyor mu, reçeteli mi, fiyat-performans.

</details>

## Çalışma mantığı

Kesin model/pazarı belirler; öncelikleri çıkarır; özellikleri ve bağımsız kanıtı doğrular; toplam maliyet ve ödünleşimleri karşılaştırır.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/purchase-advisor/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [health-product-evidence-check](../../skills/common/purchase-advisor/modules/health-product-evidence-check/MODULE.md) | Automatically evaluate a health-related product, medicine-like item, supplement, cream/gel, brace, tape, massager, electrotherapy device, wearable, exercise/rehabilitation aid, or  |
| [market-pricing-analysis](../../skills/common/purchase-advisor/modules/market-pricing-analysis/MODULE.md) | Automatically analyze product, service, subscription, marketplace, or competitor pricing when the user asks "fiyatı iyi mi", "almaya değer mi", "en ucuz/kaliteli hangisi", "muadili |
