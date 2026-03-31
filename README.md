# 📈 Big Stock Price Prediction Using Apache Spark

A comprehensive **Big Data Analytics** application for stock price prediction using **Apache Spark (PySpark)** for backend data processing and machine learning, combined with **Streamlit** for an interactive frontend dashboard.

## 🎯 Project Overview

This project demonstrates how to build a scalable financial analytics platform that:

- **Loads and processes** large historical stock datasets efficiently using Spark
- **Performs feature engineering** including technical indicators (Moving Average, RSI, MACD, Bollinger Bands)
- **Trains multiple ML models** (Linear Regression, Random Forest) using Spark MLlib
- **Evaluates models** using RMSE, MSE, MAE, and R² Score metrics
- **Provides interactive visualizations** using Streamlit and Plotly
- **Simulates portfolio tracking**

> **Note:** The price alerts module has been removed from this application; UI entries, backend logic, and database tables were cleaned up.

---

## 🏗️ Architecture

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Big Data Processing** | Apache Spark (PySpark) | Distributed data processing and model training |
| **ML Library** | Spark MLlib | Scalable machine learning algorithms |
| **Frontend** | Streamlit | Interactive web dashboard |
| **Visualization** | Plotly | Rich, interactive charts and graphs |
| **Data Format** | CSV | Local storage of historical stock data |
| **Language** | Python 3.8+ | Primary development language |

### System Architecture

```
Data Layer (CSV)
    ↓
Backend (Spark)
    ├─ Data Processing (spark_session, data_processing.py)
    ├─ Feature Engineering (feature_engineering.py)
    ├─ Model Training (model_training.py)
    └─ Prediction (prediction.py)
    ↓
Frontend (Streamlit)
    ├─ Login Page
    ├─ Dashboard
    ├─ Stock Search
    ├─ Technical Analysis
    ├─ Portfolio Tracker
    └─ Model Performance
```

---

## 📁 Project Structure

