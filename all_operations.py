import datetime
import logging
import mysql.connector as sqlc

class BasicSqlOperation:
    """In this class I am doing basic database operation like createing a table, inserting value, deleting value
    updating value and selecting the value....
    I have created five different methods for doing five operations"""

    #logging is used here for sorting print statement
    logging.basicConfig(filename='allOperations.log',filemode='a',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    logging.info("Starting of all operations program")

    myDatabase =""
    def database_connection(self):
        """"Here I am creating the connection with databse and returning two objects mycursor and database to
        all the function for further use"""
        myDatabase = sqlc.connect(host="127.0.0.1", user="root", password="root", database="student_details")
        logging.debug("connection established")
        myCursor = myDatabase.cursor()
        return myCursor,myDatabase

    def create_table(self):
        """Here I am creating a table by taking user input"""
        try:
            Cursor,Database=self.database_connection()
            #creating the table into database
            tableName=input("Enter the table name: ")
            id=input("Enter the first column name: ")
            id_type=input("Data type: ")
            first_name=input("Enter your second column name: ")
            first_name_type=input("Data type: ")
            last_name=input("Enter the third column name: ")
            last_name_type=input("Data type: ")
            department=input("Enter the fourth column name: ")
            department_type=input("Data type: ")
            TableName = f'CREATE TABLE {tableName}({id} {id_type},{first_name} {first_name_type},{last_name} {last_name_type},{department} {department_type})'
            Cursor.execute(TableName)
        except Exception as ex:
            logging.error("Problem occured while creating the table..")
            logging.error(ex)
        finally:
            Database.commit()
            print("Student table is created in the database..")
            self.Database.close()

    def inserting_into_table(self):
        """Here I am inserting value into table by taking input from users"""

        try:
            Cursor, Database = self.database_connection()
            #inserting data into table
            t_name=input("Enter the table name where you want to insert the data: ")
            id=input("Enter id of the student: ")
            f_name=input("Enter the first_name of student: ")
            l_name=input("Enter the last name of student: ")
            depart=input("Enter the department name: ")
            query=f'insert into {t_name} values(%s,%s,%s,%s)'
            val=(id,f_name,l_name,depart)
            Cursor.execute(query,val)
        except Exception as ex:
            logging.error("Problem occured while inserting the value in the table..")
            logging.error(ex)
        finally:
            Database.commit()
            print(Cursor.rowcount,"row added to server")
            Database.close()

    def deleting_from_table(self):
        """Here I am deleting value from table by taking input from users"""

        try:
            # connecting to database
            Cursor, Database = self.database_connection()

            #deleting data from the table
            t_name = input("Enter the table name from where you want to delete the data: ")
            id=input("Enter the id of yhe student you want to delete: ")
            query=f'Delete from {t_name} where id={id}'
            Cursor.execute(query)
        except Exception as ex:
            logging.error("Problem occured while deleting the value")
            logging.error(ex)
        finally:
            Database.commit()
            print(Cursor.rowcount,"Row has deleted")
            Database.close()

    def update_into_table(self):
        """Here I am updating value into table by taking input from users"""

        try:
            # connecting to database
            Cursor,Database=self.database_connection()

            t_name=input("Enter the table name you want to update: ")
            id=input("Enter the id of the student you want to update: ")
            col=input("Enter the column name you want to update: ")
            val=input("Enter the updated value: ")
            query=f'Update {t_name} set {col}="{val}" where id={id}'
            Cursor.execute(query)
        except Exception as ex:
            logging.error("Problem occured while updating the table..")
            logging.error(ex)
        finally:
            Database.commit()
            print(Cursor.rowcount,"row updated")
            Database.close()

    def show_data_form_table(self):
        """Her I am displaying value from table by taking input from users"""
        try:
            # connecting to database
            Cursor,Database=self.database_connection()

            t_name=input("Enter the table name to show it's value: ")
            query=f'select * from {t_name}'
            Cursor.execute(query)
            data=Cursor.fetchall()
            for one_by_one in data:
                print(one_by_one)
        except Exception as ex:
            logging.error("Problem occured while updating the table..")
            logging.error(ex)
        finally:
            Database.commit()
            print(Cursor.rowcount,"row updated")
            Database.close()