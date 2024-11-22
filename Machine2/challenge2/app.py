from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin"
FLAG = "ctf_{Login_Brute_Force_Success}"

@app.route("/")
def login_page():
    return """
    <h1>Login Page</h1>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == USERNAME and password == PASSWORD:
        return f"<h1>Welcome, {USERNAME}!</h1><p>Flag: {FLAG}</p>"
    else:
        return "<h1>Login Failed</h1><p>Invalid credentials.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

