Details

This program creates an SQL database containing emails, names, and passwords 
and integrates it with an html website with three pages (home, login, signup).

There are four components to this:
1) MySQL
2) HTML/CSS
3) JavaScript
4) Python(Flask)

Parts:
1) Open MySQL or MySql Workbench and run the sql script. It does the following:
   i) Creates a database to store all the data for the website (named 'project')
   ii) Creates a table to store the users (named 'tbl_user')
   iii) Create a stored procedure to check if a username (email address) exists in
	the database. If this is the case, it returns an error, if not, it adds the
	new user's information (name, email, password) to the database.

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
   
   The python file that contains the integration code is named web.py, in it, you'll need
   to type in your password on line 9, where the password variable is assigned. MAKE SURE
   YOU DO NOT PUSH THE FILE BACK UP TO GITHUB WITH YOUR PASSWORD STILL TYPED IN, if you do,
   you're gonna have a baaad time and probably get your password stolen.

5) Lastly, just run the command "python web.py", and the content from the code will be loaded
   onto a local webserver, the URL for mine is "http://127.0.0.1:5000/". The site has three
   pages and supports adding new users to the 'tbl_user' sql table.
