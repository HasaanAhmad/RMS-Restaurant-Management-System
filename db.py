import pyodbc
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
# print(f'MS-Access Drivers : {msa_drivers}')

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Admin\Desktop\Restaurant Management\Restaurant.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected to the data base")

except pyodbc.Error as e:
    print("error in connection", e)


cursor = conn.cursor()

sql = 'select * from Table1'

cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

