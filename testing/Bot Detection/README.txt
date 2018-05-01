To run these tests: 

1. Install dependencies for bot_detect:
	pip install botometer
	pip install tweepy
	pip install mysql-connector-pythoon
	
2. config.py:
	bot_detect uses a config.py file containing necessary api keys and database parameters.
	Modify the provided config_template.py file and rename as config.py for the algorithm to function

3. Database:
	Run the sql script in this folder before running tests to populate database with necessary 
	twitter accounts.
	
4. Execute tests:
	python test_bot_detect.py