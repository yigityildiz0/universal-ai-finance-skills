# Universal AI Finance Skills

> **New — version 2:** a single routed copilot with a live BIST data engine, investment committee and trade planning now lives at [yigit-investment-copilot](https://github.com/yigityildiz0/yigit-investment-copilot). This repository stays available as v1 (17 separate skills).

Seventeen bilingual, portable Agent Skills for evidence-based investing, financial literacy, BIST/TEFAS, warrants, funds, public equities, crypto research, portfolio risk, and calibrated forecasting.

This library is designed to make an AI assistant a more disciplined research and decision partner—not an oracle. It can rank candidates and give a conditional action, but every forecast must carry an evidence cutoff, horizon, range or probability, counter-thesis, risk limit, and invalidation rule. No skill guarantees returns, executes trades autonomously, or handles brokerage credentials.

## Download

| Host | Ready bundle | Install root |
|---|---|---|
| ChatGPT / Codex | [Latest release ZIP](https://github.com/yigityildiz0/universal-ai-finance-skills/releases/latest/download/universal-ai-finance-skills-chatgpt-codex.zip) | `~/.agents/skills/` |
| OpenCode | [Latest release ZIP](https://github.com/yigityildiz0/universal-ai-finance-skills/releases/latest/download/universal-ai-finance-skills-opencode.zip) | `~/.config/opencode/skills/` |
| Claude Code | [Latest release ZIP](https://github.com/yigityildiz0/universal-ai-finance-skills/releases/latest/download/universal-ai-finance-skills-claude-code.zip) | `~/.claude/skills/` |

ChatGPT/Codex is the primary package. OpenCode is the secondary package. Claude Code is published for portability and is not required for local use.

## Decision pipeline

1. Freeze the instrument identity, market, currency, horizon, and evidence cutoff.
2. Gather current primary data and pass it through `finance-evidence-guard`.
3. Use the product owner: equity, fund/ETF, warrant, Turkey market, technical/quant, regime, or read-only crypto.
4. Produce bear/base/bull cases or scored probabilities—not a single magical target.
5. Run `investment-red-team`, portfolio sizing, and `pre-trade-investment-gate`.
6. Record the thesis and forecast before the outcome; score it later and review the journal.

## Skills

| Skill | What it does |
|---|---|
| [`crypto-research-readonly`](skills/common/crypto-research-readonly/SKILL.md) | Research crypto assets in a strictly read-only mode using verified network and contract identity, multi-venue price checks, liquidity and derivatives structure, tokenomics and unlocks, treasury and governance, protocol usage, on-chain evidence, smart-contract and custody risks, catalysts, technical context, and bear/base/bull scenarios. Use when the user asks which coin or token to buy, whether to hold or sell crypto, how much it may move, compares exchanges or tokens, or requests crypto market analysis. Never connect a wallet, sign a transaction, trade, transfer, bridge, approve a token, reveal a private key, or automate spending. Turkish triggers: kripto analizi, coin/token alınır mı, kontrat ve tokenomik, cüzdansız salt okunur araştırma. |
| [`equity-opportunity-funnel`](skills/common/equity-opportunity-funnel/SKILL.md) | Search a broad investable stock universe and progressively narrow it into recommendation-grade equity ideas. Use when the user asks which stock to buy, the best or highest-upside stock, stock alternatives, a BIST or global stock scan, many shares to compare, or wants a prior stock recommendation rechecked before acting. Automatically deepen a simple “hisse öner” request through universe construction, multi-factor screening, medium diligence, full fundamental/valuation/technical/catalyst analysis, probabilistic forecasting, independent red-team review, failed-candidate replacement, and recommendation consistency tracking. Do not use for a purely descriptive company summary or when the user names a non-equity instrument. |
| [`finance-evidence-guard`](skills/common/finance-evidence-guard/SKILL.md) | Automatically verify financial evidence whenever an answer uses a current price/quote, NAV, filing, fund holding, product term, fee, tax/legal rule, target, catalyst, macro release, analyst estimate, or the user asks “fiyat doğru mu”, “veri eski mi”, “kaynak uydurma mı”, “emin misin”. Resolve identity, source hierarchy, timestamps, units, currencies, calculations, staleness, conflicts, adjustment basis, and unsupported claims; run alongside equity, fund/ETF, warrant, technical, crypto, forecast, regime, portfolio, pre-trade, or thesis work. Treat interested financial content as claims, not proof. Do not replace the underlying analysis. |
| [`financial-literacy-coach`](skills/common/financial-literacy-coach/SKILL.md) | Teach practical financial literacy with transparent calculations and adaptive explanations across budgeting, emergency funds, debt/credit, interest, inflation, compounding, fees, taxes, diversification, risk/return, funds/ETFs, stocks, bonds, derivatives, pensions, insurance, scams, and decision hygiene. Use for “explain finance”, money calculations, learning plans, or Turkish intents such as “finansal okuryazarlık”, “faiz/enflasyon hesabı”, “bileşik getiri”, “fon-hisse-varant farkı”, “kredi maliyeti”, “bütçe yap”, “yatırımı bana öğret”. Verify current local rules; do not turn education into a guaranteed product recommendation. |
| [`fund-etf-analyst`](skills/common/fund-etf-analyst/SKILL.md) | Analyze and compare mutual funds, ETFs, index funds, money-market funds, pension funds, and TEFAS products using exact identity, mandate, benchmark, holdings, look-through overlap, fees/tax, NAV versus market price, liquidity, drawdown, factor exposures, and category-consistent alternatives. Use for fund/ETF buy-hold-sell decisions, portfolio fund selection, “best fund” or “which fund” requests, and Turkish intents such as “fon alınır mı”, “hangi fon daha iyi”, “TEFAS fon karşılaştır”, “ETF mi fon mu”, “fon dağılımı” and “fonu satayım mı”. Do not rank by trailing return alone or treat a fund code as verified identity. |
| [`investment-copilot`](skills/common/investment-copilot/SKILL.md) | Orchestrate evidence-based investment research and decisions across equities, funds/ETFs, BIST/TEFAS, macro regimes, technicals, crypto, futures, warrants, portfolios, sizing, pre-trade checks, thesis tracking, journals, and short- or long-horizon forecasts. Use for buy/hold/add/reduce/sell/compare, “what should I buy”, highest-upside, position-size, reconsideration, or Turkish intents such as “alınır mı”, “ne alayım”, “en çok ne artar”, “sat/tut/artır/azalt”, “ne kadar yükselir/düşer”, “kaç lot/adet”, “portföyümü analiz et”, and “emin misin”. Verify current evidence, quantify ranges, challenge the leader, and give a clear conditional action without guaranteed-return language. Never trade autonomously or handle credentials. |
| [`investment-journal-review`](skills/common/investment-journal-review/SKILL.md) | Review one completed investment/trade or a journal of many decisions while preserving the original plan, separating process quality from profit/loss, testing thesis and forecast accuracy, identifying repeated evidence/sizing/execution errors, and proposing one or two measurable improvements. Use for post-trade reviews, recommendation scorecards, “why did this lose”, “what am I doing wrong”, and Turkish intents such as “işlem günlüğümü analiz et”, “işlem sonrası analiz”, “tahminlerin ne kadar tuttu”, “zararımdan ders çıkar”, “geçmiş al-satları incele”. Do not rewrite the original plan with hindsight or infer a stable edge from a small sample. |
| [`investment-red-team`](skills/common/investment-red-team/SKILL.md) | Independently challenge and audit an investment recommendation, thesis, valuation, portfolio action, technical setup, fund comparison, crypto analysis, or leveraged-product scenario. Use when the user asks "emin misin?", requests a fresh analysis or second opinion, asks whether a better stock, fund, ETF, gold, crypto, cash, or other relevant alternative exists, is considering a concentrated or high-risk trade, or another finance skill delegates final review. Re-underwrite without anchoring to the prior pick, recompute key numbers, seek disconfirming evidence, compare same-asset and relevant cross-asset challengers plus doing nothing, and return an evidence-based verdict. Do not merely defend, restate, or self-score the original analysis, and do not force a different answer just to appear independent. Turkish triggers: yatırım fikrini yeniden sorgula, emin misin, karşı tez ve alternatifler, bağımsız ikinci görüş. |
| [`investment-thesis-tracker`](skills/common/investment-thesis-tracker/SKILL.md) | Create and maintain an append-only investment thesis with original evidence cutoff, what is priced in, falsifiable pillars, KPIs, catalysts, valuation and entry gates, risks, kill/add/trim/exit criteria, review dates, and evidence-delta updates. Use to monitor a holding or prior recommendation, prepare earnings reviews, or for Turkish intents such as “yatırım tezimi kaydet/takip et”, “bu hisseyi bundan sonra izle”, “tez bozuldu mu”, “hangi şartta artır/sat”, “önceki analizle ne değişti”. Separate company quality, security readiness, and portfolio action; never rewrite the original thesis with hindsight. |
| [`market-regime-analysis`](skills/common/market-regime-analysis/SKILL.md) | Classify and explain the current market regime across trend, volatility, breadth, liquidity, rates, inflation, FX, credit, earnings revisions, positioning, correlations, and dated policy/event risk, then map it to asset and strategy sensitivities. Use for macro allocation, risk-on/risk-off, timing context, cross-asset comparisons, or Turkish intents such as “piyasa rejimi”, “risk-on risk-off”, “şu an hangi varlık avantajlı”, “faiz-enflasyon-borsa ilişkisi”, “volatilite ve genişlik”, “makro ortamı analiz et”. A regime label is context, not a standalone buy/sell signal or deterministic forecast. |
| [`portfolio-risk-and-sizing`](skills/common/portfolio-risk-and-sizing/SKILL.md) | Analyze portfolio concentration, position size, issuer/fund look-through overlap, sector/country/currency/rate/factor exposure, liquidity, leverage, correlation fragility, scenario loss, drawdown budget, and add-trim-hedge constraints. Use for portfolio reviews, allocation and rebalancing, “how much should I buy”, concentration or diversification questions, and Turkish intents such as “portföyümü analiz et”, “kaç lot/adet”, “yüzde kaç ayırayım”, “risk dağılımı”, “çok mu yoğunlaştım”, “fonlar çakışıyor mu”. Do not optimize from unstable estimates by default or claim diversification from the number of tickers alone. |
| [`pre-trade-investment-gate`](skills/common/pre-trade-investment-gate/SKILL.md) | Run a final read-only readiness check before an investment or trade across exact identity, evidence cutoff, executable entry, thesis, payoff, catalysts, invalidation, quantity, maximum loss, portfolio fit, liquidity, spread/fees/tax, settlement, expiry/margin, operational risk, and independent challenge. Use when the user is about to act, asks “should I place it now”, “final check”, “is this trade ready”, or Turkish intents such as “son kontrol”, “emri vereyim mi”, “işleme gireyim mi”, “alım için hazır mı”, “bir kez daha kontrol et”. Return READY/CONDITIONAL/NOT READY/REJECT, but never place, transmit, or automate an order. |
| [`probabilistic-market-forecast`](skills/common/probabilistic-market-forecast/SKILL.md) | Estimate realistic price/return distributions, target and downside probabilities, and probability-weighted scenarios for stocks, funds/ETFs, futures, warrants, crypto, commodities, FX, and portfolios; freeze and score forecasts after maturity. Use for how much/when an instrument may rise or fall, highest realistic upside, target odds, or Turkish intents such as ‘ne kadar yükselir/düşer’, ‘kaç günde/ayda’, ‘en çok ne artar’, ‘hedefe ulaşma ihtimali’, ‘ayı-baz-boğa’, ‘olasılıklı fiyat tahmini’, and ‘tahminlerin ne kadar tuttu’. Compare against naive/market benchmarks and calibration; never claim single-point certainty or guaranteed accuracy. |
| [`public-equity-research`](skills/common/public-equity-research/SKILL.md) | Perform recommendation-grade research on a named listed company using exact security identity, point-in-time primary filings, business/segment economics, earnings quality, balance sheet, cash flow, dilution, management/governance, industry/competition, valuation, what is priced in, catalysts, revisions, risks, and falsifiable thesis criteria. Use for company/hisse fundamental analysis, earnings and valuation, or Turkish intents such as “şirketi/hisseyi derin analiz et”, “bilanço ve değerleme”, “adil değer”, “yatırım tezi”, “KAP/10-K sonuçları”, “bu hisse neden alınır/satılır”. For open-ended “which stock” requests, route through the broad equity funnel first; never infer a market-wide winner from one company analysis. |
| [`technical-quant-analysis`](skills/common/technical-quant-analysis/SKILL.md) | Perform evidence-based technical and quantitative analysis from verified OHLCV data, including trend, momentum, volatility, volume, support/resistance, multi-timeframe structure, scenario levels, position risk, strategy testing, and backtest quality control. Use when the user asks for chart analysis, RSI/MACD/ATR, entry or exit timing, short-term price scenarios, stop/invalidation levels, technical screening, or whether a signal historically worked. Do not use technical indicators alone to claim certainty or replace fundamental, event, liquidity, and product-risk analysis. Turkish triggers: teknik ve nicel piyasa analizi, grafik/destek-direnç, OHLCV ve backtest. |
| [`turkey-markets-analysis`](skills/common/turkey-markets-analysis/SKILL.md) | Analyze Turkish financial markets using BIST, KAP, TEFAS, TCMB EVDS, TÜİK, SPK, issuer/fund/product documents, and current Türkiye-specific rules. Use for BIST equities, Turkish ETFs/certificates, TEFAS funds, TRY/FX macro effects, inflation accounting, corporate actions, VİOP, warrants, broker/bank products, or Turkish intents such as “BIST hissesi”, “TEFAS fon”, “varant/VİOP”, “TCMB faiz”, “KAP bilanço”, “TMS 29”. Apply universal fund, warrant, forecast, technical and portfolio specialists where appropriate; own Türkiye sourcing and market mechanics. Do not use for non-Turkish markets except comparison. |
| [`warrant-structured-product-analyst`](skills/common/warrant-structured-product-analyst/SKILL.md) | Analyze listed warrants, certificates, turbos, and related structured products from the official product terms, executable quote, underlying distribution, strike/barrier, expiry, conversion convention, settlement, market maker, spread, liquidity, time decay, implied volatility, Greeks, effective gearing, break-even, and total-loss scenarios. Use for “which warrant”, warrant quantity/return/risk, call-put comparisons, or Turkish intents such as “varant alınır mı”, “hangi varant”, “varant kaç adet”, “dayanak yüzde 10 artarsa varant ne olur”, “kullanım fiyatı/vade/dönüşüm oranı”. Never infer a fixed return from the underlying move or treat indicative model value as an issuer quote. |

## Safety and limitations

- Current price, filings, fund data, product terms, taxes, regulation, spreads, and liquidity must be refreshed at use time.
- Warrants and other leveraged products can lose all invested capital; model value is not an executable quote.
- Backtests and model scores are not live performance. Look-ahead bias, survivorship bias, overfitting, costs, and market impact must be checked.
- The assistant must not place an order, log in to a broker, store secrets, or convert uncertainty into guaranteed-return wording.
- Read [FINANCIAL_SAFETY.md](FINANCIAL_SAFETY.md) and verify release hashes in [manifests/SHA256SUMS.txt](manifests/SHA256SUMS.txt).

## Validation

```bash
python tools/validate_repo.py
python tests/test_finance_scripts.py
```

## Primary references

- [Borsa İstanbul products](https://borsaistanbul.com/piyasalar/pay-piyasasi/urunler)
- [KAP](https://www.kap.org.tr/)
- [TEFAS](https://www.tefas.gov.tr/)
- [SPK investor portal](https://spk.gov.tr/yatirimcilar)
- [OECD financial education](https://www.oecd.org/financial/education/)
- [FINRA on AI-generated investment information](https://www.finra.org/investors/insights/artificial-intelligence-and-investment-fraud)
- [ESMA investor warning on AI](https://www.esma.europa.eu/press-news/esma-news/esma-warns-retail-investors-risks-artificial-intelligence-ai)

---

# Türkçe

Kanıta dayalı yatırım, finansal okuryazarlık, BIST/TEFAS, varant, fon, halka açık şirket, kripto araştırması, portföy riski ve kalibre tahmin için 17 taşınabilir Agent Skill.

Bu paket yapay zekâyı daha disiplinli bir araştırma ve karar ortağı yapar; kâhin yapmaz. Adayları sıralayabilir ve koşullu bir eylem önerebilir; fakat her tahminde veri kesim zamanı, vade, aralık veya olasılık, karşı tez, risk sınırı ve geçersizleşme kuralı bulunur. Hiçbir beceri getiri garantisi vermez, kendiliğinden işlem yapmaz veya aracı kurum parolası işlemez.

## Türkçe beceri özeti

| Skill | Ne işe yarar? |
|---|---|
| [`crypto-research-readonly`](skills/common/crypto-research-readonly/SKILL.md) | Kripto varlıkları piyasa yapısı, token ekonomisi, zincir üstü veri, güvenlik ve likidite riskiyle salt okunur inceler. |
| [`equity-opportunity-funnel`](skills/common/equity-opportunity-funnel/SKILL.md) | Geniş hisse evrenini tarayıp kanıt kalitesine göre en güçlü adaylara indirger. |
| [`finance-evidence-guard`](skills/common/finance-evidence-guard/SKILL.md) | Finansal iddiaları güncel birincil kaynak, tarih, dönem, para birimi ve hesap tutarlılığıyla doğrular. |
| [`financial-literacy-coach`](skills/common/financial-literacy-coach/SKILL.md) | Bütçe, borç, faiz, enflasyon, bileşik getiri, vergi, fon, hisse ve türevleri hesaplarla öğretir. |
| [`fund-etf-analyst`](skills/common/fund-etf-analyst/SKILL.md) | Fon, ETF ve TEFAS ürünlerini strateji, ücret, vergi, portföy, likidite ve riskle karşılaştırır. |
| [`investment-copilot`](skills/common/investment-copilot/SKILL.md) | Hisse, fon, BIST/TEFAS, varant, teknik, makro, kripto, portföy ve tahmin becerilerini tek yatırım kararı akışında koordine eder. |
| [`investment-journal-review`](skills/common/investment-journal-review/SKILL.md) | Yatırım günlüğünü süreç kalitesi, önyargı, kural ihlali, sonuç ve öğrenme ölçümleriyle inceler. |
| [`investment-red-team`](skills/common/investment-red-team/SKILL.md) | Yatırım fikrinin karşı tezini, başarısızlık yollarını ve geçersizleşme koşullarını çıkarır. |
| [`investment-thesis-tracker`](skills/common/investment-thesis-tracker/SKILL.md) | Yatırım tezini kanıt, katalizör, risk, izlenecek ölçüt ve geçersizleşme koşullarıyla sürümleyerek takip eder. |
| [`market-regime-analysis`](skills/common/market-regime-analysis/SKILL.md) | Trend, volatilite, likidite, korelasyon, enflasyon ve büyüme göstergeleriyle piyasa rejimini sınıflandırır. |
| [`portfolio-risk-and-sizing`](skills/common/portfolio-risk-and-sizing/SKILL.md) | Portföy yoğunlaşması, korelasyon, risk bütçesi, senaryo kaybı ve pozisyon boyutunu hesaplar. |
| [`pre-trade-investment-gate`](skills/common/pre-trade-investment-gate/SKILL.md) | İşlem öncesinde ürün, veri, tez, fiyat, likidite, maliyet, boyut, zarar sınırı ve çıkış planını kontrol eder. |
| [`probabilistic-market-forecast`](skills/common/probabilistic-market-forecast/SKILL.md) | Tahminleri dondurulmuş olasılık, aralık, ufuk, kıyas ve sonradan puanlama ile kaydeder. |
| [`public-equity-research`](skills/common/public-equity-research/SKILL.md) | Şirketi faaliyet, finansal tablo, değerleme, yönetim, risk ve katalizörlerle araştırır. |
| [`technical-quant-analysis`](skills/common/technical-quant-analysis/SKILL.md) | Doğrulanmış OHLCV verisiyle teknik gösterge, seviye, volatilite ve backtest kalitesini inceler. |
| [`turkey-markets-analysis`](skills/common/turkey-markets-analysis/SKILL.md) | BIST, TEFAS, KAP, TCMB, TÜİK ve Türkiye ürünlerini resmi güncel kaynaklarla araştırır. |
| [`warrant-structured-product-analyst`](skills/common/warrant-structured-product-analyst/SKILL.md) | Varantı dayanak, kullanım fiyatı, vade, dönüşüm oranı, volatilite, likidite ve ihraççı riskiyle çözümler. |

## En doğru kullanım

Önce `investment-copilot` ile soruyu yönlendir. Güncel veriyi `finance-evidence-guard` ile doğrula. Ürün sahibinin analizinden sonra `investment-red-team`, `portfolio-risk-and-sizing` ve `pre-trade-investment-gate` çalıştır. Kararı `investment-thesis-tracker` ile kaydet; sonucu `investment-journal-review` ve tahmin puanlayıcısıyla değerlendir.

“En çok ne artar?” sorusu tek rakamlı kesin cevap üretmez. Karşılaştırılabilir aday listesi, koşullu yükseliş senaryoları, aşağı yönlü risk, güven düzeyi ve işlemi yapmama koşulları üretir.
