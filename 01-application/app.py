from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def server_inf():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR')

    return render_template('server_inf.html', hostname=hostname, ip_address=ip_address, author=author)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)