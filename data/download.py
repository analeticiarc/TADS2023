import pandas as pd
import yfinance as yf

def download_data(ticket: str) -> pd.DataFrame:
    """

    Args:
        ticket (str): _description_

    Returns:
        pd.DataFrame: _description_
    """

    data = yf.download(ticket)
    return data