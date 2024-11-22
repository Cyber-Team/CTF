from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)

app.secret_key = 'supersecretkey'  # This is used for session management

# Updated Flag in the ctf_{} format with an interesting obfuscated string
FLAG = "ctf_{y0u_4r3_g00d_@_ctf_3xpl0r3r}"

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "password"

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check credentials
        if username == USERNAME and password == PASSWORD:
            session["username"] = username  # Store username in session
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials. Please try again.", 403
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    
    # Create a response object
    response = make_response(render_template("dashboard.html"))
    
    # Add the flag in the response header (you can also add it in the response body)
    response.headers["X-Flag"] = FLAG  # Flag hidden in the response header
    
    # Alternatively, you can return the flag in the body as JSON, but headers are more secure
    # response.data = {"flag": FLAG}  # Optionally uncomment this line to include flag in response body
    
    return response

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

