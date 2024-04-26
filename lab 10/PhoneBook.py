import psycopg2, csv, sys



hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'zhangul_06'
port_id = 5432
conn, cur = None, None




def readdatafromcsv():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for item in reader:
            cur.execute('''INSERT INTO phonebook (
                        id,
                        first_name,
                        last_name, 
                        phone, 
                        region)
                        VALUES (%s, %s, %s, %s, %s)
                        ''', (item[0], item[1], item[2], item[3], item[4]))


def change():
    name = input()
    id = input()
    cur.execute(
        '''UPDATE phonebook SET first_name = %s WHERE id = %s''', (name, id)
    )


def from_console():
    id = input()
    first_name = input()
    last_name = input()
    phone = input()
    region = input()
    cur.execute(
        '''INSERT INTO phonebook (id, first_name, last_name, phone, region) 
        VALUES (%s, %s, %s, %s, %s)''', 
        (str(id), str(first_name), str(last_name), str(phone), str(region))
    )

def searchbyname():
    name = input()
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name = '{}'".format(name)
    )
    data = cur.fetchall()
    for item in data:
        print(item)
def searchbyphone():
    phone = input()
    cur.execute(
                "SELECT * FROM phonebook WHERE phone = '{}'".format(phone)
    )
    data = cur.fetchall()
    for item in data:
        print(item)


def deletebyname():
    name = input()
    cur.execute(
        "DELETE FROM phonebook WHERE first_name = '{}'".format(name)
    )

def deletebyphone():
    phone = input()
    cur.execute(
        "DELETE FROM phonebook WHERE phone = '{}'".format(phone)
    )
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()
    create_script = '''CREATE TABLE IF NOT EXISTS phonebook(
                id  varchar(3),
                first_name   varchar(30),
                last_name varchar(30),
                phone   varchar(30),
                region  varchar(30)
    )'''
    cur.execute(create_script)
   
   
    print('''1 - upload data from csv\n 2 - enter username from console\n 3 - update data\n 4 - search by name\n 5 - search by phone\n 6 - delete by name\n 7 - delete by phone\n 0 - exit''')
    num = int(input())
    if num == 1:
        readdatafromcsv()
    elif num == 2:
            from_console()
    elif num == 3:
            change()
    elif num == 4:
            searchbyname()
    elif num == 5:
            searchbyphone()
    elif num == 6:
            deletebyname()
    elif num == 7:
            deletebyphone()
    

                           

    conn.commit()


    cur.close()
    conn.close()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()