from flask import Flask
from routes.sqlRoutes import sql_routes

app = Flask(__name__)
app.register_blueprint(sql_routes)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)