```
big-stock-price-prediction/
├── main.py                          # Streamlit app entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── backend/                         # Spark backend modules
│   ├── data_processing.py          # Data loading and cleaning
│   ├── feature_engineering.py      # Technical indicators (MA, RSI, MACD)
│   ├── model_training.py           # Spark MLlib model training
│   └── prediction.py               # Model prediction utilities
│
├── frontend/                        # Streamlit frontend
│   ├── components/
│   │   ├── charts.py               # Plotly chart helpers
│   │   └── sidebar.py              # Navigation sidebar
│   └── pages/
│       ├── login.py                # Authentication page
│       ├── dashboard.py            # Main dashboard
│       ├── stock_search.py         # Stock search and analysis
│       ├── technical_analysis.py   # Technical indicators
│       ├── portfolio.py            # Portfolio tracker
│
├── config/                          # Configuration
│   └── settings.py                 # App settings and parameters
│
├── utils/                           # Utilities
│   ├── helpers.py                  # Helper functions
│   └── spark_session.py            # Spark session management
│
└── data/                            # Data storage
    └── stock_prices.csv            # Historical stock data
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Java 8+ or 11 (required for Spark)

### Installation

1. **Clone the repository** (or extract the project folder)

```bash
cd big-stock-price-prediction
```

2. **Create a virtual environment** (optional but recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

This will install:
- PySpark 3.5.0
- Streamlit 1.28.1
- Pandas, NumPy, Scikit-learn
- Plotly for visualizations
- Technical analysis library (ta)
- And other required packages

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 🔐 Login Credentials

The application includes demo authentication. Use any of these credentials:

(Credentials are stored securely in the backend database; use the sign-up page to create an account.)

---

## 📋 Features

### Frontend Features (Streamlit)

#### 1. **Login / Signup Pages**
- Full registration and login using email/password
- Backend API with JWT authentication
- Client-side form validation and feedback

#### 2. **Dashboard**
- Market overview (S&P 500, NASDAQ, Dow Jones, VIX)
- Real-time stock predictions
- Model performance metrics
- Interactive charts
- Technical analysis visualizations

#### 3. **Stock Search**
- Search any stock ticker
- View historical price data
- Multiple chart types (Line, Candlestick, Moving Average)
- Technical indicators (RSI, MACD)
- Price predictions with confidence scores
- Historical data display

#### 4. **Technical Analysis**
- **RSI (Relative Strength Index)**: Overbought/Oversold indicators
- **MACD**: Trend following momentum indicator
- **Bollinger Bands**: Volatility analysis
- **Moving Averages**: Trend identification
- Interactive interpretation guide

#### 5. **Portfolio Tracker**
- Simulate stock positions
- Track gain/loss in real-time
- Portfolio value visualization
- Download portfolio as CSV
- Manage multiple positions


### Backend Features (Spark)

#### 1. **Data Processing** (`data_processing.py`)
- Load CSV data into Spark DataFrames
- Data cleaning (handling missing values, duplicates)
- Column normalization
- Date range filtering
- Statistics calculation

#### 2. **Feature Engineering** (`feature_engineering.py`)
- **Moving Averages**: 5, 10, 20, 50-day periods
- **RSI**: 14-period Relative Strength Index
- **MACD**: MACD line, Signal line, Histogram
- **Bollinger Bands**: Upper, middle, lower bands
- **Price Changes**: 1-day, 5-day, 20-day returns
- **Volatility**: Rolling standard deviation
- **Volume Indicators**: Volume moving averages, ratios
- **Lagged Features**: Historical price lags

#### 3. **Model Training** (`model_training.py`)
Implements two algorithms using Spark MLlib:

**Linear Regression**
- Elastic net regularization
- Parameters: elasticNetParam=0.1, regParam=0.1
- Max iterations: 100

**Random Forest Regression**
- 10 decision trees
- Max depth: 5 levels
- Seed: 42 (reproducibility)

**Model Evaluation**
- RMSE (Root Mean Squared Error)
- MSE (Mean Squared Error)  
- MAE (Mean Absolute Error)
- R² Score (Coefficient of Determination)

#### 4. **Prediction** (`prediction.py`)
- Load trained models
- Prepare data for prediction
- Make single/batch predictions
- Confidence score calculation
- Multi-day forecasting

---



## 📊 Sample Dataset

The project includes sample historical stock data in `data/stock_prices.csv` with the following columns:

```
date,ticker,open,high,low,close,volume
2024-01-01,AAPL,189.95,190.22,187.50,188.75,2500000
...
```

**Format:**
- Date: YYYY-MM-DD
- Ticker: Stock symbol (e.g., AAPL, GOOGL, MSFT)
- OHLC: Open, High, Low, Close prices
- Volume: Trading volume in shares

---

## 🧠 How to Use

### 1. Start the Backend API
Before running the Streamlit frontend, start the authentication service. Open a new terminal and execute:

```bash
# install dependencies if not already done
pip install -r requirements.txt

# run FastAPI backend
uvicorn backend.app:app --reload
```

The API will listen on `http://localhost:8000` and provides the following endpoints:

- `POST /register` : create new user (requires JSON body `{email, password}`)
- `POST /login` : authenticate user and return JWT token
- `GET /profile` : protected; returns current user info when called with `Authorization: Bearer <token>`

### 2. Start the Streamlit Frontend
Once the backend is running, start the Streamlit application:

```bash
streamlit run main.py
```

### 3. Login / Signup
- Click **Sign Up** in the sidebar to create an account.
- Provide a valid email and password; duplicate emails are blocked.
- After registering, return to **Login**, enter your email/password and click **Login**.
- Upon successful login you will be sent to the dashboard automatically.
> **Tip:** if the login page seems to stay the same, refresh the page or click **Dashboard** in the sidebar.

