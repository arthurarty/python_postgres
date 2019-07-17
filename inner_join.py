from database.db_connection import DBCONNECTION

db = DBCONNECTION()
cur = db.cur
cur.execute('''
        SELECT
        EMP_ID, NAME, DEPT FROM COMPANY
        INNER JOIN DEPARTMENT
        ON COMPANY.ID = DEPARTMENT.EMP_ID;''')
print(cur.fetchall())

cur.execute('''
        SELECT
        ADDRESS FROM COMPANY
        INNER JOIN DEPARTMENT
        ON COMPANY.ID = DEPARTMENT.EMP_ID WHERE DEPT='Engineering';''')
print(cur.fetchall())
