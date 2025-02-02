import FinanceDataReader as fdr

def get_stock_price(code: str):
    try:
        stock = fdr.DataReader(code)
        latest_price = stock.iloc[-1]["Close"]
        return latest_price
    except Exception as e:
        return f"Error fetching stock price: {e}"
