from flask import Flask , request , jsonify , make_response , render_template
from flask_cors import CORS
import requests
import json
import flask
import threading
import updateTLB , getRunning , controlProcess

global pid
pid = -1
global tid 
tid = -1
app = Flask(__name__)
CORS(app)

@app.route('/startprocess', methods=['POST', 'GET'])
def startProcess():
    global pid
    pid = str(request.get_json(silent=True, force=True))

    print(pid)
    startThread = threading.Thread(target=controlProcess.start, args = (pid,)) 
    startThread.start()
    
    return 'Success', 200

@app.route('/endprocess', methods=['POST'])
def endProcess():

    endThread = threading.Thread(target=controlProcess.stop, args = ()) 
    endThread.start()
    pid = -1

    return 'Success', 200


@app.route('/getrunning', methods=['POST'])
def getRun():

    global pid
    data = getRunning.main(pid)
    print(data)
    return jsonify({"data": data})


@app.route('/startthread', methods=['POST'])
def startThread():

    tid = str(request.get_json(silent = True, force = True))
    startThread = threading.Thread(target=updateTLB.start, args = (tid, )) 
    startThread.start()
    
    return "Success", 200


@app.route('/endthread', methods=['POST'])
def endThread():

    global tid

    print("STOP Called")

    updateTLB.stop()
    tid = -1

    return "Success", 200

@app.route('/')
def main():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(use_reloader = True, port = 4000, debug=True)