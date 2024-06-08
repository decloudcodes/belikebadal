"""
Badal Prasad Singh

Flask MySQL Database Connection Documentation

Overview:
This Flask application establishes a connection to a MySQL database using the Flask-MySQLDB extension. It loads database configuration from environment variables using the `dotenv` library.

Usage:
This application sets up a Flask app and configures it to connect to a MySQL database. It uses environment variables to store database connection details securely.

Database Configuration:
The following environment variables are used for database configuration:
- MYSQL_HOST: The hostname or IP address of the MySQL server.
- MYSQL_USER: The username used to connect to the MySQL server.
- MYSQL_PASSWORD: The password used to authenticate the MySQL user.
- MYSQL_DB: The name of the MySQL database to connect to.

MySQL Connection:
The MySQL connection is established using the Flask-MySQLDB extension. It creates a cursor to execute SQL queries.

Additional Notes:
- Make sure to set up the appropriate environment variables with the database connection details.
- Ensure that the required Python libraries (`flask`, `flask_mysqldb`, `dotenv`) are installed in your Python environment.
- Proper error handling should be implemented for database connection failures and SQL query execution errors.
"""

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)
cursor = mysql.connection.cursor()
mysql.connection.commit()
cursor.close()