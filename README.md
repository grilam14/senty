# senty
CSCI 3308 SD project

The Objective of our project (Senti) is to make investing more accesible to everyone
by offering this free online service. This service helps users in making investment
decisions by providing a general overview of the publics opinion on a cerain company.
The way this is done is by using web scraping and sentment analysis on certain articles
online and tweets in order to summarize the publics opinion a the company you searched for.

When it comes to Sentiment Analysis we created three py files, bot_detect, ScoreCalculate,
and twitterSentiment. We use the bot_detect file to detect if the opinions of certain 
account are actually bots, that way we can discard those opinions. We use ScoreCalculate
to search what the general public thinks about a selected company on websites and then give
it a score depending on how positive or negative the reviews are. We use twitterSentiment
to search what the publics opinion on a certain company is in real time, then we give it a 
score depending on what the public thinks on the company. The final score will be classified
in three sections according to the general opinion, neutral, negative or positive.

Inside the ProjectWebsite folder we have three main folders: SQL, static and templates.
Inside the SQL folder we have a SQL file called 'project'which will keep track of all the user's
information. Inside the static folder we have two folders: css and jss. The css file will 
be incharged of the style of the login, Senty and signup pages. Inside the templates folder
we have the following HTML files: error, home, login, signup, result. Then we have debug.log.
The home page is the main page you see when you enter our projects website. The login page is incharged
of letting you log in with a user name and password you already have created. The signup page allows
yo to create a new account with a username and a password of your choice. Then the error page is the
page you will be redirected to if your login or register fails. Ten we have the debug.log which function
is to debug.
