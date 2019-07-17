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

    def create_table(self):
        self.cur.execute('''CREATE TABLE MEMBERS
              (ID INT PRIMARY KEY     NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL,
              ADDRESS        CHAR(50),
              SALARY         REAL);''')
        self.close_connection()

    def close_connection(self):
        """Close connection to the database"""
        self.conn.commit()
        self.conn.close()
