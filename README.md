# Finance Hub V1.0.0

**Self-hosted personal finance dashboard. Multi-currency. AI-assisted. Locally owned.**

Track transactions · Manage investments · Monitor accounts · Visualise net worth · Run recurring rules · Chat with your finances via AI

---

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Self-Hosted](https://img.shields.io/badge/Deployment-Self--Hosted-orange?style=flat-square)
![Multi-Currency](https://img.shields.io/badge/Currency-AUD%20%7C%20USD%20%7C%20BDT-purple?style=flat-square)

---

**[Features](#-features-in-detail) · [Quick Start](#-quick-start) · [Screenshots](#-screenshots) · [Security](#-security) · [Template Data](#-template-data) · [License](#-license)**

---

## 📸 Screenshots

> **Dashboard** — Net worth, monthly income/expense, balance trend, spending by category, investment portfolio donut

> **Transactions** — Full history with BDT/USD→AUD live conversion, recurring templates, category breakdown

> **Investments** — Portfolio by country (🇦🇺 🇺🇸 🇧🇩), gain/loss in AUD, property cash flow dashboard

> **Accounts** — Multi-currency balances all converted to AUD in real time

---

## ✨ Why Finance Hub?

- **100% local** — your financial data never leaves your machine
- **Multi-currency** — live FX rates (AUD, USD, BDT and more) auto-convert every figure to AUD
- **Recurring transactions** — set weekly / monthly / yearly rules; system auto-posts them on schedule
- **Investment tracking** — cost basis vs current value with gain/loss %, grouped by country and type
- **Property cash flow** — dedicated Bangladesh property dashboard with BDT→AUD rental income tracking
- **AI chat** — ask questions about your own finances using any local or cloud LLM
- **Tax notes** — per-category tax annotation for year-end reporting
- **Multi-user** — household accounts with per-user or shared investment positions
- **Export** — CSV and Excel export of any dataset
- **Dark UI** — responsive mobile-first design, works on phone or desktop browser

---

## 📋 Prerequisites

| Requirement | Minimum | Notes |
|---|---|---|
| Python | 3.10+ | 3.11 recommended |
| OS | Windows / macOS / Linux | Any platform Python runs on |
| Browser | Chrome / Firefox / Safari | Modern browser required for charts |
| Disk | ~50 MB | SQLite database grows with your data |
| RAM | 256 MB | Lightweight Flask server |
| AI (optional) | Any OpenAI-compatible API | Ollama, OpenAI, Anthropic, etc. |

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/finance-hub.git
cd finance-hub
pip install -r requirements.txt
```

### 2. Run

**Windows:**
```bat
run.bat
```

**macOS / Linux:**
```bash
python main.py
```

### 3. Open

```
http://localhost:8082
```

Default login is created on first run — set your username and password in the **Settings** page.

### 4. Configure AI (optional)

Go to **Settings → AI Providers** and enter your API key for any supported engine:

| Engine | Notes |
|---|---|
| Ollama (local) | Free, runs offline — install from ollama.com |
| OpenAI (GPT-4o) | Requires API key |
| Anthropic (Claude) | Requires API key |
| OpenRouter | Access 100+ models with one key |
| Any OpenAI-compatible | Custom base URL supported |

---

## 🔥 Features in Detail

### 💸 Transactions

- Add income / expense entries with date, category, amount, currency, account, notes
- **Live FX conversion** — BDT and USD amounts display as AUD equivalent with original shown below
- **Recurring templates** — weekly / monthly / yearly auto-posting rules
- Summary strip: filtered income / expenses / net always in AUD
- Category autocomplete — new categories created automatically on first use
- Search, filter by type, month, category

### 📈 Investments

- Track positions by name, type, units, cost basis, current value, currency, country
- **AUD conversion** — USD and BDT positions converted at live rates in every column
- Country breakdown cards: 🇦🇺 Australia · 🇺🇸 USA · 🇧🇩 Bangladesh
- Gain / Loss % per position and per country
- **Property cash flow dashboard** (Bangladesh property section):
  - Monthly rental income in BDT + AUD equivalent
  - Maintenance and repair cost tracking
  - Upcoming scheduled costs calendar
  - All-time cash flow summary
- Portfolio doughnut chart by investment type

### 🏦 Accounts

- Multi-currency account balances (AUD, USD, BDT)
- All balances displayed in AUD with original currency shown
- Account types: Savings, Checking, Fixed Deposit, Investment
- Country tagging (Australia, USA, Bangladesh, Other)

### 📊 Dashboard

- **Net worth** = Accounts + Investments − Liabilities (all AUD-converted)
- This Month / Last Month / This Year income vs expense donuts
- Balance Trend line chart (6 months)
- Income vs Expenses bar chart (weekly / monthly / yearly)
- Spending by Category progress bars
- Investment Portfolio pie chart
- Investment Trend chart (value vs cost basis over time)
- Recent Transactions widget with AUD conversion

### 🔁 Recurring Transactions

- Set any transaction as a recurring template
- Frequencies: weekly, monthly, yearly
- Optional start date and end date
- Auto-processed every time the Transactions page loads
- Summary strip shows total recurring income and recurring cost per month

### 🤖 AI Chat

- Ask natural-language questions about your finances
- Context-aware: optionally inject your account/investment/transaction summaries
- Switch AI providers from within the chat UI
- Chat history persisted locally

### 📝 Tax & Notes

- Per-category tax notes for year-end reporting
- Free-form notes section for financial memos

### 📤 Export

- CSV and Excel (XLSX) export for transactions, investments, accounts, liabilities
- Accessible from Settings → Export

---

## 🌐 Live FX Rates

Finance Hub fetches live exchange rates from `open.er-api.com` (free, no API key required) and caches them for 1 hour.

| Pair | Source |
|---|---|
| USD → AUD | Live API |
| BDT → AUD | Cross-calculated via USD |

Fallback rates are used if the API is unreachable:
- `1 USD = 1.4275 AUD`
- `1 BDT ≈ 0.01161 AUD`

---

## 🗃️ Template Data

The repository ships with **no personal data**. On first run, Finance Hub creates an empty database.

To explore the app with sample data, run the seed script:

```bash
python seed_demo.py
```

This creates:
- 3 sample users (Admin, Partner, Demo)
- 12 months of randomised income / expense transactions
- 6 sample investments (Australian ETF, US ETF, Bangladesh property)
- 3 sample accounts (Savings AUD, Fixed Deposit BDT, US Brokerage USD)
- Sample recurring templates (rent, utilities, subscriptions)

All amounts are randomised — no real financial data is included.

> ⚠️ **Before deploying publicly:** change the default admin password in Settings, set a strong `secret.key`, and bind to `localhost` only (default).

---

## 📁 Project Structure

```
finance-hub/
├── main.py                  # Flask app — all routes, API endpoints, FX logic
├── requirements.txt         # Python dependencies
├── run.bat                  # Windows launcher
├── seed_demo.py             # Demo data seeder (no real data)
├── README.md
├── templates/
│   ├── base.html            # Shared layout, nav, styles
│   ├── index.html           # Dashboard
│   ├── transactions.html    # Transaction list + recurring
│   ├── investments.html     # Portfolio + property cash flow
│   ├── accounts.html        # Account balances
│   ├── liabilities.html     # Debt tracking
│   ├── tax.html             # Tax notes
│   ├── ai.html              # AI chat interface
│   ├── notes.html           # Free-form notes
│   ├── settings.html        # Users, AI providers, export
│   └── login.html           # Authentication
└── data/                    # Auto-created on first run (gitignored)
    ├── finance.db           # SQLite database
    ├── fx_cache.json        # Live FX rate cache
    └── providers.json       # AI engine config
```

---

## ⚙️ Settings

| Section | Purpose |
|---|---|
| Users | Add / edit household members, assign colours and emoji |
| AI Providers | Configure LLM engines and API keys |
| Export | Download CSV or XLSX of any dataset |
| Version | App version and system info |

---

## 🔒 Security

- **Session auth** — password-hashed with `werkzeug.security` (PBKDF2-SHA256)
- **Per-user data isolation** — non-admin users only see their own transactions and accounts
- **Shared investments** — `user_id=0` sentinel for household-level positions visible to all members
- **Admin-only controls** — user management, shared data, and "view as" impersonation require admin role
- **Localhost binding** — server binds to `127.0.0.1` by default; do not expose to the internet without a reverse proxy and HTTPS
- **Secret key** — Flask session key stored in `data/secret.key` (auto-generated, gitignored)
- **No telemetry** — zero external data collection; FX rate fetch is the only outbound call
- **Audit log** — all add / edit / delete actions written to `app_out.log`

> See the source comments in `main.py` for the Demo account isolation design (Demo users are sandboxed from real household data).

---

## 🧪 API Endpoints

Finance Hub exposes a REST API consumed by its own frontend. Key endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/transactions` | List transactions (filterable) |
| POST | `/api/transactions` | Add transaction |
| PUT | `/api/transactions/<id>` | Update transaction |
| DELETE | `/api/transactions/<id>` | Delete transaction |
| GET | `/api/investments` | List investments |
| POST | `/api/investments` | Add investment |
| GET | `/api/accounts` | List accounts |
| POST | `/api/recurring` | Create recurring template |
| PUT | `/api/recurring/<id>` | Update recurring template |
| GET | `/api/summary` | Dashboard summary (AUD-converted) |

All endpoints return `{"ok": true, "data": ...}` or `{"ok": false, "error": "..."}`.

---

## 🤖 Built With AI

Finance Hub was built entirely using **Claude Code** (Anthropic), demonstrating that a production-grade, multi-currency personal finance system can be created through AI-assisted development — no traditional software development background required.

---

## 📜 License

MIT License — free to use, modify, and distribute.

```
Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
provided to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 🌟 Star & Share

If Finance Hub saves you money on subscription finance apps — give it a ⭐ on GitHub and share it with anyone who wants to own their financial data.

---

*Self-hosted. Local-first. Your finances, your machine, your keys.*
