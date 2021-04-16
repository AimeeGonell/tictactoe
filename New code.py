#APIs python code

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# Extract Ethereum Data from CoinGecko website
ether_data = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='eur', days=30)
ether_price_data = ether_data['prices']

data = pd.DataFrame(ether_price_data, columns=['Timestamp', 'Price'])
data['Date'] = pd.to_datetime(data['Timestamp'], unit='ms')
data.head()