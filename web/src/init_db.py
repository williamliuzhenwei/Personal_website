# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
# cursor.execute("drop table if exists Users;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      comment     TEXT NOT NULL,
      avatar   TEXT,
      school      TEXT,
      degree      TEXT,
      major       TEXT,
      date        TEXT,
      title       TEXT,
      description TEXT,
      link        TEXT,
      Image_src   TEXT,
      team        TEXT,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

# Insert Records
query = "insert into Users (first_name,last_name,email,comment,avatar,school,degree,major,date,title,description,link,Image_src,team,created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
values = [
  ('Zhenwei','Liu','zhl012@ucsd.edu','Good Job!!','https://images.unsplash.com/photo-1572251323447-f979e230f29c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3456&q=80',
  'University Of California, San Diego','Bachelor','Electrical Engineer','2021','Magic Mirror','A Smart mirror that can interact with you in yoru bathroom',
  'http://165.232.145.224.','https://drive.google.com/file/d/1Pe1oKFvq6kuSRiW0w-DthSkp8uknQzOL/view?usp=sharing','143.198.98.101 , 143.110.156.0', '2021-05-17 14:50:00')
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Users;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
