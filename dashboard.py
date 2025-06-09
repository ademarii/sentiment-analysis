import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from stream_sentiment import tweet_queue
import threading
import pandas as pd
import time

# Data buffer
data = {
    "positive": 0,
    "negative": 0,
    "neutral": 0,
    "tweets": []
}

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("📊 Real-Time Twitter Sentiment"),
    dcc.Graph(id='sentiment-pie'),
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
])

@app.callback(Output('sentiment-pie', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph(n):
    # Drain tweets from the queue
    while not tweet_queue.empty():
        text, sentiment = tweet_queue.get()
        data[sentiment] += 1
        data["tweets"].append((text, sentiment))

    fig = go.Figure(data=[
        go.Pie(labels=['Positive', 'Negative', 'Neutral'],
               values=[data['positive'], data['negative'], data['neutral']],
               hole=.3)
    ])
    fig.update_layout(title="Sentiment Distribution (Live)")
    return fig

if __name__ == '__main__':
    threading.Thread(target=lambda: __import__('stream_sentiment')).start()
    app.run_server(debug=True)
