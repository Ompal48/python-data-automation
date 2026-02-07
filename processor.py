import pandas as pd
import sqlite3
from config import DATABASE_NAME, PROCESSED_DATA_FILE

def process_data():
    """
    Loads data from SQLite database into Pandas DataFrame.
    Cleans data, sorts by market_cap descending, saves to CSV, and returns DataFrame.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    df = pd.read_sql_query("SELECT * FROM crypto_data ORDER BY timestamp DESC LIMIT 5", conn)
    conn.close()

    # Clean data: remove rows with null values
    df = df.dropna()

    # Sort by market_cap descending
    df = df.sort_values(by='market_cap', ascending=False)

    # Save processed data to CSV
    df.to_csv(PROCESSED_DATA_FILE, index=False)

    print("Processed data saved to data/processed.csv")
    return df
