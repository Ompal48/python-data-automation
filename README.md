# Crypto Data Automation & Reporting 🚀

A Flask-based crypto automation project that fetches live cryptocurrency data, stores it in a database, processes it, and generates visual + tabular reports via a web interface.

This project demonstrates **end-to-end data automation** using Python — from API consumption to deployment-ready web reporting.

---

## 🔧 Features

* Fetches live crypto market data (e.g., Bitcoin, Ethereum)
* Stores raw data in SQLite database
* Processes & cleans data using Pandas
* Generates:

  * CSV reports
  * Summary text insights
  * Price & Market Cap charts
* Web dashboard using Flask
* HTML report with tables and charts
* Ready for cloud deployment (Render)

---

## 🗂️ Project Structure

```
python-data-automation/
│
├── app.py                  # Flask application entry point
├── api_client.py           # Fetch crypto data from API
├── database.py             # SQLite DB creation & insert logic
├── processor.py            # Data processing logic
├── reporter.py             # Text + chart report generator
├── html_reporter.py        # HTML report generator
│
├── data/
│   ├── raw.json             # Raw API data
│   └── processed.csv        # Processed dataset
│
├── reports/
│   ├── summary.txt
│   ├── price_chart.png
│   ├── market_cap_chart.png
│
├── static/
│   └── charts/              # Charts served by Flask
│
├── templates/
│   ├── index.html           # Home page
│   └── report.html          # Report page
│
├── crypto_data.db           # SQLite database
├── requirements.txt
└── README.md
```

---

## ▶️ How It Works

1. User clicks **Generate Report** on homepage
2. App fetches crypto data via API
3. Data is stored in SQLite database
4. Data is processed and cleaned
5. Reports and charts are generated
6. User is redirected to `/report` page

---

## 💻 Local Setup



###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Run Application

```bash
python app.py
```

Open browser:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Deployment (Render)

* Uses dynamic PORT binding for Flask
* Production-ready for Render deployment
* Auto-deploys from GitHub


---

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* SQLite
* Matplotlib
* HTML / CSS

---

## 🎯 Learning Outcomes

* API integration
* Data automation pipelines
* Backend web development
* Report generation
* Git & GitHub workflow
* Cloud deployment basics

---

## 👤 Author

**Om Pal**

GitHub: [https://github.com/Ompal48](https://github.com/Ompal48)

---

## ⭐ Future Enhancements

* Add more cryptocurrencies
* Auto-scheduled data refresh
* User authentication
* Interactive charts
* Docker support

---

⭐ If you like this project, give it a star on GitHub!

website - https://python-data-automation-1.onrender.com
