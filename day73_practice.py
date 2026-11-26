import sqlite3

# 1. Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("test.db")

# 2. Insert data using parameterized placeholders (?) to prevent SQL injection
conn.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)", 
    ("Alice", 30)
)

# 3. Save (commit) the changes and close the connection
conn.commit()
conn.close()
