import pandas as pd
import matplotlib.pyplot as plt
from config import PROCESSED_DATA_FILE, REPORT_FILE

def generate_report(df):
    """
    Generates a text report with summary statistics and saves it to file.
    """
    if df.empty:
        print("No data available for report generation")
        return

    total_coins = len(df)
    highest_priced = df.loc[df['current_price'].idxmax()]['name']
    best_performer = df.loc[df['price_change_percentage_24h'].idxmax()]['name']
    average_price = df['current_price'].mean()

    report = f"""
Cryptocurrency Market Report
============================

Total coins analyzed: {total_coins}
Highest priced coin: {highest_priced}
Best 24h performer: {best_performer}
Average price: ${average_price:.2f}

Detailed Data:
{df.to_string(index=False)}
"""

    with open(REPORT_FILE, 'w') as f:
        f.write(report)

    print("Report generated and saved to reports/summary.txt")

def generate_html_report():
    """
    Generates an HTML report with table and charts.
    """
    df = pd.read_csv(PROCESSED_DATA_FILE)

    # Generate HTML table
    html_table = df.to_html(index=False, classes='table table-striped')

    # Generate charts
    fig, ax = plt.subplots()
    ax.bar(df['name'], df['current_price'])
    ax.set_title('Coin Prices')
    ax.set_xlabel('Coin')
    ax.set_ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/price_chart.png')
    plt.close()

    fig, ax = plt.subplots()
    ax.bar(df['name'], df['market_cap'])
    ax.set_title('Market Cap')
    ax.set_xlabel('Coin')
    ax.set_ylabel('Market Cap (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/marketcap_chart.png')
    plt.close()

    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cryptocurrency Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .table {{ width: 100%; border-collapse: collapse; }}
            .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            .table th {{ background-color: #f2f2f2; font-weight: bold; }}
            .table tr:nth-child(even) {{ background-color: #f9f9f9; }}
            img {{ max-width: 100%; height: auto; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <h1>Cryptocurrency Market Report</h1>
        <h2>Data Table</h2>
        {html_table}
        <h2>Price Chart</h2>
        <img src="price_chart.png" alt="Price Chart">
        <h2>Market Cap Chart</h2>
        <img src="marketcap_chart.png" alt="Market Cap Chart">
    </body>
    </html>
    """

    with open('reports/report.html', 'w') as f:
        f.write(html_content)

    print("HTML report generated and saved to reports/report.html")
