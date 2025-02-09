from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)


def init_db():
    conn = sqlite3.connect("admanager.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS click_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad_id INTEGER,
            timestamp TEXT,
            user_ip TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/getAd", methods=["GET"])
def get_ad():
    mock_ad = {
        "adId": "12345",
        "adImage": "test_ad_image.webp",
        "adUrl": "https://example.com",
    }
    return jsonify(mock_ad)


@app.route("/recordClick", methods=["POST"])
def record_click():
    try:
        data = request.json
        ad_id = data.get("adId")
        user_ip = request.remote_addr
        timestamp = datetime.datetime.now().isoformat()

        conn = sqlite3.connect("admanager.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO click_events (ad_id, timestamp, user_ip) "
            "VALUES (?, ?, ?)",
            (ad_id, timestamp, user_ip),
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Click logged successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
