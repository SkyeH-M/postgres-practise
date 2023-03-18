import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artists" table
# cursor.execute('SELECT * FROM "Artist"') # prints all names and IDs

# Query 2 - select only the "name" column from "artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')  # prints all names

# Query 3 - select only "Queen" from "artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#  Query 5 - select only the albums with "ArtistId" #51 on the "album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - select all tracks from Soundgarden
# cursor.execute(
# 'SELECT * FROM "Track" WHERE "Composer" = %s', ["Soundgarden"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
