import yfinance as yf
import pandas as pd
from datetime import datetime

# Hypothetical list of German stock tickers (you would need a more comprehensive list for real use)
german_stocks = ["SAP.DE", "DTE.DE", "BAS.DE", "ALV.DE", "BMW.DE"]


def get_stock_data(ticker, start_date, end_date):
    """
    Fetches stock market data for a given stock ticker from Yahoo Finance.

    :param ticker: The stock ticker symbol (e.g., 'SAP.DE' for SAP).
    :param start_date: The start date for the data in YYYY-MM-DD format.
    :param end_date: The end date for the data in YYYY-MM-DD format.
    :return: A pandas DataFrame containing the stock market data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data


def is_sharia_compliant(ticker):
    """
    Checks if a stock is Sharia compliant.
    Here we perform hypothetical checks based on financial ratios and business activities.

    :param ticker: The stock ticker symbol.
    :return: Boolean indicating if the stock is Sharia compliant.
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    # Example checks (these should be more comprehensive and based on actual Sharia criteria)
    sector = info.get("sector", "").lower()
    if sector in ["financial services", "alcohol", "gambling", "pork"]:
        return False

    # Financial ratio checks (e.g., Debt to Assets ratio should be less than 33%)
    total_debt = info.get("totalDebt", 0)
    total_assets = info.get("totalAssets", 0)
    if total_assets > 0 and (total_debt / total_assets) > 0.33:
        return False

    return True


def get_sharia_compliant_stocks(stocks, start_date, end_date):
    """
    Fetches stock data for stocks that are Sharia compliant.

    :param stocks: List of stock ticker symbols.
    :param start_date: The start date for the data in YYYY-MM-DD format.
    :param end_date: The end date for the data in YYYY-MM-DD format.
    :return: Dictionary of stock data for compliant stocks.
    """
    compliant_stocks_data = {}
    for stock in stocks:
        if is_sharia_compliant(stock):
            stock_data = get_stock_data(stock, start_date, end_date)
            compliant_stocks_data[stock] = stock_data
    return compliant_stocks_data


def save_data_to_csv(data_dict):
    """
    Saves stock data to CSV files with filenames that include the current date.

    :param data_dict: Dictionary of stock data.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    for ticker, data in data_dict.items():
        filename = f"{ticker}_{current_date}.csv"
        data.to_csv(filename)
        print(f"Saved data for {ticker} to {filename}")


# Example usage:
start_date = "2023-01-01"
end_date = "2023-12-31"

sharia_compliant_stocks_data = get_sharia_compliant_stocks(
    german_stocks, start_date, end_date)

save_data_to_csv(sharia_compliant_stocks_data)
