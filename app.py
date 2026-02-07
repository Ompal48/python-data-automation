from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import shutil
from api_client import fetch_crypto_data
from database import create_table, insert_crypto_data
from processor import process_data
from reporter import generate_report
from html_reporter import generate_html_report

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home page with button to generate crypto report.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Runs the full crypto automation workflow and redirects to report.
    """
    print("Starting crypto data automation workflow...")

    # Step 1: Fetch data
    print("Fetching data...")
    data = fetch_crypto_data()
    if not data:
        return "Failed to fetch data. Please try again."

    # Step 2: Store in database
    print("Storing data...")
    create_table()
    insert_crypto_data(data)

    # Step 3: Process data
    print("Processing data...")
    df = process_data()

    # Step 4: Generate reports
    print("Generating reports...")
    generate_report(df)
    generate_html_report()

    # Copy charts to static folder for serving
    shutil.copy('reports/price_chart.png', 'static/charts/price_chart.png')
    shutil.copy('reports/market_cap_chart.png', 'static/charts/market_cap_chart.png')

    print("Workflow completed!")
    return redirect(url_for('report'))

@app.route('/report')
def report():
    """
    Displays the generated crypto report with table, summary, and charts.
    """
    # Read processed CSV
    csv_path = 'data/processed.csv'
    if not os.path.exists(csv_path):
        return "Processed data not found. Please generate the report first."

    df = pd.read_csv(csv_path)
    table_columns = df.columns.tolist()
    table_data = df.values.tolist()

    # Read summary text
    summary_path = 'reports/summary.txt'
    summary_text = ""
    if os.path.exists(summary_path):
        with open(summary_path, 'r') as f:
            summary_text = f.read()

    return render_template('report.html', table_columns=table_columns, table_data=table_data, summary_text=summary_text)

if __name__ == '__main__':
    app.run(debug=True)

