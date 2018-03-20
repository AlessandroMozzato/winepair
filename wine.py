import pandas as pd

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/csv')
def read_csv():
   df = pd.read_csv('/Users/am8e13/wine-data/wine-insight/Data_winedatasetv3.csv')
   return df['Wine Name'].values[1]

if __name__ == '__main__':
   app.run(debug = True)