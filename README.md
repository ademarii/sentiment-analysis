# sentiment-analysis
Sentiment Analysis for Twitter

project/
│
├── stream_sentiment.py      # Twitter stream processor
├── dashboard.py             # Real-time Plotly Dash dashboard
└── utils.py                 # Sentiment analysis logic


What This Does
- Streams 5,000+ tweets per minute using Twitter’s filtered stream (note: actual rate depends on your access level)
- Analyzes each tweet using VADER sentiment analysis
- Queues results in real-time using a Queue
- Dash app updates pie chart every 2 seconds

