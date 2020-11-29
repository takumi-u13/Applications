import sqlite3
class DAO(object):
    def __init__(self):
        self.dbname = 'database.db'
        self.con = sqlite3.connect(self.dbname)
        self.cursor = self.con.cursor()
        try:
            self.con.execute("PRAGMA foreign_keys = 1")
            acc_table = """
            CREATE TABLE acc_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                acc_date DATE NOT NULL,
                item_code INTEGER NOT NULL,
                amount INTEGER,
                FOREIGN KEY (item_code) REFERENCES item(item_code)
            )
            """
            item_table = """
            CREATE TABLE item(
                item_code INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL UNIQUE
            )
            """
            self.cursor.execute(item_table)
            self.cursor.execute(acc_table)
            self.cursor.execute('insert into item(item_name) values("食費");')
            self.cursor.execute('insert into item(item_name) values("光熱費");')
            self.cursor.execute('insert into item(item_name) values("住宅費");')
            self.con.commit()
            self.con.close()
        except:
            self.con.close()
    
    def insert(self,date,item_name,amount):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            
            item_code = self.get_item_code(item_name)
            
            insert_sql = 'insert into acc_data(acc_date,item_code,amount) values ("{}",{},{});'.format(
                date, item_code, amount)
            cursor.execute(insert_sql)
            con.commit()
            con.close()
            print('Registered')
        except:
            print('Registration failed')
            con.close()
    
    def get_item_list(self):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            
            item_list =[]
            for i in cursor.execute('select item_name from item'):
                item_list.append(i)
            return item_list
        except:
            con.close()
    
    def get_item_code(self, item_name):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            item_code = cursor.execute("""
                SELECT item_code FROM item WHERE item_name = '{}'
                """.format(item_name))
            item_code = item_code.fetchone()[0] 
            return item_code
        except:
            con.close()
    
    def get_acc(self):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            sql = """
            SELECT acc_date,item_name,amount
            FROM acc_data as a,item as i
            WHERE a.item_code = i.item_code
            ORDER BY acc_date
            """
            
            cursor.execute(sql)
            list_data = cursor.fetchall()
            con.close()
            return list_data
            
        except:
            con.close()

    def select_acc_data(self,start_date,end_date):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            sql = """
            SELECT acc_date,item_name,amount
            FROM acc_data as a,item as i
            WHERE a.item_code = i.item_code
            AND acc_date BETWEEN '{}' AND '{}' 
            ORDER BY acc_date
            """.format(start_date, end_date)
            
            cursor.execute(sql)
            list_data = cursor.fetchall()
            con.close()
            
            return list_data
        except:
            con.close()
