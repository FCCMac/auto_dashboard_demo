import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
import datetime
import os
from dotenv import load_dotenv
import datapane as dp

load_dotenv()

symbol = 'AAPL'
start = datetime.datetime.now() - datetime.timedelta(days=365)
end = datetime.datetime.now()

tickerData = yf.Ticker(symbol)
df = tickerData.history(period='1d', start=start, end=end)
df['10ma'] = df['Close'].rolling('10d').mean()
df['20ma'] = df['Close'].rolling('20d').mean()

fig = px.line(df, x=df.index, y='Close', template='ggplot2')
fig.add_trace(go.Line(x=df.index, y=df['10ma'], name='10ma'))
fig.add_trace(go.Line(x=df.index, y=df['20ma'], name='20ma'))
fig.update_layout(
    title={
        'text': f'{symbol} Price'
    }
)

dp.Report(
    dp.Blocks(
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        dp.Plot(fig),
        columns=2,
        rows=4
    ), dp.Plot(fig)
).publish(name='stock_report', open=True)
