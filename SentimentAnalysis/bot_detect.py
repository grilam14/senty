import json
import botometer
# the botometer library must be install by running the command:
# pip install botometer
# int the terminal in order for this method to function


# acc_name is the @accountname or account ID (from tweet data)
# for a single twitter account
#
# returns the unviersal bot score from botometer from 0-1, where larger
# values indicate a higher likelihood of the account being a bot

def bot_detector(acc_name):
	# keys acquired from mashape marketplace and twitter's developer program
	mashape_key = 'Qd8Lh3avPDmshLjJIeQzGyr2qHRcp1mSjbwjsnv4QJO3fUlQ1p'
	twitter_app_auth = {
		'access_token': '2852131812-dIlDgWIm65Xi5cKiDGgK3nsaRBYcdjH2JJ4hZYL',
		'access_secret': 'uGHDZuS3uDaION8GnHwlOg3nCtzF3t5OrOJhSAoP7R4Of',
		'consumer_key': '5S9D6TlASa3I4B5IkMYlQ3KWX',
		'consumer_secret': 'ruxsdIseFAdT35lt0dF97hotZ3w89AdyZURI4Mv6dOKYHcnFmw',
	}

	meter = botometer.Botometer(mashape_key = mashape_key, **twitter_app_auth)

	acc_score = json.dumps(meter.check_account(acc_name))
	return json.loads(acc_score.strip())['scores']['universal']

