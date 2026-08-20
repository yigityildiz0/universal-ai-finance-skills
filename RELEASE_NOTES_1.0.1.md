# Universal AI Finance Skills 1.0.1

Publication and CI verification patch. The 17-skill finance payload and all
three release archives are unchanged from 1.0.0.

- Added the three small host bundles to the tracked repository so a clean
  GitHub Actions checkout can verify every SHA-256 entry.
- Moved the workflow to `actions/setup-python@v6`.
- Re-ran the repository validator and all eight deterministic finance-script
  tests successfully on GitHub Actions.

No skill guarantees returns, places orders, connects to a broker or wallet, or
handles credentials.

---

# Universal AI Finance Skills 1.0.1 — Türkçe

Yayın ve CI doğrulama yaması. 17 finans becerisinin içeriği ve üç host ZIP'i
1.0.0 ile aynıdır.

- Temiz bir GitHub Actions kopyasının bütün SHA-256 kayıtlarını doğrulayabilmesi
  için üç küçük host paketi depoda izlenir hale getirildi.
- İş akışı `actions/setup-python@v6` sürümüne geçirildi.
- Depo doğrulayıcısı ve sekiz deterministik finans betiği testi GitHub
  Actions'ta başarıyla yeniden çalıştırıldı.

Hiçbir beceri getiri garantisi vermez, emir göndermez, aracı kuruma veya
cüzdana bağlanmaz ve kimlik bilgisi işlemez.