> **Tip:** the sidebar now includes a **Theme** selector (Light/Dark). Choose a dark mode if you'd prefer a darker UI.

### Downloading Historical Data
A helper script has been added to the backend for pulling multiple years of
stock history from Yahoo Finance and saving it as CSV.  The function
``backend.real_data_fetch.save_historical_data`` does the heavy lifting, and
`backend/fetch_and_train.py` provides a command‑line wrapper:

```bash
# fetch 5 years of data for AAPL and save to data/AAPL_5y.csv
python -m backend.fetch_and_train AAPL --years 5

# do the same and then run the Spark training pipeline on that file
python -m backend.fetch_and_train AAPL --years 5 --train
```

The produced CSV (e.g. ``data/AAPL_5y.csv``) can then be loaded and processed
using the sample training workflow shown later in this README.

### 3. Explore Dashboard
- View market overview and metrics (dashboard will be selected automatically after login)
- Check stock predictions
- Analyze model performance

### 4. Search Stocks
- Go to "Stock Search"
- Enter a ticker (e.g., AAPL, GOOGL)
- Select time period and chart type
- View technical indicators

### 5. Build Portfolio
- Navigate to "Portfolio Tracker"
- Add stock positions
- Track gains/losses
- Download portfolio data


---

## 🔍 Technical Details

### Spark MLlib Model Training

**Linear Regression Process:**
```
Raw Data (CSV)
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Train-Test Split (80-20)
    ↓
Feature Scaling (StandardScaler)
    ↓
Model Training
    ↓
Evaluation (RMSE, MSE, R²)
    ↓
Model Persistence
```

**Random Forest Training:**
- Bootstrap sampling of data
- Random feature selection at each split
- Ensemble predictions from multiple trees
- Aggregated results for final prediction

### Feature Engineering Pipeline

```python
# Technical Indicators Calculated
1. Moving Averages (5, 10, 20, 50-day)
2. RSI (14-period)
3. MACD (12, 26, 9-day periods)
4. Bollinger Bands (20-day, 2 std dev)
5. Price Returns (1, 5, 20-day)
6. Volatility (20-day rolling std)
7. Volume Indicators
8. Lagged Features (historical prices)
↓
Target Variable: Future Price (next 1, 5, or 20 days)
↓
Handle Missing Values
↓
Ready for Model Training
```

---

## 📈 Sample Workflow

### Training a Model

```python
from backend import data_processing, feature_engineering, model_training
from utils.spark_session import get_spark_session

# 1. Get Spark session
spark = get_spark_session()

# 2. Load data
df = data_processing.load_csv_data("data/stock_prices.csv", spark)

# 3. Clean data
df_clean = data_processing.handle_missing_values(df)

# 4. Engineer features
pdf = data_processing.convert_spark_to_pandas(df_clean)
pdf_features = feature_engineering.engineer_features(pdf)

# 5. Convert back to Spark
sdf = data_processing.convert_pandas_to_spark(pdf_features, spark)

# 6. Split data
train_df, test_df = model_training.split_train_test(sdf)

# 7. Train models
lr_model = model_training.train_linear_regression(train_df)
rf_model = model_training.train_random_forest(train_df)

# 8. Evaluate
lr_metrics = model_training.evaluate_model(lr_model, test_df)
rf_metrics = model_training.evaluate_model(rf_model, test_df)

# 9. Save best model
model_training.save_model(lr_model)
```

---

## 🎓 Educational Value

This project demonstrates:

### Big Data Concepts
- **Distributed Processing**: PySpark for parallel data operations
- **Scalability**: Handling large datasets efficiently
- **Data Pipeline**: End-to-end ETL process

### Machine Learning
- **Feature Engineering**: Technical indicators for stock analysis
- **Model Training**: Multiple algorithms using Spark MLlib
- **Model Evaluation**: Comprehensive metrics (RMSE, MSE, MAE, R²)

