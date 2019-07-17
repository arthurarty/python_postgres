import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DBCONNECTION():
    """Class to create db connection"""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
                )
        except:
            print("Database connection failed.")
        self.cur = self.conn.cursor()

    def commit_session(self):
        """Commit session"""
        self.conn.commit()


class Table(DBCONNECTION):
    """Class to handle creating tables"""

    def __init__(self, table_name, sql_query):
        DBCONNECTION.__init__(self)
        self.table_name = table_name
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name}
        ({sql_query});''')
        self.commit_session()

    def insert_record(self, columns, values):
        self.cur.execute(f"""
        INSERT INTO {self.table_name} ({columns})
        VALUES ({values})
        """)
        self.commit_session()
