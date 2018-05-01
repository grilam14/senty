Details

This program creates an SQL database containing emails, names, and passwords 
and integrates it with an html website with three pages (home, login, signup).

There are four components to this:
1) MySQL
2) HTML/CSS
3) JavaScript
4) Python(Flask)
5) Install modules

Parts:
1) Open MySQL or MySql Workbench and run the sql script. It does the following:
   i) Creates a database to store all the data for the website (named 'project')
   ii) Creates a table to store the users (named 'tbl_user'), to hold users
   iii) Creates a table to store the users (named 'scores'), to hold company scores
   iv) Creates a stored procedure to check if a given username (email address) exists in
	the database. If this is the case, it returns an error, indicating that the given
	username is already in the database, if not, it adds the new user's information
	(name, email, password) to the database.
   v) Creates a stored procedure to check if a given username (email address) exists in
	the database. If this is the case, return their password.
   
   Addtionally, run the bot.sql and twitter_users.sql scripts. bot.sql creates a table
   to hold information about twitter accounts analyzed through Botometer. twitter_users.sql
   populates this table with information about roughly ~6000 twitter accounts


2) There is an HTML file and accompanying CSS file for each page on the website 
   (e.g. logIn, signUp, Home). I made minor changes to the Senty.HTML file 
   (changed the href addresses, e.g. 'kenny' to 'logIn', added home link) and
    made no changes to the other HTML/CSS files.

3) I use jQuery AJAX to send the signup request to the python function. This is done
   in the signUp.js file, the other two files are generic jQuery files.

4) To integrate all of these parts I used flask, a microframework for python thats
   relatively easy to learn.
   To use flask, you have to download it on the terminal with the following commands(linux):
	sudo pip install flask
	sudo pip install flask-mysql

5) Install all necessary dependencies
   In terminal:
   pip install mysql-connector-python
   pip install tweepy
   pip install botometer
   pip3 install feedparser
   pip3 install requests
   pip3 install regex
   pip3 install textblob
   pip3 install beautifulsoup4
   
6) Set up config.py file:
   Modify the provided config_template.py file with the necessary information (keys, password, ect.), then rename this file to 
   config.py. config.py is necessary to set up the database as well as provide authorization for the APIs
   used in the website programming.
   
7) Lastly, just run the command "python web.py", and the content from the code will be loaded
   onto a local webserver, the URL for mine is "http://127.0.0.1:5000/". The site has three
   pages and supports adding new users, logging in, and performing searches for companys' sentiment.
