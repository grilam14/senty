# senty
CSCI 3308 SD project

This site helps users make investment decisions by providing a general overview of the public's opinion on a publicly traded company. This is done by using running sentiment analysis on articles published on SeekingAlpha.com, as well as tweets in order to summarize the sentiment the public has for the company.

The sentiment analysis was contained in three .py files, bot_detect, scoreCalculate, and twitterSentiment.  That way we can discard those opinions. ScoreCalculate webscrapes the website SeekingAlpha and calculates a polarity score through TextBlob. TwitterSentiment searches what the public's opinion is on a certain company is in real time, then it's given a score depending on what the public thinks on the company. bot_detect checks if tweets are coming from people or bots, and discards bot tweets. The final score from scoreCalculate and twitterSentiment will be classified in three sections according to the general opinion, neutral, negative, or positive.

Inside the ProjectWebsite folder we have three main folders: SQL, static and templates. The database for the site is called 'project,', users in 'user_tbl,', scores in 'scores.' Inside the static folder we have two folders: css and jss. The css styles the HTML pages. The login page is in charge of letting you log in with a username and password you already have created. The signup page allows you to create a new account with a username and a password of your choice. Then the error page is the page you will be redirected to if your login or register fails.

The README for how to run the project is in ProjectWebsite.
