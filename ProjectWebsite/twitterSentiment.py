import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
    def __init__(self):
        # keys and tokens
        consumer_key = 'XDeWp3DBNl42PflxpUp19MJg9'
        consumer_secret = 'tXBg53eaf1Yqb4F1m47GGL8B79fNsOtln4Z8RajhEvALvp1gZT'
        access_token = '973339215587979264-qVeUpYwoo87VXfVu1F5GEWF9x3yyRAk'
        access_token_secret = 'k3VETXF8npX1FIs1VSF2dSVfT2VKWELIYZQAnykVjRYbQ'

        # authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        # Remove links and special characters from tweet

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        # get sentiment with textblob library

        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0.01:
            x = ['positive', analysis.sentiment.polarity]
            return x
        elif analysis.sentiment.polarity == 0:
            x = ['neutral', analysis.sentiment.polarity]
            return x
        else:
            x = ['negative', analysis.sentiment.polarity]
            return x

    def get_tweets(self, query, count):
        # empty list to store parsed tweets
        tweets = []

        try:
            # get tweets
            new_tweets = self.api.search(q=query, count=count, lang='en', tweet_mode='extended', include_rts=True)

            for tweet in new_tweets:
                # dictonary of tweets with text and sentiment
                parsed_tweet = {}
                # get full text of tweet
                try:
                    if tweet.retweeted_status:
                        parsed_tweet['text'] = tweet.retweeted_status.full_text
                except:
                    parsed_tweet['text'] = tweet.full_text
                # get sentiment measure
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.full_text)

                # add unique tweets
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def print_tweets(ptweets, ntweets, neutweets):
    print("\n\nPositive tweets:")  # self.clean_tweet(tweet)
    for tweet in ptweets[:5]:
        print(ptweets.index(tweet) + 1, ' ', clean_tweet(tweet['text']))
    print("\n\nNegative tweets:")
    for tweet in ntweets[:5]:
        print(ntweets.index(tweet) + 1, ' ', clean_tweet(tweet['text']))
    print("\n\nNeutral tweets:")
    for tweet in neutweets[:5]:
        print(neutweets.index(tweet) + 1, ' ', clean_tweet(tweet['text']))


def main():
    api = TwitterClient()
    tweets = api.get_tweets(query='TESLA', count=100)

    # get positive tweets and print their percentage
    ptweets = [tweet for tweet in tweets if tweet['sentiment'][0] == 'positive']
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # get negative tweets and print their percentage
    ntweets = [tweet for tweet in tweets if tweet['sentiment'][0] == 'negative']
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # get neutra; tweets and print their percentage
    neutweets = [tweet for tweet in tweets if tweet['sentiment'][0] == 'neutral']
    print("Neutral tweets percentage: {} % \
        ".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    # printing first 5 positive, negative, and neutral tweets
    print_tweets(ptweets, ntweets, neutweets)
    s = 0
    i = 0
    for tweet in tweets:
        if tweet['sentiment'][0] != 'neutral':
            x = 100*tweet['sentiment'][1]
            s+=x
            i+=1
    avgScore = s/i
    return(avgScore)
 

if __name__ == "__main__":
    # calling main function
    main()
