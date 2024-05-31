import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from scipy.signal import convolve

def Plot(Y, Y2 = None, X = None, name_Y = 'Y', name_Y2 = 'Y2'):
    if Y2 is None:
        Y_name = Y.name if isinstance(Y, pd.Series) else name_Y
        go.Figure(go.Scatter(x = X, y = Y, mode = 'lines+markers', name =Y_name)
        ).update_yaxes(title_text = Y.name
        ).show()
    if Y2 is not None:
        Y_name = Y.name if isinstance(Y, pd.Series) else name_Y
        Y2_name = Y2.name if isinstance(Y2, pd.Series) else name_Y2
        fig = make_subplots(specs = [[{'secondary_y': True}]])
        fig.add_trace(go.Scatter(x = X, y = Y, mode = 'lines+markers',name = Y_name),secondary_y=False)
        fig.add_trace(go.Scatter(x = X,y = Y2, mode = 'lines+markers',name = Y2_name),secondary_y=True)
        fig.update_yaxes(title_text = Y_name, secondary_y=False)
        fig.update_yaxes(title_text = Y2_name, secondary_y=True)
        fig.show()

def calcualte_slope(df, n = 2, Name_Time = 'Minute', Name_TMP = 'TMPmbar'):
    slopes = np.zeros(len(df))
    for i in range(n,len(df)):
        x = df[Name_Time].iloc[i-n:i+1]
        y = df[Name_TMP].iloc[i-n:i+1]
        coeff = np.polyfit(x,y,1)
        slopes[i] = coeff[0]
    return slopes

def rolling_mean_centered(x, window):
    weights = np.ones(window) / window
    return convolve(x, weights, mode='same')