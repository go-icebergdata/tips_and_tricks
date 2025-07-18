# 🍺 Moe vs Barney: Modern Web Scraping Anti-Bot Evasion

> *"Writing custom headers is so 2015. If you want your scraper to blend in today, you don't need to build the disguise from scratch. You need a full profile."*

## 🎭 The Analogy

**Barney (Basic Scraper)** = Your typical scraper with static headers  
**Moe (Anti-Bot System)** = Modern bot detection that kicks out obvious scrapers  
**Barney Returns Disguised** = Advanced scraper using full browser fingerprint profiles  

*In other words: Moe kicks you out, but you come back in with a mustache.*

## 🚀 What This Demo Demonstrates

This demonstration shows the evolution from basic web scraping to sophisticated anti-bot evasion:

1. **`barney_basic.py`** - Traditional scraper with static headers (gets detected)
2. **`barney_disguised.py`** - Modern scraper with full browser fingerprint using `curl_cffi`
3. **`demo.py`** - Side-by-side comparison showing the difference
4. **`examples.py`** - Practical real-world usage examples
5. **`Moe_vs_Barney_Demo.ipynb`** - 📓 **Interactive Jupyter notebook with live examples!**

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
# Test installation
python quick_test.py

# Run the basic scraper (Barney)
python barney_basic.py

# Run the disguised scraper (Barney with mustache)
python barney_disguised.py

# Compare both approaches
python demo.py

# See practical examples
python examples.py

# 📓 Interactive notebook (recommended!)
jupyter notebook Moe_vs_Barney_Demo.ipynb
```

## 📓 Interactive Jupyter Notebook

**New!** The `Moe_vs_Barney_Demo.ipynb` notebook provides an interactive experience where you can:
- See live output from both scraping approaches
- Compare TLS fingerprints and headers side-by-side
- Test different browser impersonations
- View the results directly in your browser

Perfect for understanding the concepts and sharing with others!

## 🔍 What You'll Learn

- Why static headers don't work anymore
- How browser fingerprinting actually works
- Modern anti-bot evasion techniques
- Real-world comparison of detection rates

## 🔬 Technical Deep Dive

### What curl_cffi does differently:
- Mimics exact TLS handshake of real browsers
- Uses correct cipher suite preferences
- Maintains proper HTTP/2 settings
- Sends headers in browser-realistic order
- Handles compression algorithms correctly

### Why static headers fail:
- TLS fingerprint mismatches User-Agent claim
- Header order follows alphabetical pattern
- Missing browser-specific security headers
- HTTP/1.1 when browser claims HTTP/2 support

---

*"The key isn't to outsmart Moe – it's to become someone Moe doesn't recognize."* 