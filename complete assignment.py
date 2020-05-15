import requests
from flask import Flask,render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import text
import mysql.connector
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine
from pandas.io.json import json_normalize

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("use mydatabase")
mycursor.execute("DROP TABLE IF EXISTS Covid_Tab")
mycursor.execute("CREATE TABLE Covid_Tab (Country VARCHAR(255), Date DATE, Confirmed INTEGER , Deaths INTEGER , Recovered INTEGER )")

df = pd.DataFrame(r)
print(df.head())
#mycursor.execute("INSERT INTO Covid_Tab(Country,Date,Confirmed,Deaths,Recovered) values(?,?,?,?,?)", row['Country'], row['Date'], row['Deaths'], row['Recovered'])
print(df.columns)

@app.route('/',methods = ['GET','POST'])
def _home():
    print(df.head())
    print(df.columns)
    for index, row in df.iterrows():
        print(row)
   
if __name__ == "__main__":
   app.run(debug=True)
