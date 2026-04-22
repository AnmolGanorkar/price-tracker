# Price Tracker

A price tracking application that scrapes prices, cleans data, stores in database, exposes API, and runs on schedule.

## Structure
- `scraper/`: Web scraping logic
- `processing/`: Data cleaning
- `database/`: Database operations
- `api/`: REST API
- `scheduler/`: Scheduling tasks
- `data/`: CSV data files

## Setup
1. `pip install -r requirements.txt`
2. Configure database in `database/db.py`
3. Run `python scheduler/scheduler.py`

## Usage
Start API: `python api/app.py`

# 📊 Competitor Price Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

------------------------------------------------------------------------

## 🔹 Problem Statement

Small and medium businesses often lack visibility into competitor
pricing. Without structured and up-to-date pricing data, they struggle
to:

-   Adjust pricing strategies\
-   Identify market trends\
-   Stay competitive

------------------------------------------------------------------------

## 🔹 Business Use Case

This system helps:

-   E-commerce sellers\
-   Business analysts\
-   Pricing teams

### Example:

A seller uses **average price** to decide: - Overpriced → losing
customers\
- Underpriced → losing profit

------------------------------------------------------------------------

## 🔹 Features

-   Web scraping with pagination\
-   Data cleaning & standardization\
-   Database storage\
-   REST API (FastAPI)\
-   Simple frontend dashboard\
-   Automated pipeline

------------------------------------------------------------------------

## 🔹 API Endpoints

### GET /products

Returns all products

### GET /average-price

Returns average product price

------------------------------------------------------------------------

## 🔹 Example Response

``` json
{
  "average_price": 37.85
}
```

------------------------------------------------------------------------

## 🔹 Project Structure

    price-tracker/
    │── scraper/
    │── processing/
    │── database/
    │── api/
    │── frontend/
    │── scheduler/

------------------------------------------------------------------------

## 🔹 Setup Instructions

``` bash
pip install -r requirements.txt
python scraper/scraper.py
python processing/clean_data.py
python database/db.py
uvicorn api.app:app --reload
```

------------------------------------------------------------------------

## 🔹 Run Frontend

``` bash
python -m http.server 5500
```

Open: http://127.0.0.1:5500/frontend/index.html

------------------------------------------------------------------------

## 🔹 Future Improvements

-   PostgreSQL integration\
-   ML-based price prediction\
-   Cloud deployment

------------------------------------------------------------------------

## 📸 Screenshots

(Add your project screenshot here)

------------------------------------------------------------------------

## 👨‍💻 Author

Anmol Ganorkar

