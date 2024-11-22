from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful!", "flag": "ctf_{SQL_Injection_Wins}"})
    else:
        return jsonify({"message": "Invalid credentials."}), 401


@app.route('/')
def index():
    return '''
    <h1>Login</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username">
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password">
        <br>
        <button type="submit">Login</button>
    </form>
    '''