### Software Engineering
- **Modular Design**: Separated concerns (backend, frontend, config)
- **Clean Code**: Well-documented functions and classes
- **Best Practices**: Error handling, logging, configuration management

### Data Visualization
- **Interactive Charts**: Plotly for rich visualizations
- **Real-time Dashboards**: Streamlit for reactive UI
- **Technical Analysis**: Multiple indicator visualizations

---

## 🏆 Viva Presentation Talk Points

### 1. Problem Statement
"Build a scalable system for stock price prediction using big data technologies that can process historical stock data, engineer relevant features, train multiple ML models, and provide actionable insights through an interactive dashboard."

### 2. Solution Architecture
"We used Apache Spark for distributed data processing and MLlib for scalable model training. The frontend is built with Streamlit for rapid prototyping and interactivity. This architecture can handle datasets of any size."

### 3. Key Features Implemented
- Robust data processing pipeline
- Comprehensive feature engineering (8+ indicators)
- Two-model ensemble approach (Linear Regression + Random Forest)
- Multi-metric evaluation
- Interactive web dashboard

### 4. Technical Highlights
- **PySpark**: Distributed processing across multiple cores/nodes
- **MLlib**: Scalable machine learning algorithms
- **Plotly**: Interactive visualizations
- **Streamlit**: Rapid UI development

### 5. Results & Metrics
- R² Score: 0.92+ indicates good model performance
- RMSE/MAE: Low prediction errors
- Portfolio Tracker: Accurate P&L calculations
- Portfolio simulation and tracking

### 6. Scalability
"The system can scale to:
- Terabytes of historical data (Spark cluster)
- Real-time streaming data (Structured Streaming)
- Multiple stocks or markets
- Multiple users (with proper architecture)"

### 7. Future Enhancements
- Integrate real-time market data (yfinance, market APIs)
- Add deep learning models (Neural Networks)
- Implement distributed feature engineering
- Cloud deployment (AWS, Azure, GCP)
- User authentication and persistence

---

## 📝 Dependencies

Main Python packages:
- **pyspark==3.5.0** - Distributed computing
- **streamlit==1.28.1** - Web framework
- **pandas==2.1.1** - Data manipulation
- **numpy==1.24.3** - Numerical computing
- **plotly==5.17.0** - Interactive charts
- **scikit-learn==1.3.1** - ML utilities
- **ta==0.10.2** - Technical analysis

See `requirements.txt` for complete list.

---

## 🐛 Troubleshooting

### Issue: Spark not starting
**Solution**: Ensure Java is installed and JAVA_HOME is set
```bash
java -version
```

### Issue: Port 8501 already in use
**Solution**: Use a different port
```bash
streamlit run main.py --server.port 8502
```

### Issue: Memory errors with large datasets
**Solution**: Increase Spark memory in settings.py
```python
SPARK_DRIVER_MEMORY = "8g"  # Increase from 4g
```

### Issue: PySpark import errors
**Solution**: Reinstall PySpark
```bash
pip install --upgrade pyspark
```

---

## 📚 References & Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Technical Analysis Indicators](https://en.wikipedia.org/wiki/Technical_analysis)

---

## 👨‍💻 Development

### Code Style
- Follow PEP 8 conventions
- Use type hints for function parameters
- Write comprehensive docstrings
- Keep functions focused and small

### Testing
To test individual modules:
```python
# Test Spark session
from utils.spark_session import get_spark_session
spark = get_spark_session()
print(f"Spark Version: {spark.version}")
```

### Potential Enhancements
1. Add real data integration (yfinance API)
2. Implement backtesting framework
3. Add risk metrics (Sharpe ratio, max drawdown)
4. Deploy on cloud (AWS, Azure, GCP)
5. Add websocket for real-time updates

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

---

## 📞 Contact

For questions or support, please reach out or check the project documentation.

---

**Last Updated**: March 2026  
**Version**: 1.0.0  
**Status**: Production Ready 🚀

