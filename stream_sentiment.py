import tweepy
import threading
from queue import Queue
from utils import analyze_sentiment

# Twitter API credentials
BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"

# Shared queue
tweet_queue = Queue()

class TweetStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.referenced_tweets is None:  # skip retweets
            sentiment = analyze_sentiment(tweet.text)
            tweet_queue.put((tweet.text, sentiment))
            if tweet_queue.qsize() > 5000:
                tweet_queue.get()  # trim to 5000 max

def start_stream():
    stream = TweetStream(BEARER_TOKEN)
    stream.add_rules(tweepy.StreamRule("product launch lang:en -is:retweet"))
    stream.filter(tweet_fields=["text"], threaded=True)

if __name__ == "__main__":
    start_stream()
