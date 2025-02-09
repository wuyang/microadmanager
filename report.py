import sqlite3
import argparse
from tabulate import tabulate

DB_PATH = "admanager.db"

def fetch_click_events(ad_id=None):
    """Fetch click events from the database, optionally filtered by ad_id."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if ad_id:
        cursor.execute("SELECT ad_id, timestamp, user_ip FROM click_events WHERE ad_id = ? ORDER BY timestamp DESC", (ad_id,))
    else:
        cursor.execute("SELECT ad_id, timestamp, user_ip FROM click_events ORDER BY timestamp DESC")

    rows = cursor.fetchall()
    conn.close()

    return rows

def generate_report(ad_id=None):
    """Generate and display a report of click events."""
    data = fetch_click_events(ad_id)

    if not data:
        print("No click events found.")
        return

    print("\nAd Click Report:")
    headers = ["Ad ID", "Timestamp", "User IP"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def count_clicks():
    """Count total clicks per ad_id."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT ad_id, COUNT(*) FROM click_events GROUP BY ad_id")
    rows = cursor.fetchall()
    conn.close()

    print("\nClick Summary by Ad ID:")
    print(tabulate(rows, headers=["Ad ID", "Total Clicks"], tablefmt="grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query click_events from click_events.db")
    parser.add_argument("--ad_id", type=int, help="Filter report by a specific ad ID")
    parser.add_argument("--summary", action="store_true", help="Show summary of total clicks per ad ID")

    args = parser.parse_args()

    if args.summary:
        count_clicks()
    else:
        generate_report(args.ad_id)
