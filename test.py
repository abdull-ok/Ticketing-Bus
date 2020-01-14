from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'tiket'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tiketbus'


mysql = MySQL(app)

@app.route('/tiketbus/', methods=['GET', 'POST'])
def login():

    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

@app.route('/tiketbus/logout')
def logout():

   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))

@app.route('/tiketbus/register', methods=['GET', 'POST'])
def register():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'telp' in request.form:

        username = request.form['username']
        password = request.form['password']
        telp = request.form['telp']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO accounts(username, password, telp) VALUES (%s, %s, %s)",
                     (username, password, telp))
        mysql.connection.commit()
        cur.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/tiketbus/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/tiketbus/profile')
def profile():

    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

@app.route('/tiketbus/jenis')
def jenis():
    return render_template('jenis.html')

@app.route('/tiketbus/pemesanan', methods=['GET','POST'])

def pemesanan():

    if request.method == 'POST':
        hasil = request.form
        nobus = hasil['nobus']
        tanggal =  hasil['tanggal']
        if nobus == 'J001' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

        if nobus == 'J002' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

        if nobus == 'J003' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

        if nobus == 'J004' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

        if nobus == 'J005' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

        if nobus == 'J006' :
            cur = mysql.connection.cursor()
            print(nobus)
            cur.execute("SELECT id from accounts ORDER BY id DESC LIMIT 1")
            id = cur.fetchone()
            print(id)
            cur.execute("INSERT INTO tiket(nobus, id, tanggal) VALUES (%s, %s, %s)",
                 (nobus, id, tanggal))
            mysql.connection.commit()
            cur.close()

    return render_template('pemesanan.html')

@app.route('/tiketbus/cek')
def cek():

    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tiket WHERE id = %s', [session['id']])
        tiket = cursor.fetchone()
        return render_template('cek.html', tiket=tiket)
    return redirect(url_for('login'))










