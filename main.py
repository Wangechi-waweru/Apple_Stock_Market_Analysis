from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go


app = Dash(__name__)

app.layout = html.Div([
    html.H4('Apple stock candlestick chart'),
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider',
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input("toggle-rangeslider", "value"))
def display_candlestick(value):
    data = pd.read_csv("C:/Users/Administrator/Downloads/AAPL.csv")
    data = data.dropna()

    fig = go.Figure(go.Candlestick(x=data['Date'],
                                   open=data['Open'],
                                   high=data['High'],
                                   low=data['Low'],
                                   close=data['Close']
                                   ))
    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig


app.run_server(debug=True)
