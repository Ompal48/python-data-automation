import sqlite3
import datetime
from config import DATABASE_NAME

def create_table():
    """
    Creates the crypto_data table if it doesn't exist.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_data (
            id TEXT PRIMARY KEY,
            name TEXT,
            current_price REAL,
            market_cap REAL,
            price_change_percentage_24h REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_crypto_data(data):
    """
    Inserts cryptocurrency data into the database with a timestamp.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()

    for coin in data:
        cursor.execute('''
            INSERT OR REPLACE INTO crypto_data (id, name, current_price, market_cap, price_change_percentage_24h, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            coin['id'],
            coin['name'],
            coin['current_price'],
            coin['market_cap'],
            coin['price_change_percentage_24h'],
            timestamp
        ))

    conn.commit()
    conn.close()
    print("Data inserted into database")
