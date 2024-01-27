import socket
import subprocess
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def login():
   global num
   if request.method == 'POST':
      process = subprocess.Popen(['python3', 'stress_cpu.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      return "", 200
   else:
      return socket.gethostname(), 200

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001)
