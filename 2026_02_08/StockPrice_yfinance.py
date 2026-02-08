import yfinance as yf
import pandas as pd

pd.set_option('display.max_rows', None)
df = yf.download( '2330.TW', start = '2019-01-01', end = '2026-02-08' )
print( df )