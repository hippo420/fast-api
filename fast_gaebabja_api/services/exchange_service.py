import FinanceDataReader as fdr

def get_exchange_rate(currency: str):
    try:
        exchange = fdr.DataReader(currency)
        latest_rate = exchange.iloc[-1]["Close"]
        return latest_rate
    except Exception as e:
        return f"Error fetching exchange rate: {e}"
