import sqlite3
conn = sqlite3.connect("mydatabase__14_10_2019.db")
cursor = conn.cursor()
sql_command = " CREATE TABLE CUSTOMERS ( ID INTEGER PRIMARY KEY," \
              " FIRST_NAME VARCHAR(50) NOT NULL," \
              " LAST_NAME VARCHAR(50) NOT NULL, " \
              "PHONE VARCHAR(100)," \
              "ADDRESS VARCHAR(100)," \
              "EMAIL VARCHAR (100));"

cursor.execute(sql_command)

sql_command = "INSERT INTO customers VALUES (1, 'Ivan', 'Ivanov', '11111', 'Fontanskaya doroga, 1', ' 11111@gmail.com');"
cursor.execute(sql_command)
conn.commit()

customers = [(2, 'Petro', 'Petrov', '22222', 'Fontanskaya doroga, 2', ' 22222@gmail.com'),
             (3, 'Sergey', 'Sergeev', '33333', 'Fontanskaya doroga,3', ' 33333@gmail.com'),
             (4, 'Victor', 'Victorov', '44444', 'Fontanskaya doroga, 4', ' 4444@gmail.com'),
             (5, 'Grigorii', 'Grigorev', '55555', 'Fontanskaya doroga, 5', ' 55555@gmail.com')]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", customers)
conn.commit()
cursor.close()
conn.close()


class MyDataBase:

    my_db = " "
    sql_command = " "

    def __init__(self, my_db):
        self.my_db = my_db

    def sqlite3_read_db(self, table):
        self.table = table
        conn = sqlite3.connect(self.my_db)
        cursor = conn.cursor()
        self.sql_command = ' SELECT * FROM '+ str(self.table)+''
        cursor.execute(self.sql_command)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def sqlite3_add_new_object(self, table, new_object=()):
        self.table = table
        self.new_object = new_object
        conn = sqlite3.connect(self.my_db)
        cursor = conn.cursor()
        self.sql_command = " INSERT INTO "+ str(self.table)+" VALUES "+ str(self.new_object)+""
        cursor.execute(self.sql_command)
        conn.commit()
        cursor.close()
        conn.close()
        return print('Object {} was add'.format(self.new_object))

    def sqlite3_get_object_from_ID(self,table, id):
        self.table = table
        self.id = id
        conn = sqlite3.connect(self.my_db)
        cursor = conn.cursor()
        self.sql_command = 'SELECT * FROM '+str(self.table)+' WHERE id=?'
        cursor.execute(self.sql_command, [(self.id)])
        object = cursor.fetchall()
        cursor.close()
        conn.close()
        return object

    def sqlite3_get_sorted_list(self, table, param):
        self.table = table
        self.param = param
        conn = sqlite3.connect(self.my_db)
        cursor = conn.cursor()
        self.sql_command = 'SELECT * FROM '+str(self.table)+' ORDER BY  '+str(self.param)
        cursor.execute(self.sql_command)
        sort_list = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return sort_list


mydatabase1 = MyDataBase("mydatabase__14_10_2019.db")
print(mydatabase1.sqlite3_read_db('customers'))
mydatabase1.sqlite3_add_new_object('customers', new_object=(6, 'Nikolay', 'Nikolaev', '66666', 'Fontanskaya doroga, 6',' 66666@gmail.com'))
mydatabase1.sqlite3_add_new_object('customers', new_object=(7, 'Vova', 'Vladimir', '77777', 'Fontanskaya doroga, 7',' 77777@gmail.com'))
print(mydatabase1.sqlite3_get_object_from_ID('customers', 4))
print(mydatabase1.sqlite3_get_sorted_list('customers', 'phone'))
print(mydatabase1.sqlite3_get_sorted_list('customers', 'address'))
print(mydatabase1.sqlite3_get_sorted_list('customers', 'id'))

