import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()
    #UPDATE
    cur.execute("UPDATE users SET score = score+500 WHERE old > 20")
    #DELETE
    # cur.execute("DELETE FROM users WHERE rowid IN(2,5)")