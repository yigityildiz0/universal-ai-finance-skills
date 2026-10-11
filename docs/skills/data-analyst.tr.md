# data-analyst

[English](data-analyst.en.md) · [Türkçe](data-analyst.tr.md) · [Library](../../README.tr.md)

**Veriyi birim, eksik değer, varsayım ve belirsizlikleri açık tutarak analiz eder.**

## Örnek istek

> Bu veri kümesini incele; örneklemin hangi sonuçları desteklediğini açıkla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Structured data work: exploratory and statistical analysis, data quality, SQL queries, metric definitions and data dictionaries, dashboards and KPI views, chart selection and chart review. Turkish triggers: veriyi analiz et, tabloyu incele, istatistik, SQL yaz/düzelt, dashboard yap, grafik seç, KPI, veri temizle. More triggers: KPI panosu, karar odaklı raporlama, veri sözlüğü, metrik tanımı.

</details>

## Çalışma mantığı

Şema ve kaliteyi inceler; uygun yöntemi seçer; hesaplar/görselleştirir; gözlem ile yorumu ayırır.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/data-analyst/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [data-analysis](../../skills/common/data-analyst/modules/data-analysis/MODULE.md) | Perform defensible exploratory, descriptive, statistical, or diagnostic analysis on structured data. Use for analyze data, investigate a metric, statistics, data quality, trends, c |
| [data-context](../../skills/common/data-analyst/modules/data-context/MODULE.md) | Create or repair a durable data context containing schema, grain, metric definitions, lineage, ownership, freshness, and quality caveats. Use for data dictionary, metric definition |
| [data-dashboard](../../skills/common/data-analyst/modules/data-dashboard/MODULE.md) | Plan, build, review, or improve a decision-focused dashboard with metric definitions, owners, filters, freshness, alerts, and validation. Use for dashboard, KPI dashboard, analytic |
| [data-visualization-playbook](../../skills/common/data-analyst/modules/data-visualization-playbook/MODULE.md) | Apply a concise decision-focused playbook to design, implement, critique, or validate charts with correct encodings, annotations, accessibility, and source context. Use when the us |
| [sql-analytics-workflow](../../skills/common/data-analyst/modules/sql-analytics-workflow/MODULE.md) | Design, review, debug, or explain analytical SQL with correct grain, joins, filters, time logic, performance awareness, and validation. Use for SQL analysis, writing or debugging a |
