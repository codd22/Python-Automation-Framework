# 🚀 Playwright Python Automation Framework with Behave and Allure

A complete Python-based automation framework built using:
- **Playwright** (for browser automation)
- **Behave** (for BDD-style testing)
- **Allure** (for detailed reporting)

---

## 📁 Project Structure

project-root/ │ ├── features/ │ ├── steps/ # Step definitions (glue code) │ ├── pages/ # Page Object Models (POM) │ ├── environment.py # Hooks for setup/teardown │ ├── example.feature # Sample feature files │ ├── reports/ │ ├── allure-results/ # Raw Allure results │ ├── requirements.txt # Python dependencies ├── behave.ini # Behave configuration ├── README.md # Project documentation └── .gitignore # Git ignore rules


---

## 🛠 Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m playwright install
