import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully");
conn.execute('''CREATE TABLE STUDENT
 (ID INT PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 AGE INT NOT NULL);''')
print ("Table created successfully");
conn.execute("INSERT INTO STUDENT (ID,NAME,AGE) \
 VALUES (1, 'Ram', 20)");
conn.execute("INSERT INTO STUDENT (ID,NAME,AGE) \
 VALUES (2, 'Jon', 19)");
conn.execute("INSERT INTO STUDENT (ID,NAME,AGE) \
 VALUES (3, 'Maya', 18)");
conn.commit()
print ("Records created successfully");
cursor = conn.execute("SELECT id, name, age from STUDENT")
for row in cursor:
 print ("ID = ", row[0])
 print ("NAME = ", row[1])
 print ("AGE = ", row[2],"\n")
print ("Operation done successfully");
conn.execute("UPDATE STUDENT set AGE = 25 where ID = 1")
cursor = conn.execute("SELECT id, name, age from STUDENT")
for row in cursor:
 print ("ID = ", row[0])
 print ("NAME = ", row[1])
 print ("AGE = ", row[2],"\n")
print ("Updated table successfully");
conn.commit()
conn.close()
