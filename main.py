import pandas as pd
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier as RFC

def financeScrape(ticker):
    stock = yf.Ticker(ticker)
    stock = stock.history(period="6mo")
    stock = stock.drop(columns=['Dividends', 'Stock Splits'])
    stock["Tomorrow"] = stock["Close"].shift(-1)
    stock["Target"] = (stock["Tomorrow"] > stock["Close"]).astype(int)
    print(stock)

def main():
    financeScrape("NANO.TO")

if __name__ == "__main__":
    main()