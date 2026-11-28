import sqlite3

# 1. Connect to the database (note the '=' sign)
conn = sqlite3.connect("test.db")

# 2. Execute the UPDATE statement using '?' placeholders to prevent SQL injection
conn.execute("UPDATE users SET email = ? WHERE id = ?", ("new@example.com", 1))

# 3. Save (commit) the changes and close the connection
conn.commit()
conn.close()
