from flask import Flask, request, make_response

app = Flask(__name__)

FLAG = "ctf_{Cookies_Are_Sweet}"

@app.route("/")
def home():
    resp = make_response("""
    <h1>Welcome to Cookie Monster Challenge</h1>
    <p>Check your browser cookies for clues.</p>
    """)
    resp.set_cookie("hint", "Try harder!")
    return resp

@app.route("/secret")
def secret():
    cookie = request.cookies.get("admin")
    if cookie == "true":
        return f"<h1>Welcome, Admin!</h1><p>Flag: {FLAG}</p>"
    else:
        return "<h1>Access Denied!</h1><p>You are not authorized to view this page.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

