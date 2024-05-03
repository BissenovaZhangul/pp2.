import psycopg2, csv, sys
from config import host, user, password, db_name

connection = psycopg2.connect
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit=True
    


    cursor=connection.cursor()

        #creating table
    #with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE phonebook(
    #            first_name varchar(50) NOT NULL,
    #            id SERIAL PRIMARY KEY,
    #            study_year INT,
    #            phone_num varchar(11));""")
    #     print("INFO Table created successfully")

    with connection.cursor() as cursor:
        cursor.execute(
            """ALTER TABLE phonebook ALTER COLUMN phone_num TYPE varchar(20);"""
        )
        print("INFO: Column type altered successfully")


        #inserting    
    #with connection.cursor() as cursor:
    #    data=(input("First Name:"),input("ID:"),input("Study Year:"),input("Phone number:"))
    #    cursor.execute(
    #         """INSERT INTO phonebook(first_name,id,study_year,phone_num) VALUES
    #         (%s,%s,%s,%s);""",data
    #    )
    #    print("[INFO] Data was successfully inserted")

   #inserting csv
   # with open('phoneBook.csv', 'r') as file:
    #    rows = csv.reader(file)  
    #    for data in rows:
    #        with connection.cursor() as cursor:
    #            cursor.execute(
    #                """INSERT INTO phonebook(first_name, id, study_year, phone_num) VALUES(%s,%s, %s, %s);""",
    #                data
    #            )


                #deleting
    #name=input("Name: ")
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        """DELETE FROM phonebook WHERE first_name=%s;""",(name,)
    #    )
    #    print(f"Deleted")
    #check data

    #change
    #with connection.cursor() as cursor:
    #    cursor.execute("""UPDATE phonebook
    #        SET first_name = 'Arman'
    #        WHERE id = '123455'
    #        """)
    #print("[INFO] Data was successfully changed")


    #Querying






except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection==True: 
        connection.close()
        print("[INFO] PostgreSQL connection closed")