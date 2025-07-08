# 🍺 Moe vs Barney: Modern Web Scraping Anti-Bot Evasion

> *"Writing custom headers is so 2015. If you want your scraper to blend in today, you don't need to build the disguise from scratch. You need a full profile."*

## 🎭 The Analogy

**Barney (Basic Scraper)** = Your typical scraper with static headers  
**Moe (Anti-Bot System)** = Modern bot detection that kicks out obvious scrapers  
**Barney Returns Disguised** = Advanced scraper using full browser fingerprint profiles  

*In other words: Moe kicks you out, but you come back in with a mustache.*

## 🚀 What This Repo Demonstrates

This repository shows the evolution from basic web scraping to sophisticated anti-bot evasion:

1. **`barney_basic.py`** - Traditional scraper with static headers (gets detected)
2. **`barney_disguised.py`** - Modern scraper with full browser fingerprint using `curl_cffi`
3. **`demo.py`** - Side-by-side comparison showing the difference

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 📊 Key Technologies

- **curl_cffi**: Browser impersonation with TLS fingerprinting
- **Fingerprint simulation**: Browser version, screen size, timezone, language
- **Anti-detection**: Modern techniques that actually work in 2024

## 🎯 Why This Matters

Modern anti-bot systems detect more than just headers:
- ✅ TLS fingerprints
- ✅ JavaScript execution patterns  
- ✅ Mouse movements and timing
- ✅ Browser environment consistency
- ✅ Network-level indicators

## 🏃‍♂️ Quick Start

```bash
# Run the basic scraper (Barney)
python barney_basic.py

# Run the disguised scraper (Barney with mustache)
python barney_disguised.py

# Compare both approaches
python demo.py
```

## 🔍 What You'll Learn

- Why static headers don't work anymore
- How browser fingerprinting actually works
- Modern anti-bot evasion techniques
- Real-world comparison of detection rates

---

*"The key isn't to outsmart Moe – it's to become someone Moe doesn't recognize."* 