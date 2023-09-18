import pandas as pd
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import precision_score as ps

# takes ticker symbol and returns pandas array of stock prices
def financeScrape(ticker):
    stock = yf.Ticker(ticker)
    stock = stock.history(period="max")
    stock = stock.drop(columns=['Dividends', 'Stock Splits'])
    stock["Tomorrow"] = stock["Close"].shift(-1)
    stock["Target"] = (stock["Tomorrow"] > stock["Close"]).astype(int)
    print(stock.news)
    return stock

def ml(stock):
    model = RFC(n_estimators=100, min_samples_leaf=100, random_state=1)

    train = stock.iloc[:-100]
    test = stock.iloc[-100:]
    predictors = ["Close", "Volume", "Open", "High", "Low"]

    model.fit(train[predictors], train["Target"])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index=test.index)
    precision = ps(test["Target"], preds)
    print(f"precision: {precision}")

def main():
    ml(financeScrape("BTC-CAD"))

if __name__ == "__main__":
    main()