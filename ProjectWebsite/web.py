
from flask import Flask, render_template, json, request, redirect, session, url_for
from flask import Flask, render_template, json, request, redirect, url_for
from flaskext.mysql import MySQL
#from flask_login import LoginManager, current_user, login_required, login_user, logout_user, UserMixin, AnonymousUserMixin, confirm_login, fresh_login_required
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from ScoreCalculate import scoreCalculate
import twitterSentiment
from config import *


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = SQL_CONFIG['password'] # put your sql password here
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/", methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        print('here')
        conn = mysql.connect()
        cur = conn.cursor()
        twitterScore = twitterSentiment.main()
        newticker = request.form['ticker']
        uID = 1#this needs to be changed when we get login working

        newscore = scoreCalculate(newticker)
        cur.execute("INSERT INTO scores (ticker,score,twitterScore, user_ID) VALUES (%s, %s, %s, %s)", (newticker, newscore, twitterScore, uID))
        print('added')
        conn.commit()
        cur.close()

        return redirect('/')

    else:
        print('rendering Senty.html')
        return render_template('Senty.html') 

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        if session.get('user'):
            return render_template('home.html')
        else:
            return render_template('error.html',error = 'Unauthorized Access')

    else:
        return redirect('/result')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        conn = mysql.connect()
        cur = conn.cursor()
        newticker = request.form['ticker']
        twitterScore = twitterSentiment.main(newticker)
        uID = -1
        if session.get('user'):
            uID = int(session['user'])
        newscore = scoreCalculate(newticker)
        cur.execute("INSERT INTO scores (ticker,score,twitterScore, user_ID) VALUES (%s, %s, %s, %s)", (newticker, newscore, twitterScore, uID))
        print('added')
        conn.commit()
        cur.close()
        return render_template('result.html', tScore = twitterScore, 
            nScore = newscore, company = newticker)
    else:
        return redirect('/home')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


@app.route('/showSignIn')
def showSignIn():
    if session.get('user'):
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
 
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()

        cursor.close()
        con.close()
 
        if len(data) > 0:
            print (data[0][1])
            print (data[0][2])
            print (data[0][3])
            if str(data[0][3]) ==_password:
                session['user'] = data[0][0]
                return redirect(url_for('home'))
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')
    except Exception as e:
        return render_template('error.html',error = str(e))


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    
    # still need to create signup class and transfer below code to new file
    conn = mysql.connect()
    cur = conn.cursor()
    #code=307 runs homepage without updating the actual page your on. So weird. 
    #return redirect(url_for('main'))

    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            print(_name, _email, _password)
            
            cur.callproc('sp_createUser',(_name,_email,_password,))
            print ("Registered")
            data = cur.fetchall()

            conn.commit()
            cur.close() 
            conn.close()
            json.dumps({'message':'User created successfully !'})
            print('redirecting')
            return redirect(url_for('index'))


        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    else:
        return render_template('signup.html')


if __name__ == "__main__":
    
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()