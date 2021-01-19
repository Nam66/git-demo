import mysql.connector
import csv
import datetime

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "nam123",
	database = "testdb"
	)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customerscsv2 (customerid INT PRIMARY KEY, firstname VARCHAR(50), lastname VARCHAR(50), companyname VARCHAR(255), billingaddress1 VARCHAR(255), billingaddress2 VARCHAR(255), city VARCHAR(255), state VARCHAR(255), postalcode VARCHAR(20), country VARCHAR(255), phonenumber VARCHAR(20), emailaddress VARCHAR(255), createdate DATETIME)")
fieldnames = []
rows = []
with open("D:\\python\\customer.csv", "r") as csvfile:
	file_content = csv.reader(csvfile)
	#skip the firs row of the csv file
	fieldnames = next(file_content)
	for row in file_content:
		rows.append(row)
query = "INSERT INTO customerscsv VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
for row in rows:
	row[-1] = datetime.datetime.strptime(row[-1], '%d/%m/%Y %H:%M')
mycursor.executemany(query, rows)
mydb.commit()