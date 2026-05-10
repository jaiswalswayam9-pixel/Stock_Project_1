from flask import Flask, render_template, send_from_directory
import pandas as pd
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "tsla_stock.db")
TABLE_NAME = "tsla_stock_data"


def get_data():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn,
        parse_dates=["Date"]
    )

    conn.close()

    monthly = df[df["1monthchange"].notna()].copy()
    monthly["MonthLabel"] = monthly["Date"].dt.strftime("%b %Y")
    last_24 = monthly.tail(24).reset_index(drop=True)

    return df, last_24


@app.route("/")
def index():
    df, last_24 = get_data()

    table_data = last_24[
        ["MonthLabel", "Adj Close", "1monthchange"]
    ].to_dict(orient="records")

    stats = {
        "period_start": last_24["MonthLabel"].iloc[0],
        "period_end": last_24["MonthLabel"].iloc[-1],
        "best": last_24.loc[last_24["1monthchange"].idxmax(), "MonthLabel"],
        "best_val": round(last_24["1monthchange"].max(), 2),
        "worst": last_24.loc[last_24["1monthchange"].idxmin(), "MonthLabel"],
        "worst_val": round(last_24["1monthchange"].min(), 2),
        "avg": round(last_24["1monthchange"].mean(), 2),
        "positive": int((last_24["1monthchange"] > 0).sum()),
        "negative": int((last_24["1monthchange"] < 0).sum()),
        "total_rows": len(df),
        "date_start": df["Date"].min().strftime("%b %d, %Y"),
        "date_end": df["Date"].max().strftime("%b %d, %Y"),
    }

    return render_template(
        "index.html",
        table_data=table_data,
        stats=stats
    )


@app.route("/database")
def database():
    try:
        if not os.path.exists(DB_NAME):
            return f"""
            <h1>Database file not found</h1>
            <p>Flask is looking here:</p>
            <p>{DB_NAME}</p>
            """

        conn = sqlite3.connect(DB_NAME)

        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table';",
            conn
        )

        if TABLE_NAME not in tables["name"].values:
            conn.close()
            return f"""
            <h1>Table not found</h1>
            <p>Database found, but table '{TABLE_NAME}' is missing.</p>
            <p>Available tables:</p>
            <pre>{tables}</pre>
            """

        df = pd.read_sql_query(
            f"SELECT * FROM {TABLE_NAME} ORDER BY Date DESC LIMIT 200",
            conn
        )

        conn.close()

        if df.empty:
            return "<h1>Database found, but table has no rows.</h1>"

        html_table = df.to_html(
            classes="db-table",
            index=False,
            border=0
        )

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>TSLA Database</title>
            <style>
                body {{
                    background: #0b0f1a;
                    color: white;
                    font-family: Arial, sans-serif;
                    padding: 30px;
                }}

                h1 {{
                    text-align: center;
                    color: #00d4aa;
                }}

                .btn {{
                    display: inline-block;
                    background: #00d4aa;
                    color: black;
                    padding: 10px 18px;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}

                .db-table {{
                    width: 100%;
                    border-collapse: collapse;
                    background: #111827;
                    color: white;
                    font-size: 13px;
                }}

                .db-table th {{
                    background: #00d4aa;
                    color: black;
                    padding: 10px;
                    border: 1px solid #1e2d40;
                }}

                .db-table td {{
                    padding: 10px;
                    border: 1px solid #1e2d40;
                    text-align: center;
                }}

                .db-table tr:nth-child(even) {{
                    background: #172033;
                }}
            </style>
        </head>

        <body>
            <a href="/" class="btn">← Back to Dashboard</a>

            <h1>TSLA SQLite Database Records</h1>

            <p><b>Database path:</b> {DB_NAME}</p>
            <p><b>Total records shown:</b> {len(df)}</p>

            {html_table}
        </body>
        </html>
        """

    except Exception as e:
        return f"""
        <h1>Database Error</h1>
        <p>{e}</p>
        <p>Database path: {DB_NAME}</p>
        """


@app.route("/static/graphs/<filename>")
def serve_graph(filename):
    return send_from_directory("static/graphs", filename)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)