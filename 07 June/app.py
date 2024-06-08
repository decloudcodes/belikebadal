"""
Badal Prasad Singh

Tech Stack API Documentation

Overview:
This Flask application serves as a simple API to provide information about the technology stack used

Usage:
The API exposes a single endpoint:

- GET /: Retrieves the technology stack used by the project

Response:
The response is in JSON format and includes an array of technologies used in the project.

Example response:
["Python", "Flask", "MySQL"]

Technologies Used:
- Python: The primary programming language used for developing the project.
- Flask: A lightweight WSGI web application framework used for building the API.
- MySQL: A relational database management system used for data storage in the project.

Running the Application:
To run the application, execute the Python script. Ensure you have Flask installed in your Python environment.

Additional Notes:
- This application runs in debug mode by default, which provides helpful debugging information in case of errors. It's recommended to disable debug mode in production environments.
- Make sure to configure MySQL connection settings appropriately for your environment.
"""


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def techstack():
    data = ["Python", "Flask", "MySQL"]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug = True)