import streamlit as st
from plot.interactive import plot_line

st.title('Stock Price App')

# Sidebar
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

# Plot
fig = plot_line(symbol)
st.plotly_chart(fig)
