from flask import Blueprint, render_template, request
from controllers.sqlController import login,search,get_profile

sql_routes = Blueprint('sql_routes', __name__)
@sql_routes.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login(username, password)
        if user:
            return f"Welcome, {user[1]}! Password: {user[2]}, and Profile: {user[3]}"  # Access by index
        else:
            return "Login failed."
    return render_template('login.html')

@sql_routes.route('/search', methods=['GET', 'POST'])
def search_route():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search(query)
        print(f"Search query: {query}")  # Debugging output
        print(f"Search results: {results}")  # Debugging output
    return render_template('search.html', results=results)

@sql_routes.route('/profile/<int:user_id>', methods=['GET'])
def profile_route(user_id):
    user = get_profile(user_id)  #  This function retrieves the user's profile
    if user:
        return render_template('profile.html', user=user)
    else:
        return "User not found.", 404
