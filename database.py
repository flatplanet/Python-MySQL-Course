import mysql.connector

#SET MYSQL CONNECTION
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "password123",
	database = "testdb",
	)

#CREATE CURSOR INSTANCE
my_cursor = mydb.cursor()

#CREATE DATABASE
my_cursor.execute("CREATE DATABASE testdb")

#SHOW DATABASE
my_cursor.execute("SHOW DATABASES")

#CREATE TABLE
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")

#INSERT ONE RECORD
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)
my_cursor.execute(sqlStuff, record1)
mydb.commit()

#INSERT MULTIPLE RECORDS
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Tim", "tim@tim.com", 32),
	("Mary", "Mary@mary.com", 21),
	("Steve", "steve@steveEmail.com", 57),
	("Tina", "tina@somethingellse.com", 29),]
my_cursor.executemany(sqlStuff, records)
mydb.commit()

#PULL DATA FROM THE TABLE
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
	print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

#WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE name =  'John'")
result = my_cursor.fetchall()
for row in result:
	print(row)

#WHERE and LIKE WILDCARDS
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%'")
result = my_cursor.fetchall()
for row in result:
	print(row)

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29 AND user_id = 5")
result = my_cursor.fetchall()
for row in result:
	print(row)

#UPDATING RECORDS
my_sql = "UPDATE users SET name = 'Johnny' WHERE user_id = 6"
my_cursor.execute(my_sql)
mydb.commit()

#LIMIT RESULTS
my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = my_cursor.fetchall()
for row in result:
	print(row)

#ORDERING RESULTS
my_cursor.execute("SELECT * FROM users ORDER BY age DESC")
result = my_cursor.fetchall()
for row in result:
	print(row)

#DELETE RECORDS
my_sql = "DELETE FROM users WHERE name  = 'John'"
my_cursor.execute(my_sql)
mydb.commit()

# DELETE DROP TABLE
my_sql = "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)
