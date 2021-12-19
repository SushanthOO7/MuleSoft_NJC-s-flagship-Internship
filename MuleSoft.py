import sqlite3

c=sqlite3.connect('MuleSoft.db')
cu=c.cursor()

command1="""CREATE TABLE IF NOT EXISTS Movies(Name VARCHAR,Actor CHAR,Actress CHAR,Year_of_Release INTEGER,Director CHAR)"""
cu.execute(command1)

cu.execute("INSERT INTO Movies Values('Fantastic Beasts: The Crimes of Grindelwald','Eddie Redmayne','Katherine Waterston',2018,'David Yates')")
cu.execute("INSERT INTO Movies Values('Escape Room 2','Logan Miller','Taylor Russell',2021,'Adam Robitel')")
cu.execute("INSERT INTO Movies Values('Spider-Man: No Way Home','Tom Holland','Zendaya',2021,'Jon Watts')")
cu.execute("INSERT INTO Movies Values('F9','Vin Diesel','Michelle Rodriguez',2021,'Justin Lin')")
cu.execute("INSERT INTO Movies Values('Dune','Timothee Chalamet','Zendaya',2021,'Denis Villeneuve')")
cu.execute("INSERT INTO Movies Values('Shang-Chi and The Legend of The Ten Rings','Simu Liu','Awkwafina',2021,'Destin Daniel Cretton')")

cu.execute("SELECT * FROM Movies")
data = cu.fetchall()
cu.execute("SELECT Name From Movies WHERE Actor ='Vin Diesel'")
actor = cu.fetchall()
cu.execute("SELECT Name From Movies WHERE Actress ='Zendaya'")
actress = cu.fetchall()


for i in data:
    print(i)
for i in actor:
    print(i)
for i in actress:
    print(i)
