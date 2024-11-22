from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the landing page
    return send_file('index.html')

@app.route('/access.log')
def serve_log_file():
    # Serve the access.log file as a download
    return send_file('access.log', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

