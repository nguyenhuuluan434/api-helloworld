#!/usr/bin/python
import psycopg2
import pprint

def getData(req):
	#Define connection string
	conn_string = "host='127.0.0.1' dbname='abc' user='luannh' password='1234@qwer'"
 
	# get a connection
	conn = psycopg2.connect(conn_string)
 
	#cursor object to interactive with database
	cursor = conn.cursor()
	# execute our Query
	query = """SELECT * FROM yeah1 WHERE content = '""" + str(req) + """';"""
	cursor.execute(query)
	records = cursor.fetchall()
	return records
