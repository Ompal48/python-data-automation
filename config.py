# Configuration file for the Python Data Automation & Reporting Tool

# API Configuration
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
API_PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": False
}

# Database Configuration
DATABASE_NAME = "crypto_data.db"

# File Paths
RAW_DATA_FILE = "data/raw.json"
PROCESSED_DATA_FILE = "data/processed.csv"
REPORT_FILE = "reports/summary.txt"
