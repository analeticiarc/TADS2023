import yfinance as yf
from plotnine import *

data = yf.download('bbas3.sa')

ggplot(
    data=data.reset_index(),
    mapping=aes(x='Date', y='Close')
) + \
    geom_line() + \
    ggtitle("Dados históricos do BBAS3") + \
    xlab('Data') + \
    ylab('Fechamento')

############################
import plotly.express as px
from data.download import download_data

# data = download_data("bbas3.sa")

from plot.interactive import plot_line
plot_line("BBAS3.SA")
