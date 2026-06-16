# 📊 Stock Analysis Complete Portfolio
## Akshaya AI Internship - All 4 Projects in One

Welcome! This is a **unified showcase** of my complete stock market analysis journey, from basic data exploration to production-ready AI forecasting systems.

---

## 🎯 Quick Navigation

| Project | Level | Technologies | Status |
|---------|-------|--------------|--------|
| **[Project 1: Stock Data Explorer](#project-1-stock-data-explorer)** | Beginner | Jupyter, Python, CSV Analysis | ✅ Complete |
| **[Project 2: Web Dashboard](#project-2-stock-web-dashboard)** | Intermediate | Flask, SQLite, HTML/CSS | ✅ Complete |
| **[Project 3: ML Predictions](#project-3-stock-vision-ai-ml-predictions)** | Advanced | Scikit-Learn, ML Models, JavaScript | ✅ Complete |
| **[Project 4: Time Series Forecasting](#project-4-quantumforecast-ai)** | Expert | ARIMA, LSTM, Prophet, Advanced ML | ✅ Complete |

---

## 📈 Portfolio Overview

This portfolio demonstrates **progressive skill development** across the entire data science and ML engineering stack:

```
Data Exploration → Web Development → Machine Learning → Production Forecasting
```

---

## 🚀 Project Details

### **Project 1: Stock Data Explorer**

**📁 Repository**: [Stock_Project_1](https://github.com/jaiswalswayam9-pixel/Stock_Project_1)

**Description**: Initial stock market data exploration and analysis using Jupyter Notebooks.

**Key Highlights**:
- 📊 Exploratory data analysis (EDA)
- 📉 Tesla stock historical data analysis
- 📊 Data visualization with Matplotlib
- 🔍 Statistical analysis

**Technologies**: 
- Jupyter Notebook (91.1%)
- Python (3.3%)
- HTML (5.6%)

**Key Files**:
- `Untitled.ipynb` - Main analysis notebook
- `TSLA.csv` - Tesla historical stock data

**What You'll Learn**:
- How to load and explore stock data
- Data preprocessing techniques
- Basic statistical analysis
- Data visualization

---

### **Project 2: Stock Web Dashboard**

**📁 Repository**: [Stock_Project_2](https://github.com/jaiswalswayam9-pixel/Stock_Project_2)

**Description**: Full-stack web application for stock data management and real-time analysis.

**Key Highlights**:
- 🌐 Interactive web interface
- 🔄 Real-time data fetching from Yahoo Finance
- 📊 Beautiful data visualization dashboard
- 📝 CRUD operations (Create, Read, Update, Delete)
- 🎨 Dark-themed responsive design

**Technologies**:
- Python (43.4%) - Flask backend
- HTML (34.6%) - Frontend markup
- CSS (22%) - Styling

**Project Structure**:
```
├── app.py                   # Main Flask application (13KB)
├── database.py              # SQLite operations
├── fetch_stock_data.py      # Yahoo Finance API integration
├── calculations.py          # Financial metrics (returns, moving averages)
├── requirements.txt         # Dependencies
├── templates/               # HTML pages
│   ├── index.html          # Home dashboard
│   ├── stock_data.html     # Data table & charts
│   └── edit_stock.html     # Add/Edit form
└── static/
    └── style.css           # Custom styling
```

**Key Features**:
- Stock data fetching from Yahoo Finance
- Calculate daily returns and moving averages
- Interactive data table
- Chart.js visualizations
- Search & filter functionality
- Add/Edit/Delete records

**API Endpoints**:
- `GET /api/stocks` - All stocks as JSON
- `GET /api/stocks/TSLA` - Ticker-specific data
- `GET /api/chart/MSFT` - Chart data

**Setup**:
```bash
pip install -r requirements.txt
python app.py
# Visit: http://127.0.0.1:5000
```

**What You'll Learn**:
- Building Flask web applications
- SQLite database management
- REST API design
- Real-time data integration
- Frontend-backend communication

---

### **Project 3: StockVision AI - ML Predictions**

**📁 Repository**: [Stock_Project_3](https://github.com/jaiswalswayam9-pixel/Stock_Project_3)

**Description**: Machine learning-powered stock price prediction system with interactive dashboard.

**Key Highlights**:
- 🤖 Multi-model ML pipeline (5 regression models)
- 📊 Advanced feature engineering (15+ technical indicators)
- 🎯 Automatic best-model selection
- 📈 Interactive prediction dashboard
- 📉 Historical database browser
- 🔌 RESTful API endpoints

**Technologies**:
- Python (37.7%) - ML backend
- HTML (30.7%) - Dashboard frontend
- CSS (18.1%) - Responsive design
- JavaScript (13.5%) - Interactive charts

**Project Structure**:
```
├── app.py                  # Flask application (16.5KB)
├── train_model.py          # ML training pipeline
├── predict.py              # Inference engine
├── best_model.pkl          # Serialized model
├── feature_columns.pkl     # Feature registry
├── scaler.pkl              # Fitted scaler
├── model_results.csv       # Model performance metrics
├── training_history.json   # Training metadata
├── requirements.txt
├── templates/
│   ├── base.html          # Navigation layout
│   ├── index.html         # Dashboard home
│   ├── predictions.html   # Forecast view
│   ├── database.html      # Historical browser
│   └── models.html        # Model analytics
└── static/
    └── style.css          # Dashboard styling
```

**ML Models Used**:
1. **Linear Regression** - Baseline model
2. **Decision Tree Regressor** - Non-linear patterns
3. **Random Forest** - Ensemble learning
4. **Gradient Boosting** - High-performance gradient-based
5. **XGBoost** - State-of-the-art boosting

**Feature Engineering** (15+ indicators):
- Simple Moving Averages (5, 10, 20 days)
- Exponential Moving Averages (5, 12 days)
- Lagged values (1, 2, 3 days)
- Volatility measures (5, 10 days)
- Intraday metrics
- Price momentum
- Volume indicators
- Relative Strength Index (RSI)

**API Endpoints**:
- `GET /api/stocks` - Stock data with pagination
- `GET /api/predict/<symbol>` - Next-day prediction
- `GET /api/model-results` - Model metrics
- `GET /api/chart-data/<symbol>` - Chart data

**Setup**:
```bash
pip install -r requirements.txt
python train_model.py      # Train models
python app.py              # Start server
# Visit: http://127.0.0.1:5000
```

**What You'll Learn**:
- Machine learning model comparison
- Feature engineering for time series
- Model serialization & deployment
- Scikit-Learn & XGBoost
- Model evaluation metrics
- Production ML pipelines

---

### **Project 4: QuantumForecast AI - Advanced Forecasting** ⭐

**📁 Repository**: [Stock_Project_4](https://github.com/jaiswalswayam9-pixel/Stock_Project_4)

**Description**: Enterprise-grade time series forecasting platform for top 20 stocks with multi-model ensemble.

**Key Highlights**:
- 📊 Top 20 stocks by market cap
- ⏰ 5-year historical OHLCV data
- 🤖 5 forecasting models (Naive, ARIMA, SARIMA, SARIMAX, Holt-Winters)
- 📈 Advanced feature engineering
- 💾 SQLite persistence (9.8MB database)
- 📊 Model performance tracking
- 🎯 Risk scoring & recommendations
- 🔌 Comprehensive REST APIs

**Technologies**:
- Python (45.9%) - Advanced ML backend
- HTML (34.3%) - Dashboard
- CSS (13.8%) - Styling
- JavaScript (6%) - Interactive charts

**Project Structure**:
```
├── app.py                          # Flask app (21KB)
├── fetch_top20_data.py             # Data pipeline (13.6KB)
├── train_timeseries_models.py      # Training (25KB)
├── forecast_engine.py              # Forecasting (13.7KB)
├── quantumforecast.db              # Database (9.8MB)
├── model_summary.csv               # Model metrics
├── best_model_per_stock.csv        # Best models
├── stock_forecasts.csv             # Predictions (1.46MB)
├── stock_score_2026-05-26.csv      # Market cap ranking
├── top20_stocks.csv                # Selected stocks
├── requirements.txt
├── data/
│   ├── stock_prices.csv
│   └── processed_stock_data.csv
├── templates/
│   ├── index.html                  # KPI dashboard
│   ├── forecast_dashboard.html     # Forecasts
│   ├── model_comparison.html       # Models
│   ├── stock_details.html          # Per-stock analysis
│   └── database.html               # Database browser
└── static/
    ├── style.css
    ├── dashboard.js
    └── graphs/                     # Generated charts
```

**Time Series Models**:

| Model | Configuration | Purpose |
|-------|---------------|---------|
| **Naive** | Last value | Baseline comparison |
| **ARIMA** | (5,1,0) | Autoregressive trends |
| **SARIMA** | (1,1,1)×(1,1,1,5) | Weekly seasonality |
| **SARIMAX** | +Exogenous vars | Volume & returns |
| **Holt-Winters** | Dynamic seasonality | Trend + seasonality |

**Performance Metrics**:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- R² (Coefficient of determination)

**Feature Engineering**:
- Returns and log returns
- SMA/EMA indicators
- Bollinger Bands
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Lagged features
- Trend signals
- Volume ratios

**API Endpoints**:
- `GET /api/stocks` - All stocks with best model
- `GET /api/forecast/<symbol>` - Historical + forecast
- `GET /api/model-results` - Model comparison
- `GET /api/best-models` - Best per stock

**Output Files**:
- `top20_stocks.csv` - Selected equities
- `model_summary.csv` - All metrics
- `best_model_per_stock.csv` - Winners
- `stock_forecasts.csv` - 30-day forecasts
- `quantumforecast.db` - SQLite database
- `static/graphs/*.png` - Visualization charts

**Setup**:
```bash
pip install -r requirements.txt
python fetch_top20_data.py         # Fetch data
python train_timeseries_models.py  # Train models
python app.py                      # Start server
# Visit: http://127.0.0.1:5000
```

**What You'll Learn**:
- Time series analysis & forecasting
- ARIMA/SARIMA models
- Ensemble forecasting
- Advanced feature engineering
- Production ML systems
- Database optimization
- API development
- Data pipeline automation

---

## 🛠️ Technology Stack Summary

### Backend
- **Python** - Core programming language
- **Flask** - Web framework
- **SQLite** - Database engine
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

### Machine Learning
- **Scikit-Learn** - ML algorithms
- **XGBoost** - Gradient boosting
- **Statsmodels** - Time series (ARIMA, SARIMA, Holt-Winters)
- **Joblib** - Model serialization

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Chart.js** - Data visualization
- **D3.js** - Advanced charts

### Data Sources
- **Yahoo Finance API** - Stock prices
- **CSV files** - Market cap rankings

---

## 📊 Key Skills Demonstrated

### Data Science
✅ Exploratory Data Analysis (EDA)
✅ Statistical Analysis
✅ Data Cleaning & Preprocessing
✅ Time Series Analysis

### Machine Learning
✅ Regression models
✅ Model evaluation & comparison
✅ Feature engineering
✅ Hyperparameter tuning
✅ Model serialization

### Time Series Forecasting
✅ ARIMA modeling
✅ Seasonal decomposition
✅ Ensemble forecasting
✅ Exogenous variables

### Web Development
✅ Flask backend development
✅ RESTful API design
✅ HTML/CSS frontend
✅ JavaScript interactivity
✅ Database integration

### Software Engineering
✅ Code organization
✅ Error handling
✅ Documentation
✅ Version control
✅ CI/CD concepts

---

## 🚀 Getting Started

Each project is independently runnable. Start with Project 1 and progress through Project 4:

### **Quick Start - Project 1**
```bash
# Just explore the Jupyter Notebook
# No installation needed!
```

### **Quick Start - Project 2**
```bash
git clone https://github.com/jaiswalswayam9-pixel/Stock_Project_2
cd Stock_Project_2
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Open: http://127.0.0.1:5000
```

### **Quick Start - Project 3**
```bash
git clone https://github.com/jaiswalswayam9-pixel/Stock_Project_3
cd Stock_Project_3
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train_model.py
python app.py
# Open: http://127.0.0.1:5000
```

### **Quick Start - Project 4**
```bash
git clone https://github.com/jaiswalswayam9-pixel/Stock_Project_4
cd Stock_Project_4
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python fetch_top20_data.py
python train_timeseries_models.py
python app.py
# Open: http://127.0.0.1:5000
```

---

## 📈 Learning Progression

**Week 1: Data Exploration**
- Load and explore stock data
- Basic statistical analysis
- Data visualization fundamentals

**Week 2: Web Development**
- Build Flask web applications
- Database management
- Real-time data integration
- User interface design

**Week 3: Machine Learning**
- Feature engineering
- Model training & evaluation
- Scikit-Learn & XGBoost
- Model deployment

**Week 4: Advanced Forecasting**
- Time series analysis
- ARIMA/SARIMA modeling
- Ensemble methods
- Production systems

---

## 📊 Project Comparison

| Aspect | Project 1 | Project 2 | Project 3 | Project 4 |
|--------|-----------|-----------|-----------|-----------|
| **Complexity** | Beginner | Intermediate | Advanced | Expert |
| **Data Points** | Single CSV | 3 stocks | 3 stocks | 20 stocks |
| **Historical Data** | ~250 rows | 1 year | 1 year | 5 years |
| **Models** | Visualization | Analytics | 5 ML models | 5 forecasting models |
| **Database** | None | SQLite | SQLite | SQLite (9.8MB) |
| **UI** | Notebook | Web dashboard | Interactive dashboard | Enterprise dashboard |
| **Predictions** | Analysis | Analytics | Next-day price | 30-day forecast |
| **API Endpoints** | None | 3 APIs | 4 APIs | 4 APIs |

---

## 🎓 Certificates & Recognition

- **Akshaya AI Internship** - Stock Market Analysis specialization
- **Technologies mastered**: Python, Flask, Machine Learning, Time Series
- **Portfolio status**: Complete & production-ready

---

## 📞 Connect With Me

- **GitHub**: [jaiswalswayam9-pixel](https://github.com/jaiswalswayam9-pixel)
- **LinkedIn**: [Swayam Jaiswal](https://www.linkedin.com/in/swayam-jaiswal-b91865238)

---

## 📝 Individual Project Links

1. **[Stock_Project_1](https://github.com/jaiswalswayam9-pixel/Stock_Project_1)** - Data Explorer
2. **[Stock_Project_2](https://github.com/jaiswalswayam9-pixel/Stock_Project_2)** - Web Dashboard
3. **[Stock_Project_3](https://github.com/jaiswalswayam9-pixel/Stock_Project_3)** - ML Predictor
4. **[Stock_Project_4](https://github.com/jaiswalswayam9-pixel/Stock_Project_4)** - Time Series Forecasting

---

**Last Updated**: June 16, 2026  
**Status**: ✅ All Projects Complete and Fully Functional

---

## License

All projects are open source and available for learning purposes.

**Made with ❤️ during Akshaya AI Internship**
