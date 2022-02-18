1.First I created a class named as "BasicSqlOperation"

2.I have used logging to elimnate extra print statement and storing those print statement in a seperated file with proper type of error statement, There are five 
  statements in a log and I used most of them as requirment of the project in aseperated .txt file named as "allOperations" 

3.Inside that class I have created six methods 
	
	3.1 database_connection(self):This is the first method inside the class. This method is to estlablished the connection with database.

	3.2 create_table(self):This is the second method inside the class.In this method first I have called the first method for making the connection then i have 
            taken user input for table name, table column name etc used those data in sql query to create a table by keeping the whole code in try except block for 
	    handling the exception

	3.3 inserting_into_table(self): This is the third table for inserting data into table and it have the same equipments as the create_table method have.
	
	3.4 deleting_from_table(self):This is same as inserting data into the table the slit difference is that we are deleting the data based on the id of the row
	   given by the user.

	3.5 update_into_table(self):Here I just updating the value where needed

	3.6 show_data_form_table(self):In this I am printing all the data present inside the table

4.I have taken an starting_point.py file to put the main method of the program, In main() I took an while loop and inside the loop a if else block like switch case in 
"C" program, by that switch case I have taken user input to make use of specific operation. 


	    