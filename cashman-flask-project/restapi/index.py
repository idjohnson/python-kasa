import subprocess
import os
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "use /on /off and /swap with ?devip=IP&apikey=APIKEY!"

@app.route("/on", methods=["GET","POST"])
def turn_on():
    deploykey = os.getenv('API_KEY')
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        apikey = request.args.get('apikey','apikey')
        if apikey == deploykey:
            stdout = check_output(['./some.sh',typen,devip,'on']).decode('utf-8')
            return '''<h1>Turning On {}: {}</h1>'''.format(devip, stdout)
        else:
            return '''<h1>NOT Turning On {}: Invalid API Key {}.</h1>'''.format(devip, apikey)
    if request.method == 'POST':
        devip = request.form.get('devip')
        typen = request.form.get('type','plug')
        apikey = request.form.get('apikey','apikey')
        if apikey == deploykey:
            stdout = check_output(['./some.sh',typen,devip,'on']).decode('utf-8')
            return '''<h1>Turning On {}: {}</h1>'''.format(devip, stdout)
        else:
            return '''<h1>NOT Turning On {}: Invalid API Key {}.</h1>'''.format(devip, apikey)

@app.route("/off", methods=["GET","POST"])
def turn_off():
    deploykey = os.getenv('API_KEY')
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        apikey = request.args.get('apikey','apikey')
        if apikey == deploykey:
            stdout = check_output(['./some.sh',typen,devip,'off']).decode('utf-8')
            return '''<h1>Turning Off {}: {}</h1>'''.format(devip, stdout)
        else:
            return '''<h1>NOT Turning Off {}: Invalid API Key {}.</h1>'''.format(devip, apikey)
    if request.method == 'POST':
        devip = request.form.get('devip')
        typen = request.form.get('type','plug')
        apikey = request.form.get('apikey','apikey')
        if apikey == deploykey:
            stdout = check_output(['./some.sh',typen,devip,'off']).decode('utf-8')
            return '''<h1>Turning Off {}: {}</h1>'''.format(devip, stdout)
        else:
            return '''<h1>NOT Turning Off {}: Invalid API KEY {}.</h1>'''.format(devip, apikey)

@app.route("/swap", methods=["GET","POST"])
def turn_swap():
    deploykey = os.getenv('API_KEY')
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        apikey = request.args.get('apikey','apikey')
        #return '''<h1>Swapping On/Off: {}</h1>'''.format(devip)
        if apikey == deploykey:
            stdout = check_output(['./swap.sh',typen,devip]).decode('utf-8')
            return stdout
        else:
            return "INVALID API KEY. WILL NOT SWAP"
    if request.method == 'POST':
        devip = request.form.get('devip','192.168.1.245')
        typen = request.form.get('type','plug')
        apikey = request.form.get('apikey','apikey')
        
        if apikey == deploykey:
            stdout = check_output(['./swap.sh',typen,devip]).decode('utf-8')
            return stdout
        else:
            return "INVALID API KEY. WILL NOT SWAP"

@app.route("/testshell1")
def testshell():
    session = Popen(['./some.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

    
@app.route("/testshell2")
def testshell2():
    stdout = check_output(['./some.sh','plug','192.168.1.245','on']).decode('utf-8')
    return stdout

@app.route("/testshell3")
def testshell3():
    stdout = check_output(['/usr/local/bin/kasa','--host','192.168.1.245','off']).decode('utf-8')
    return stdout

@app.route("/testshell4")
def testshell4():
    stdout = check_output(['/usr/local/bin/kasa','--host','192.168.1.245','on']).decode('utf-8')
    return stdout

@app.route('/health')
def health():
    return