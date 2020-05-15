#question2
#connect to mysql and store the fetched json data in the table

#import mysql modules
import mysql.connector
import MySQLdb

#creating instance 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
)

#creating cursor
mycursor = mydb.cursor()

#creating a database
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")

#using database
mycursor.execute("use mydatabase")


#creating table
mycursor.execute("DROP TABLE IF EXISTS Covid_Tab")
mycursor.execute("CREATE TABLE Covid_Tab (Country VARCHAR(255), Date DATE, 
Confirmed INTEGER , Deaths INTEGER , Recovered INTEGER )")

#inserting values into table
mycursor.execute("INSERT INTO Covid_Tab(Country,Date,Confirmed,Deaths,Recovered) values(?,?,?,?,?)", row['Country'], row['Date'], row['Deaths'], row['Recovered'])
