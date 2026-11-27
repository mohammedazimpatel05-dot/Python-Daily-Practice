import sqlite3; conn = sqlite3.connect("test.db"); print(conn.execute("SELECT * FROM your_table_name").fetchall())
