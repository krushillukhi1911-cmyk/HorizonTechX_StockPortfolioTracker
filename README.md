# Stock Portfolio Tracker

## Overview
A console-based Stock Portfolio Management System that allows users to manage their stock investments, calculate portfolio values based on predefined stock prices, generate CSV reports, and store data persistently in JSON format.

## Features
- Add Stocks
- View Portfolio
- Search Stocks
- Update Stocks
- Delete Stocks
- Calculate Portfolio Value
- Generate CSV Reports
- Save Data Permanently (JSON)
- Display Investment Analytics

## Technologies Used
- **Language**: Python 3.11+
- **Libraries**: os, csv, json, datetime, pathlib, logging

## Folder Structure
```text
StockPortfolioTracker/
├── main.py
├── config/
│   └── stock_prices.py
├── models/
│   └── stock.py
├── services/
│   ├── portfolio_service.py
│   ├── report_service.py
│   └── analytics_service.py
├── data/
│   └── portfolio.json
├── reports/
│   └── investment_report.csv
├── logs/
│   └── portfolio.log
├── screenshots/
├── tests/
│   └── test_portfolio.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
Clone the repository:
```bash
git clone <repository-url>
cd StockPortfolioTracker
```

## Create Virtual Environment
```bash
python -m venv venv
```

## Activate Environment
**Windows**:
```bash
venv\Scripts\activate
```
**Linux/Mac**:
```bash
source venv/bin/activate
```

## Install Requirements
```bash
pip install -r requirements.txt
```

## Run Project
```bash
python main.py
```

## Sample Outputs
**Adding a Stock:**
```text
Stock Added Successfully
Symbol: AAPL
Quantity: 10
Price: 180
Investment Value: 1800
```

**Viewing Portfolio:**
```text
---------------------------------------------------------
SYMBOL     QTY        PRICE      VALUE     
---------------------------------------------------------
AAPL       10         180        1800      
TSLA       5          250        1250      
---------------------------------------------------------
TOTAL VALUE = 3050
---------------------------------------------------------
```

## Future Enhancements
* Real-time Stock API
* Portfolio Charts
* Web Dashboard
* User Authentication

## Author
Krushil Lukhi
