from database.db_connection import DBCONNECTION, Table

# create department table
department_table = Table('department', '''
    ID INT PRIMARY KEY      NOT NULL,
    DEPT           CHAR(50) NOT NULL,
    EMP_ID         INT      references COMPANY(ID)''')

department_table.insert_record(
      'ID, DEPT, EMP_ID',
      "1, 'IT Billing', 2")
department_table.insert_record(
      'ID, DEPT, EMP_ID',
      "2, 'Engineering', 3")
