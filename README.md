# Micro Ad Manager

## Overview
This project demonstrates a minimalistic system similar to Google Ad Manager, implemented in under 200 lines of code. It is designed using publicly available information and assisted by GenAI tools like ChatGPT.

To keep the demo simple:
- Most data is hardcoded.
- There is no GUI, only a CLI.
- It lacks supporting systems such as testing, deployment, and monitoring.

Main Components
- SDK: test.html (Ad display and interaction)
- Serving: server.py (Ad server and click tracking)
- Reporting: report.py (Query and analytics tool)
- Database: SQLite3 (Stores ad click events)

---

## Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/wuyang/microadmanager.git
cd microadmanager
```

### **2. Create a Virtual Environment & Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Run the Flask Server**
```bash
python server.py
```
By default, the server runs at `http://127.0.0.1:5000`.

---

## CLI Tool: Query Click Events
### **Usage**
Run the CLI tool to query the `click_events` table:

#### **1. Show All Click Events**
```bash
python query_clicks.py
```

#### **2. Filter by a Specific Ad ID**
```bash
python query_clicks.py --ad_id 123
```

#### **3. Show Click Summary per Ad ID**
```bash
python query_clicks.py --summary
```

### **Example Output**
#### **Click Events Report**
```
+--------+----------------------------+-------------+
| Ad ID  | Timestamp                  | User IP     |
+--------+----------------------------+-------------+
|  123   | 2024-02-09T14:30:15.123456 | 192.168.1.1 |
|  456   | 2024-02-08T12:05:30.987654 | 10.0.0.2    |
+--------+----------------------------+-------------+
```

#### **Click Summary by Ad ID**
```
+--------+--------------+
| Ad ID  | Total Clicks |
+--------+--------------+
|  123   |      10      |
|  456   |       7      |
+--------+--------------+
```