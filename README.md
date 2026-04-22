# 📊 Price Tracker - Competitor Price Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

------------------------------------------------------------------------

## Live Deployment Link -

FastAPI (Render) - https://price-tracker-vak8.onrender.com

Frontend (Netlify) - https://reliable-zabaione-bd0785.netlify.app/

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

## 🔹 API Response Examples

### **GET /** - Health Check
```bash
curl http://127.0.0.1:8000/
```
Response:
```json
{
  "message": "Price Tracker API Running"
}
```

### **GET /products** - Get All Products
```bash
curl http://127.0.0.1:8000/products
```
Response:
```json
{
  "data": [
    ["Product Name 1", 12.99, "2024-01-15 10:30:45"],
    ["Product Name 2", 45.50, "2024-01-15 10:30:45"]
  ]
}
```

### **GET /average-price** - Get Average Price
```bash
curl http://127.0.0.1:8000/average-price
```
Response:
```json
{
  "average_price": 37.85
}
```

------------------------------------------------------------------------

## 🔹 Troubleshooting

### **Port 8000 already in use**
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :8000   # Windows (find PID, then taskkill /PID <pid>)

# Or use different port
python -m uvicorn api.app:app --port 8001
```

### **Database file not found**
```bash
# Ensure you've run initialization
python scraper/scraper.py
python processing/clean_data.py
python database/db.py
```

### **Import errors (missing packages)**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### **CORS errors in frontend**
Ensure API is running with CORS enabled (already configured in `api/app.py`)

------------------------------------------------------------------------

## 🔹 Project Structure

```
price-tracker/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
│
├── scraper/
│   └── scraper.py         # Web scraping logic (BeautifulSoup)
│
├── processing/
│   └── clean_data.py      # Data cleaning & transformation (Pandas)
│
├── database/
│   └── db.py              # Database initialization & insertion (SQLite)
│
├── api/
│   └── app.py             # REST API endpoints (FastAPI)
│
├── scheduler/
│   └── scheduler.py       # Automated pipeline scheduler
│
├── frontend/
│   └── index.html         # Dashboard UI
│
└── data/
    ├── raw_data.csv       # Scraped data
    ├── cleaned_data.csv   # Cleaned data
    └── products.db        # SQLite database
```

------------------------------------------------------------------------

## 🔹 Environment Variables

------------------------------------------------------------------------

## 🔹 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for version control)

Check Python version:
```bash
python --version
```

------------------------------------------------------------------------

## 🔹 Complete Setup Instructions

### **Step 1: Clone Repository**
```bash
cd price-tracker
git init
```

### **Step 2: Create Virtual Environment** (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

Expected output: Successfully installed requests, beautifulsoup4, pandas, fastapi, uvicorn, schedule, python-dotenv

### **Step 4: Create Environment Configuration**
Create `.env` file in project root:
```bash
# .env
DB_PATH=data/products.db
API_HOST=127.0.0.1
API_PORT=8000
SCRAPE_INTERVAL=6
```

### **Step 5: Run Data Pipeline (One-Time Setup)**

#### **5a. Scrape Data**
```bash
python scraper/scraper.py
```
Output: "Scraping Done" (creates `data/raw_data.csv`)

#### **5b. Clean Data**
```bash
python processing/clean_data.py
```
Output: "Cleaning Done" (creates `data/cleaned_data.csv`)

#### **5c. Initialize Database**
```bash
python database/db.py
```
Output: Database created with schema and data inserted

### **Step 6: Start API Server**
```bash
python -m uvicorn api.app:app --reload --host 127.0.0.1 --port 8000
```

Expected output:
```
Uvicorn running on http://127.0.0.1:8000
Press CTRL+C to quit
```

The API is now live! 🚀

### **Step 7: Access API Endpoints**

#### **Interactive Documentation (Swagger UI)**
```
http://127.0.0.1:8000/docs
```

#### **Test Endpoints in Terminal (New Window)**

Get products:
```bash
curl http://127.0.0.1:8000/products
```

Get average price:
```bash
curl http://127.0.0.1:8000/average-price
```

Health check:
```bash
curl http://127.0.0.1:8000/
```

### **Step 8: Access Frontend Dashboard** (New Terminal)

```bash
python -m http.server 5500
```

Open browser:
```
http://127.0.0.1:5500/frontend/index.html
```

------------------------------------------------------------------------

## 🔹 Running Automated Scheduler** (Optional - New Terminal)

Run pipeline automatically every 6 hours:
```bash
python scheduler/scheduler.py
```

To stop: Press `CTRL+C`

------------------------------------------------------------------------

## 🔹 Complete Workflow Example

### Terminal 1 - Run API
```bash
python -m uvicorn api.app:app --reload
```

### Terminal 2 - Run Scheduler
```bash
python scheduler/scheduler.py
```

### Terminal 3 - Access Frontend
```bash
python -m http.server 5500
# Open http://127.0.0.1:5500/frontend/index.html
```

Or test API with curl:
```bash
curl http://127.0.0.1:8000/products
curl http://127.0.0.1:8000/average-price
```

------------------------------------------------------------------------

## 🔹 Quick One-Command Setup**

Fresh setup from scratch:
```bash
python -m venv venv && \
venv\Scripts\activate && \
pip install -r requirements.txt && \
python scraper/scraper.py && \
python processing/clean_data.py && \
python database/db.py && \
echo "Setup complete! Run: python -m uvicorn api.app:app --reload"
```

------------------------------------------------------------------------

## 🔹 Environment Variables

Create `.env` file in project root with:

```env
# Database
DB_PATH=data/products.db

# API Configuration
API_HOST=127.0.0.1
API_PORT=8000

# Scheduler
SCRAPE_INTERVAL=6
```

### **Variable Descriptions**
| Variable | Description | Default |
|---|---|---|
| `DB_PATH` | SQLite database file path | `data/products.db` |
| `API_HOST` | API server host address | `127.0.0.1` |
| `API_PORT` | API server port | `8000` |
| `SCRAPE_INTERVAL` | Scheduler interval in hours | `6` |

------------------------------------------------------------------------

## 🔹 Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| **Web Scraping** | BeautifulSoup4 | Extract HTML data |
| **Data Processing** | Pandas | Clean & transform data |
| **Database** | SQLite | Store structured data |
| **API** | FastAPI | REST endpoints |
| **Web Server** | Uvicorn | ASGI server |
| **Automation** | Schedule | Run pipeline periodically |
| **Frontend** | HTML/JavaScript | Display dashboard |

------------------------------------------------------------------------

## 🔹 Data Flow

```
Scraper → Raw CSV → Cleaner → Cleaned CSV → Database → API ↔ Frontend
   ↑                                                      ↑
   └──────── Scheduler (Every 6 hours) ───────────────┘
```

------------------------------------------------------------------------

## 🔹 Future Improvements

- [ ] PostgreSQL integration (instead of SQLite)
- [ ] ML-based price prediction using historical data
- [ ] Email alerts for price changes
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Azure)
- [ ] Advanced analytics dashboard
- [ ] User authentication
- [ ] Multi-source scraping

------------------------------------------------------------------------

## 🔹 Skills Demonstrated

✅ Web Scraping (BeautifulSoup, pagination, error handling)  
✅ Data Cleaning & Transformation (Pandas)  
✅ Database Design & Management (SQLite)  
✅ REST API Development (FastAPI)  
✅ Process Automation & Scheduling  
✅ Frontend Integration  
✅ Error Handling & Logging  
✅ Version Control (Git)

------------------------------------------------------------------------
