import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Sam', 'Loved to cuddle, very quiet')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Poppy', 'Massive diva, would only eat junk food')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Prince', 'Only used us as a rest stop. Super chill')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Wendy', 'Loved to cuddle, only had her for a week')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Pippin', 'Very food motivated. Took about 3 weeks to figure out how to meow')
            )

connection.commit()
connection.close()