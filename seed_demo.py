"""
seed_demo.py — Populate Finance Hub with randomised sample data.
Run once after first launch: python seed_demo.py
Wipes existing data and inserts fresh demo records.
"""
import sqlite3, random, datetime
from pathlib import Path
from werkzeug.security import generate_password_hash

DB = Path("data/finance.db")
if not DB.exists():
    print("ERROR: data/finance.db not found. Start the app once first (python main.py), then run this script.")
    raise SystemExit(1)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

# ── Wipe existing demo data ──────────────────────────────────────────────────
con.executescript("""
DELETE FROM transactions;
DELETE FROM investments;
DELETE FROM accounts;
DELETE FROM liabilities;
DELETE FROM recurring_templates;
DELETE FROM users WHERE username != 'admin';
""")

# ── Users ────────────────────────────────────────────────────────────────────
con.execute("DELETE FROM users")
con.execute("""
    INSERT INTO users (name, username, password_hash, emoji, color, is_admin)
    VALUES ('Alex','admin',?,  '👤','#1565c0',1)
""", (generate_password_hash("demo1234"),))
con.execute("""
    INSERT INTO users (name, username, password_hash, emoji, color, is_admin)
    VALUES ('Sam','sam',?,  '🧑','#2e7d32',0)
""", (generate_password_hash("demo1234"),))

admin_id = con.execute("SELECT id FROM users WHERE username='admin'").fetchone()[0]
sam_id   = con.execute("SELECT id FROM users WHERE username='sam'").fetchone()[0]

# ── Accounts ─────────────────────────────────────────────────────────────────
accounts = [
    ("Main Savings",   "Savings",       "Australia", "AUD", round(random.uniform(18000, 35000), 2), admin_id),
    ("Everyday",       "Checking",      "Australia", "AUD", round(random.uniform(2000,  6000),  2), admin_id),
    ("US Brokerage",   "Investment",    "USA",       "USD", round(random.uniform(5000,  15000), 2), admin_id),
    ("Term Deposit",   "Fixed Deposit", "Bangladesh","BDT", round(random.uniform(300000,600000),2), admin_id),
    ("Sam Savings",    "Savings",       "Australia", "AUD", round(random.uniform(8000,  20000), 2), sam_id),
]
for a in accounts:
    con.execute("INSERT INTO accounts (name,acc_type,country,currency,balance,user_id) VALUES (?,?,?,?,?,?)", a)

# ── Investments ───────────────────────────────────────────────────────────────
investments = [
    ("VAS",            "VAS",  "Australian ETF",  random.randint(80,200),   "AUD", "Australia"),
    ("VGS",            "VGS",  "Australian ETF",  random.randint(50,150),   "AUD", "Australia"),
    ("SCHD",           "SCHD", "US ETF",          random.randint(30,100),   "USD", "USA"),
    ("MSFT",           "MSFT", "Stock",           random.randint(5,25),     "USD", "USA"),
    ("Dhaka Property", "",     "Property",        1.0,                      "BDT", "Bangladesh"),
    ("Super Fund",     "",     "Superannuation",  1.0,                      "AUD", "Australia"),
]
for name, ticker, inv_type, units, currency, country in investments:
    if currency == "AUD":
        cost = round(units * random.uniform(80, 120), 2)
        val  = round(cost  * random.uniform(0.95, 1.35), 2)
    elif currency == "USD":
        cost = round(units * random.uniform(50, 300), 2)
        val  = round(cost  * random.uniform(0.90, 1.50), 2)
    else:
        cost = round(random.uniform(3000000, 8000000), 2)
        val  = round(cost  * random.uniform(1.05, 1.20), 2)
    con.execute(
        "INSERT INTO investments (name,ticker,inv_type,units,cost_basis,current_value,currency,country,user_id) VALUES (?,?,?,?,?,?,?,?,?)",
        (name, ticker, inv_type, units, cost, val, currency, country, admin_id)
    )

# ── Transactions (12 months of history) ──────────────────────────────────────
categories_income  = ["Salary", "Freelance", "Rental Income", "Interest"]
categories_expense = ["Groceries", "Utilities", "Internet", "Subscriptions",
                      "Insurance", "Transport", "Health", "Dining", "Shopping",
                      "Property Maintenance"]
today = datetime.date.today()

for month_offset in range(12):
    base = (today.replace(day=1) - datetime.timedelta(days=30 * month_offset))
    ym   = base.strftime("%Y-%m")

    # Salary
    con.execute(
        "INSERT INTO transactions (date,type,category,description,amount,currency,account,user_id) VALUES (?,?,?,?,?,?,?,?)",
        (f"{ym}-25", "income", "Salary", "Monthly salary", round(random.uniform(6500,8500),2), "AUD", "Main Savings", admin_id)
    )
    # Partner salary
    con.execute(
        "INSERT INTO transactions (date,type,category,description,amount,currency,account,user_id) VALUES (?,?,?,?,?,?,?,?)",
        (f"{ym}-25", "income", "Salary", "Monthly salary", round(random.uniform(4500,6000),2), "AUD", "Sam Savings", sam_id)
    )
    # Rental income (BDT)
    con.execute(
        "INSERT INTO transactions (date,type,category,description,amount,currency,account,user_id) VALUES (?,?,?,?,?,?,?,?)",
        (f"{ym}-01", "income", "Rental Income", "Apartment rent -monthly", round(random.uniform(14000,18000),2), "BDT", "Term Deposit", admin_id)
    )
    # Expenses
    expenses = [
        ("Groceries",    random.uniform(400, 700)),
        ("Utilities",    random.uniform(150, 300)),
        ("Internet",     random.uniform(60,  90)),
        ("Subscriptions",random.uniform(30,  60)),
        ("Insurance",    random.uniform(180, 280)),
        ("Transport",    random.uniform(100, 200)),
        ("Dining",       random.uniform(200, 450)),
        ("Health",       random.uniform(50,  200)),
    ]
    for cat, amt in expenses:
        day = random.randint(1, 28)
        con.execute(
            "INSERT INTO transactions (date,type,category,description,amount,currency,account,user_id) VALUES (?,?,?,?,?,?,?,?)",
            (f"{ym}-{day:02d}", "expense", cat, cat, round(amt, 2), "AUD", "Everyday", admin_id)
        )

# ── Recurring Templates ───────────────────────────────────────────────────────
templates = [
    ("expense", "Rent",          "Monthly rent",           2200,  "AUD", "monthly"),
    ("expense", "Utilities",     "Electricity & gas",       180,  "AUD", "monthly"),
    ("expense", "Subscriptions", "Streaming services",       45,  "AUD", "monthly"),
    ("income",  "Rental Income", "Apartment rent -monthly", 16000,"BDT", "monthly"),
]
for typ, cat, desc, amt, cur, freq in templates:
    con.execute(
        "INSERT INTO recurring_templates (type,category,description,amount,currency,frequency,start_date,next_date,active) VALUES (?,?,?,?,?,?,?,?,1)",
        (typ, cat, desc, amt, cur, freq, today.isoformat(), today.replace(day=1).isoformat())
    )

# ── Liabilities ───────────────────────────────────────────────────────────────
con.execute(
    "INSERT INTO liabilities (name,amount,currency,category,notes,user_id) VALUES (?,?,?,?,?,?)",
    ("Car Loan", round(random.uniform(8000, 18000), 2), "AUD", "Loan", "Vehicle finance", admin_id)
)

con.commit()
con.close()
print("✅ Demo data seeded successfully.")
print("   Login: admin / demo1234  or  sam / demo1234")
print("   Open: http://localhost:8082")
