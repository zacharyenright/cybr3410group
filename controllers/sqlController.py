from config.dbConfig import get_db_connection

def login(username, password):
    conn = get_db_connection()
    sql = "SELECT * FROM users WHERE username = ? AND password = ?"  # Uses placeholders
    user = conn.execute(sql, (username, password)).fetchone()  # Parameters are passed as a tuple
    conn.close()
    return user

def search(query):
    conn = get_db_connection()
    sql = "SELECT * FROM users WHERE username LIKE ?"  # Uses placeholder
    rows = conn.execute(sql, (f"%{query}%",)).fetchall()  # Pass parameter as tuple
    conn.close()
    results = [dict(row) for row in rows]  # Convert each row to a dictionary
    print(f"Results from DB: {results}")  # Debugging output
    return results



def get_profile(user_id):
    conn = get_db_connection()
    sql = "SELECT * FROM users WHERE id = ?"  # Use placeholder to prevent SQL injection
    user = conn.execute(sql, (user_id,)).fetchone()  # Pass parameter as tuple
    # sql = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection Vulnerability
    # user = conn.execute(sql).fetchone()
    conn.close()
    return user
    # The get_profile function now uses a parameterized query with a
    # placeholder (?). This prevents SQL injection by ensuring that user
    # input is treated as data, not executable code.
    # All SQL queries now consistently use placeholders, which improves
    # code readability and security.