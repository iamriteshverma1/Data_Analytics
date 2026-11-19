import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user = "root",
    password = "#exam3403@R",
    database = "analytics"
)

cur = con.cursor()

query = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"

values = (1, "Rahul", 21)

cur.execute(query, values)

con.commit()

print("Record inserted successfully")

cur.close()
con.close()