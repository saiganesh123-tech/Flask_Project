from flask import Flask, render_template, request, jsonify
import mysql.connector
from config import db_config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Database Connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    try:
        data = request.json
        name = data['name']
        email = data['email']
        gender = data['gender']
        country = data['country']
        programming = ", ".join(data['programming'])  # Convert list to string

        if not name or not email or not gender or not country or not programming:
            return jsonify({"status": "error", "message": "All fields are required!"}), 400

        # Insert into MySQL
        query = "INSERT INTO users (name, email, gender, country, programming) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, gender, country, programming)
        cursor.execute(query, values)
        db.commit()

        return jsonify({"status": "success", "message": "Successfully registered!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
