from config.dbConfig import get_db_connection

def login(username, password):
    conn = get_db_connection()
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"  # SQL Injection Vulnerability
    user = conn.execute(sql).fetchone()
    conn.close()
    return user

def search(query):
    conn = get_db_connection()
    sql = f"SELECT * FROM users WHERE username LIKE '%{query}%'"
    rows = conn.execute(sql).fetchall()
    conn.close()
    results = [dict(row) for row in rows]  # Convert each row to a dictionary
    print(f"Results from DB: {results}")  # Debugging output
    return results


def get_profile(user_id):
    conn = get_db_connection()
    sql = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection Vulnerability
    user = conn.execute(sql).fetchone()
    conn.close()
    return user