# 🧪 QA Portfolio – Jiří Karadžov

Ukázky **manuálního a automatizovaného testování** (Web UI + API).  
Projekt kombinuje přehlednost manuálních testů s reálnou ukázkou automatizace pomocí **Pytest + Selenium**  
a integrací do **GitHub Actions CI/CD**.

![CI](https://github.com/JirkaKar/qa-portfolio/actions/workflows/ci.yml/badge.svg)

---

## 📁 Struktura projektu
```
qa-portfolio/
├── manual/
│ ├── test-cases/ # Příklady testovacích scénářů
│ ├── bug-reports/ # Ukázky reportů chyb
│ └── checklists/ # Smoke/Regression checklisty
├── automation/
│ ├── web-ui/ # Automatizované testy webového rozhraní
│ └── api/ # Testy API (v přípravě)
├── docs/ # Poznámky, roadmapy, dokumentace
└── .github/workflows/ # CI pipeline (GitHub Actions)
```
## ⚙️ Automatizované testy (Pytest + Selenium)

Projekt obsahuje ukázku end-to-end testů webového rozhraní pomocí **Python + Pytest + Selenium WebDriver**.  
Testy jsou spustitelné **lokálně i v CI pipeline** (GitHub Actions).

### 🔹 Klíčové principy

- **Framework:** Pytest – jednoduchý a rozšiřitelný framework pro testování.  
- **Web automatizace:** Selenium WebDriver (Chrome, headless režim).  
- **Fixture:** Funkce `driver()` v `conftest.py` spouští a uzavírá prohlížeč.  
- **Explicitní čekání:** `WebDriverWait` + `expected_conditions` zvyšují stabilitu testů.  
- **Assertion:** Každý test končí ověřením (`assert ...`).  
- **Reportování:** Plugin `pytest-html` generuje přehledný report (`reports/report.html`).  
- **CI/CD:** Testy běží automaticky po každém pushi (workflow `.github/workflows/ci.yml`).

### 🔹 Ukázkový test
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_positive(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in flash
🔹 Výsledky testů

Po běhu testů se automaticky vygeneruje HTML report v automation/web-ui/reports/.
V CI se tento report ukládá jako artifact, který lze stáhnout přímo ze stránky GitHub Actions.

Ukázka HTML reportu:

✅ 1 Passed, 0 Failed, 0 Skipped
Soubor: reports/report.html

🚀 Quick start (lokálně)
cd automation/web-ui
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
pytest


Report bude vygenerován do automation/web-ui/reports/report.html.

🧩 Použité technologie
Oblast	Nástroj / Technologie
Test framework	Pytest
Web automatizace	Selenium WebDriver
Reporty	pytest-html
CI/CD	GitHub Actions
Správa driveru	webdriver-manager
Jazyk	Python 3.11+
🧠 Cíl projektu

Cílem je ukázat praktické schopnosti v oblasti QA automatizace:
od návrhu testovacích případů až po jejich plně automatizovaný běh a reportování výsledků.
Repozitorář slouží jako portfolio při přechodu z technické praxe (ISP / elektro) do IT (QA / Dev).

(C) 2025 – Jiří Karadžov
