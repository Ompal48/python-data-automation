from api_client import fetch_crypto_data
from database import create_table, insert_crypto_data
from processor import process_data
from reporter import generate_report
from html_reporter import generate_html_report

def main():
    """
    Orchestrates the full workflow: fetch → store → process → report
    """
    print("Starting Python Data Automation & Reporting Tool...")

    # Step 1: Fetch data from API
    print("Fetching cryptocurrency data from API...")
    data = fetch_crypto_data()
    if not data:
        print("Failed to fetch data. Exiting.")
        return

    # Step 2: Store data in database
    print("Storing data in database...")
    create_table()
    insert_crypto_data(data)

    # Step 3: Process data
    print("Processing data...")
    df = process_data()

    # Step 4: Generate reports
    print("Generating text report...")
    generate_report(df)
    print("Generating HTML report...")
    generate_html_report()

    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()
