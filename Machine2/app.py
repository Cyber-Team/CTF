from flask import Flask, request, render_template

app = Flask(__name__)

# Flags for each vulnerability
SQLI_FLAG = "ctf_{sneaky_sql_injection}"
XSS_FLAG = "ctf_{cross_site_scripting_success}"
CMDI_FLAG = "ctf_{command_injection_achieved}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comment", methods=["GET", "POST"])
def comment():
    comment = None
    flag = None
    if request.method == "POST":
        comment = request.form.get("comment", "")
        
        # Check if the comment contains an XSS payload, for demonstration purposes
        if "<script>" in comment:
            flag = XSS_FLAG
    
    return render_template("comment.html", comment=comment, flag=flag)

@app.route("/login", methods=["GET", "POST"])
def login():
    username = None
    flag = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        
        # Check for SQL Injection in username field
        if "'" in username or "--" in username:
            flag = SQLI_FLAG
    
    return render_template("login.html", username=username, flag=flag)

@app.route("/command", methods=["GET", "POST"])
def command():
    output = None
    flag = None
    if request.method == "POST":
        cmd = request.form.get("cmd", "")
        
        # Simulate command injection vulnerability
        if ";" in cmd or "&&" in cmd:
            flag = CMDI_FLAG
            output = "Simulated command output here"
    
    return render_template("command.html", cmd=cmd, output=output, flag=flag)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

