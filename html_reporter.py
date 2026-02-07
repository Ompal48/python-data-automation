import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import os

def generate_html_report():
    """
    Generates an HTML report with a styled table and charts from processed.csv.
    Saves the report to reports/report.html, and charts to reports/price_chart.png and reports/market_cap_chart.png.
    """
    # Define paths
    processed_csv_path = os.path.join('data', 'processed.csv')
    reports_dir = 'reports'
    report_html_path = os.path.join(reports_dir, 'report.html')
    price_chart_path = os.path.join(reports_dir, 'price_chart.png')
    market_cap_chart_path = os.path.join(reports_dir, 'market_cap_chart.png')

    # Read data from CSV
    df = pd.read_csv(processed_csv_path)

    # Generate styled HTML table
    html_table = df.to_html(index=False, classes='crypto-table')

    # Generate bar chart for current_price
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['name'], df['current_price'], color='skyblue')
    ax.set_title('Current Price by Coin')
    ax.set_xlabel('Coin')
    ax.set_ylabel('Current Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(price_chart_path)
    plt.close()

    # Generate bar chart for market_cap
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['name'], df['market_cap'], color='lightgreen')
    ax.set_title('Market Cap by Coin')
    ax.set_xlabel('Coin')
    ax.set_ylabel('Market Cap (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(market_cap_chart_path)
    plt.close()

    # HTML content with professional layout and inline CSS
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cryptocurrency Market Report</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
                margin-bottom: 30px;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
                margin-top: 40px;
            }}
            .crypto-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 14px;
            }}
            .crypto-table th, .crypto-table td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            .crypto-table th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            .crypto-table tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            .crypto-table tr:hover {{
                background-color: #e8f4fd;
            }}
            img {{
                max-width: 100%;
                height: auto;
                margin: 20px 0;
                border: 1px solid #ddd;
                border-radius: 4px;
            }}
            .chart-section {{
                margin-bottom: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Cryptocurrency Market Report</h1>
            <section>
                <h2>Data Table</h2>
                {html_table}
            </section>
            <section class="chart-section">
                <h2>Price Chart</h2>
                <img src="price_chart.png" alt="Current Price Chart">
            </section>
            <section class="chart-section">
                <h2>Market Cap Chart</h2>
                <img src="market_cap_chart.png" alt="Market Cap Chart">
            </section>
        </div>
    </body>
    </html>
    """

    # Write HTML to file
    with open(report_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("HTML report generated and saved to reports/report.html")
    print("Charts saved to reports/price_chart.png and reports/market_cap_chart.png")
