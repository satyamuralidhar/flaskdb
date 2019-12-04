from flask import Flask , render_template, request, redirect
from flaskext.mysql import MySQL
import mysql.connector

import pymysql

app = Flask(__name__)
#app = Flask(__name__)
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] ='root'
#app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
#mysql = MySQL(app)

db = pymysql.connect("localhost", "root", "root", "flaskapp")

@app.route("/" ,methods=['GET', 'POST'])
def create_table():
   if request.method == 'POST':
      userDetails = request.form

      name = userDetails['name']

      email = userDetails['email']

      cur = db.cursor()

      cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))

      db.commit()

      cur.close()

      return 'success'
   return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
