import json
import botometer # pip install botometer
import mysql.connector # pip install mysql-connector-python
import difflib
import tweepy # pip install tweepy
from tweepy import OAuthHandler
from datetime import date
from config import * # config contains API keys and database parameters



class BotDetector(object):

	# API authorization and databsae initializiation
	def __init__(self):
		#from config
		mashape_key = MASHAPE_KEY
		twitter_app_auth = TWITTER_AUTH
		SQL_config = SQL_CONFIG
		
		self.db = mysql.connector.connect(**SQL_config)

		self.meter = botometer.Botometer(mashape_key = mashape_key, 
			**twitter_app_auth)
		
		self.auth = OAuthHandler(TWITTER_AUTH['consumer_key'], 
			TWITTER_AUTH['consumer_secret'])
		self.auth.set_access_token(TWITTER_AUTH['access_token'], 
			TWITTER_AUTH['access_secret'])

		self.api = tweepy.API(self.auth)


	# returns count tweets with query as search term
	# used mostly for testing and populating database
	def get_tweets(self, query, count):
		new_tweets = self.api.search(q=query, count=count, 
			lang='en', tweet_mode='extended', include_rts=True)
		return new_tweets

	# gets single twitter user with user_id
	# used mostly for testing
	# user_id can be twitter account id, screen_name, or name
	def get_user(self, user_id):
		return self.api.get_user(user_id)


	# checks for twitter account in database
	# returns tuple with Botometer score (if available) and is_bot boolean
	# returns None if account is not in db
	def check_db(self, acc_id): 
		cursor = self.db.cursor()
		query = "SELECT bot_score, is_bot FROM twitter_users WHERE account_id = "
		query = query + "'" + str(acc_id) + "'"
		cursor.execute(query)
		return cursor.fetchone()


	# adds account to database
	def add_to_db(self, user, score, is_bot):
		query = """INSERT INTO twitter_users (account_id, 
			account_name, bot_score, is_bot) VALUES(%s,%s,%s,%s)"""

		cursor = self.db.cursor()
		cursor.execute(query, (user.id, user.screen_name, 
			score, is_bot))
		self.db.commit()


	# checks account with botometer API
	def get_score(self, acc_id):
		result = json.dumps(self.meter.check_account(acc_id))
		result = json.loads(result.strip())
		return result


	# checks similarity of tweets from twitter account with account id acc_id
	def check_similarity(self, acc_id):
		timeline = self.api.user_timeline(acc_id)

		statuses = []
		s_count = 0
		tot = 0
		tot_score = 0.0

		for tweets in timeline:
			statuses.append(tweets)
			s_count += 1

		for x in range(0,s_count):
			for y in range(0,s_count):
				if x != y:
					tot_score += difflib.SequenceMatcher(None, 
						statuses[x].text, statuses[y].text).ratio()
					tot += 1

		if tot == 0:
			return 0
		else:
			return (tot_score/tot)


	# calculates the average number of tweets posted by the account per day
	def tweets_per_day(self, user):
		s_count = float(user.statuses_count)
		acc_age = float((date.today() - user.created_at.date()).days)

		if acc_age == 0:
			acc_age += 1

		return (s_count/acc_age)


	# main function to check accounts
	# takes as input tweet object returned from tweepy search function
	# returns boolean value, True if account determined to be a bot, 
	# False if not a bot
	# Checks DB for account match with Botometer score. Uses faster, 
	# less accurate checks if no score is found
	def bot_check(self, user):
		# check if account is in database
		response = self.check_db(user.id)

		if response is None: #account not in DB, use quick checks
			tpd = self.tweets_per_day(user)

			is_bot = False

			if tpd > 50:
				sim = self.check_similarity(user.id)
				if sim > 0.40:
					is_bot = True
				if tpd > 100:
					is_bot = True
			if user.id != 25073877: # @realdonaldtrump, must not be in db for testing
				self.add_to_db(user, 0, is_bot)

			return is_bot

		else: # account already in DB, get pre-determined bot score
			if response[0] == 0: # account was not scored with Botometer
				return bool(response[1])
			elif response[0] < 0.43:
				return False
			else:
				return True

def main():
	detecto = BotDetector()
	tweets = detecto.get_tweets('google', 100)
	for tweet in tweets:
		print detecto.bot_check(tweet.user)

if __name__ == '__main__':
	main()