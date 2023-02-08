import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("""SELECT sex, sum(score) as sum
    FROM users
    WHERE score > 1500
    GROUP BY sex
    ORDER BY sum DESC
    LIMIT 5""")

    for i in cur:
        if i[0] == 1:
            print(f"Мужчины набрали {i[1]} баллов")
        if i[0] == 2:
            print(f"Женщины набрали {i[1]} баллов")