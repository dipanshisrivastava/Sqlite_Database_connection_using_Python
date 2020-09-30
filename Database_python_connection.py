import sqlite3
import os
from sqlite3 import Error

# Used to create connection with Database file 
def create_connection(Education):
	conn = None
	try:
		conn = sqlite3.connect(Education)
	except Error as e:
		print(e)
	return conn

# Used to Select the Column Names from table 
def select_task(conn,table_name,col_name,where_clause):
	cur = conn.cursor()
	str_query = "SELECT "
	print("After adding select keyword ",str_query)

	#string for all the relevent columns of the table:
	str_column_list = ""
	# SELECT Roll_Number,a,b,c FROM Student
	for i in range(len(col_name)):
		str_column_list = str_column_list + col_name[i]
		print(str_column_list)
		if i != len(col_name)-1:
			str_column_list = str_column_list + ","

	print( " Column Names are ",str_column_list)

	str_query = str_query + str_column_list
	print( " Now Query is ",str_query)

	str_query = str_query + " FROM " + table_name + " "

	print( " Now Query is ",str_query)

	if where_clause != "":
		str_query = str_query + " WHERE " + where_clause

	print( " Now Query is ",str_query)
	cur.execute(str_query)
	rows = cur.fetchall()
	for row in rows:
		print(row)

def delete_task(conn,table_name,where_clause):
	cur = conn.cursor()
	#DELETE FROM Student where Subject_ID=2
	str_query = ""
	if where_clause != "":
		str_query = str_query + "DELETE FROM " + table_name + " WHERE "+ where_clause
	else:
		str_query = str_query + "DELETE FROM " + table_name
		
	print( " Now Delete Query is ",str_query)
	cur.execute(str_query)
	rows = cur.fetchall()
	for row in rows:
		print(row)

# update tb set c1 = c1_val , c2 = c2_val WHERE c_name = c_name_value
def update_task(conn,table_name,col_name,data,where_clause):
	cur = conn.cursor()
	str_query = "update "+ table_name+ " set "

	for i in range(len(col_name)):
		str_query = str_query + col_name[i] + " = '"+ data[i] + "'"
		if i != len(col_name)-1:
			str_query = str_query + ","

	if where_clause != "":
		str_query = str_query + " WHERE "+ where_clause
		
	#str = "update Subject set branch='computer science' where subject_id = 3"
	print( " Now Update Query is ",str_query)

	cur.execute(str_query)

	rows = cur.fetchall()

	for row in rows:
		print(row)

	

def main():
	database = r"Education.db"
	print("Current Path : ",os.getcwd())
	conn = create_connection(database)
	with conn:
		print("1. Query task")

		col_name = ['Roll_Number','Name']
		#select_task(conn,'Student',col_name,"Name='Ram'")
		select_task(conn,'Student',col_name,"")

		#col_name = ['Branch','Subject_Name']
		delete_task(conn,'Subject',"Subject_ID=4")

		col_name = ['Name','Address','Id_Proof']
		data_send = ['Astha','Gorakhpur','PAN']
		update_task(conn,'Student',col_name,data_send,"Roll_Number=3")

		col_name = ['Name','Roll_Number','Address','Phone_Number','Id_Proof']
		#select_task(conn,'Student',col_name,"Name='Ram'")
		select_task(conn,'Student',col_name,"")


if __name__ == '__main__':
	main()
