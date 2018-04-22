To run these tests: 

1. Install dependencies for bot_detect:
	pip install botometer
	pip install tweepy
	pip install mysql
	
2. config.py:
	bot_detect uses a config.py file containing necessary api keys and database parameters.
	This file will be emailed to the TA.

3. Database:
	Run the sql script in this folder before running tests to populate database with necessary 
	twitter accounts.