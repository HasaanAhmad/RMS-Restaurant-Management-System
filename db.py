import pyodbc
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
# print(f'MS-Access Drivers : {msa_drivers}')

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cui\Downloads\RMS-Restaurant-Management-System-master\RMS-Restaurant-Management-System-master\Restaurant.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected to the data base")

except pyodbc.Error as e:
    print("error in connection", e)


cursor = conn.cursor()
sql = "INSERT INTO bill_data (reference_id, total_bill) VALUES (?, ?)"
val = ("bill545", "1200")
cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount, "record inserted.")



