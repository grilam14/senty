import json
import botometer
from config import *
import mysql.connector


# acc_name is the @accountname or account ID (from tweet data)
# for a single twitter account
#
# returns the unviersal bot score from botometer from 0-1, where larger
# values indicate a higher likelihood of the account being a bot

def bot_detector(acc_name):
	mashape_key = MASHAPE_KEY
	twitter_app_auth = TWITTER_AUTH
	db = mysql.connector.connect(**SQLconfig)

	cursor = db.cursor()
	query = "SELECT is_bot FROM accounts WHERE name = " + "'" + acc_name + "'"
	cursor.execute(query)
	result = cursor.fetchone()

	if result is None: #account not yet in database, get score and add to DB
		meter = botometer.Botometer(mashape_key = mashape_key, **twitter_app_auth)

		acc_score = json.dumps(meter.check_account(acc_name))
		acc_score = json.loads(acc_score.strip())['scores']['universal']

		if float(acc_score) < 0.66:
			is_bot = 0
		else:
			is_bot = 1

		add_acc = "INSERT INTO accounts (name, is_bot) VALUES(%s,%s)"
		cursor.execute(add_acc, (acc_name, is_bot))
		db.commit()
		return is_bot
		print is_bot
	else: #account already checked, return pre-determined bot score
		return result[0]



print bot_detector('@realdonaldtrump')