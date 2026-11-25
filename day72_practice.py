import sqlite3

# 1. Connect to the database (creates 'test.db' if it doesn't exist)
conn = sqlite3.connect("test.db")

# 2. Create a table
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
""")

# 3. Insert a sample record and save (commit) changes
conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# 4. Verify by fetching the data
cursor = conn.execute("SELECT * FROM users")
print(cursor.fetchall())

# 5. Close the connection
conn.close()
