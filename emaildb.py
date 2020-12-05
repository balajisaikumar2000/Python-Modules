#python type--------------sqlitetype
#None--------------------NULL
#int---------------------INTEGER
#float--------------------REAL
#str----------------------TEXT
#bytes---------------------BLOB

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()             #cursor is important because it has the methods for executing the sql statements like execute(),executemany() etc..

cur.execute('DROP TABLE IF EXISTS Counts')     #execute is cursor() 's method

cur.execute('''
CREATE TABLE Counts (email text, count integer)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#to retrieve data after executing a SELECT statement ,you can either treat the cursor as an iterator,
#call the cursor's fetchone() method to retrieve a single matching row
#the below statement looks like this:-
#for row in in cur.execute('SELECT count FROM Counts WHERE email = ?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()     #if we do not call it ,it won't save the changes to databases

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

conn.close()     #closes databases
