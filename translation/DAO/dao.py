import sqlite3

class DAO(object):
    def __init__(self):
        self.dbname = 'database.db'
        self.con = sqlite3.connect(self.dbname)
        self.cursor = self.con.cursor()
        try:
            translation_table = """
            CREATE TABLE translation_table(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jp_word TEXT NOT NULL,
                en_word TEXT NOT NULL
            )
            """
            self.cursor.execute(translation_table)
            self.con.commit()
            self.con.close()
        except:
            self.con.close()

    def save_word(self, en_word, translated_word):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()

            insert_sql = 'insert into translation_table(jp_word,en_word) values ("{}","{}");'.format(
                translated_word, en_word)
            cursor.execute(insert_sql)
            con.commit()
            con.close()
            print('Registered')
        except:
            print('Registration failed')
            con.close()
    
    def get_data(self):
        con = sqlite3.connect(self.dbname)
        try:
            cursor = con.cursor()
            sql = """
            SELECT en_word,jp_word FROM translation_table 
            """

            cursor.execute(sql)
            list_data = cursor.fetchall()
            con.close()
            return list_data

        except:
            con.close()

