import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "use /on /off and /swap with ?devip=IP!"

@app.route("/on", methods=["GET","POST"])
def turn_on():
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        stdout = check_output(['./some.sh',typen,devip,'on']).decode('utf-8')
        return '''<h1>Turning On {}: {}</h1>'''.format(devip, stdout)
    if request.method == 'POST':
        devip = request.form.get('devip')
        typen = request.form.get('type','plug')
        stdout = check_output(['./some.sh',typen,devip,'on']).decode('utf-8')
        return '''<h1>Turning On {}: {}</h1>'''.format(devip, stdout)

@app.route("/off", methods=["GET","POST"])
def turn_off():
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        stdout = check_output(['./some.sh',typen,devip,'off']).decode('utf-8')
        return '''<h1>Turning Off {}: {}</h1>'''.format(devip, stdout)
    if request.method == 'POST':
        devip = request.form.get('devip')
        typen = request.form.get('type','plug')
        stdout = check_output(['./some.sh',typen,devip,'off']).decode('utf-8')
        return '''<h1>Turning Off {}: {}</h1>'''.format(devip, stdout)

@app.route("/swap", methods=["GET","POST"])
def turn_swap():
    if request.method == 'GET':
        devip = request.args.get('devip','192.168.1.245')
        typen = request.args.get('type','plug')
        #return '''<h1>Swapping On/Off: {}</h1>'''.format(devip)
        stdout = check_output(['./swap.sh',typen,devip]).decode('utf-8')
        return stdout
    if request.method == 'POST':
        devip = request.form.get('devip','192.168.1.245')
        typen = request.form.get('type','plug')
        stdout = check_output(['./swap.sh',typen,devip]).decode('utf-8')
        return stdout

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