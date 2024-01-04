import plotly.express as px
from data.download import download_data

def plot_line(ticker: str):
    """interactive plot

    Args:
        ticker (str): ticker to show

    Returns:
        _type_: a figure
    """
    data = download_data(ticker)
    fig = px.line(
        data.reset_index(),
        x='Date', y='Close', title=ticker,
        labels={'Close': 'Fechamento', 'Date': 'Data'}
    )
    return fig