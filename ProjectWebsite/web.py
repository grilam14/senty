
from flask import Flask, render_template, json, request, redirect, session, url_for
from flask import Flask, render_template, json, request, redirect, url_for
from flask.ext.mysql import MySQL
#from flask_login import LoginManager, current_user, login_required, login_user, logout_user, UserMixin, AnonymousUserMixin, confirm_login, fresh_login_required
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from ScoreCalculate import scoreCalculate
import twitterSentiment


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # put your sql password here
app.config['MYSQL_DATABASE_DB'] = 'project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/")
def main():
     return(render_template('Senty.html'))

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



@app.route('/showSignIn')
def showSignIn():
    if session.get('user'):
        return render_template('Senty.html')
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
 
        if len(data) > 0:
            if str(data[0][3]) ==_password:
                session['user'] = data[0][0]
                return redirect('/')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()
    

@app.route('/showSignUp')
def showSignUp():

    return (render_template('signup.html'))
    


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    # still need to create signup class and transfer below code to new file
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('sp_createUser',(_name,_email,_password,))
            print "Registered"
            data = cur.fetchall()

            if len(data) is 0:
                conn.commit()
                return(json.dumps({'message':'User created successfully !'}))
            else:
                return(json.dumps({'error':str(data[0])}))
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cur.close() 
        conn.close()


if __name__ == "__main__":
    
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()
