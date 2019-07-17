from database.db_connection import DBCONNECTION, Table

# create members table
members_table = Table('company', '''
      ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL''')

members_table.insert_record(
      'ID,NAME,AGE,ADDRESS,SALARY',
      "4, 'Mark', 25, 'Rich-Mond ', 65000.00")
members_table.insert_record(
      'ID,NAME,AGE,ADDRESS,SALARY',
      "3, 'Teddy', 23, 'Norway', 20000.00")
