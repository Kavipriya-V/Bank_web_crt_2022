from flask import *
from random import randint
from face_detection import *
from face_reg import *
import sqlite3 as sql
from datetime import datetime
app = Flask(__name__)
import smtplib
app.secret_key="panda"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        bname = request.form['bname']
        aadhar = request.form['aadhar']
        def random_with_N_digits(n):    
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        a=random_with_N_digits(16)
        pin = random_with_N_digits(4)
        print(pin)
        val = get(username)
        if val =='your not allowed to register':
                    error = 'already registered'
                    return render_template("register.html",register_error1=error)
        else:
            con = sql.connect('bank.db')
            cur =con.cursor()
            cur.execute('insert into register(acc_no,pin,name,email,username,password,phone,bname,aadhar,amount) values(?,?,?,?,?,?,?,?,?,?)',(a,pin,name,email,username,password,phone,bname,aadhar,5000))
            con.commit()
            return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        print(name)
        password = request.form['password']
        con  = sql.connect('bank.db')
        cur = con.cursor()
        cur.execute('select username,password,acc_no,pin from register where username=? and password=?',(name,password))
        data = list(cur.fetchone())
        p = data[3]
        ano = data[2]
        
        print(data)
        con.commit()
        ac = face_reg(name)
        print(ac)
        if ac == 'Unauthorized':
            return render_template('login.html',error='error')
        elif ac == 'Authorized':
            session['name'] =name
            session['password'] =password
            session['pin'] = p
            session['ano'] = ano
            print(type(session['ano']))
            print(type(session['pin']))
            print('auth')
            return render_template('home.html',name=name,acc_no=data[2],pin=data[3] )
        elif ac=='Invalid User':
            return render_template('login.html',invalid='invalid')
    return render_template('login.html')


@app.route('/home',methods=['POST','GET'])
def home():
    session['acc_no'] = acc_no
    session['f_name'] = f_name
    session['r_name'] = r_name
    session['to_acc'] = to_acc
    session['amount'] = amount
    session['now'] = now
    name = session['name'] 
    return render_template('home.html',name=session['name'],acc_no=session['ano'],pin=session['pin'])



if __name__ == '__main__':
    app.run(debug=True)