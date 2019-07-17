from database.db_connection import DBCONNECTION

db = DBCONNECTION()
cur = db.cur
cur.execute('SELECT * FROM COMPANY')
rows = cur.fetchall()
for row in rows:
    print(f'Id is {row[0]}')
    print(f'Name is {row[1]}')
    print(f'Age is {row[2]}')
    print(f'Address is {row[3]}')
    print(f'Salary is {row[4]}')
    print()
