from flask import Flask, render_template, request, redirect
from time import sleep
from threading import *



command_txt = "ingenting"
set_change_timer = False

app = Flask(__name__)


class change_api(Thread):
    def run(e):
        global set_change_timer
        global command_txt
        while True:
            sleep(0.3)
            if set_change_timer:
                sleep(5)
                command_txt = "ingenting"
                set_change_timer = False

change_api_var = change_api()
change_api_var.start()



    
    


@app.route("/api")
def api():
    print(f"{request.remote_addr} opened api website")
    return render_template("api.html", command = command_txt)
 
@app.route("/mat_alarm")
def mat_alarm():
    print(f"{request.remote_addr} opened website")
    return render_template("index.html")


@app.route('/middag')
def mat():
    global command_txt
    global set_change_timer
    set_change_timer = True
    command_txt = "Mat_98174"
    print(f"Click from: {request.remote_addr}")
    return "nothing"

@app.route('/legg_knapp')
def legg_knapp():
    global command_txt
    global set_change_timer
    set_change_timer = True
    command_txt = "Leggetid_98174"
    print(f"Click from: {request.remote_addr}")
    return "nothing"

@app.route('/Møte_knapp')
def møte_knapp():
    global command_txt
    global set_change_timer
    set_change_timer = True
    command_txt = "Møte_98174"
    print(f"Click from: {request.remote_addr}")
    return "nothing"

@app.route('/skjerm_knapp')
def skjerm_knapp():
    global command_txt
    global set_change_timer
    set_change_timer = True
    command_txt = "Skjermpause_98174"
    print(f"Click from: {request.remote_addr}")
    return "nothing"


@app.route('/Sendt/', methods = ['POST', 'GET'])
def data():
    global command_txt
    global set_change_timer
    if request.method == 'GET':
        return redirect("/mat_alarm")
    if request.method == 'POST':
        print(f"{request.remote_addr} sende melding")
        text = request.form['Melding']
        print(text)
        command_txt = text
        set_change_timer = True
        return render_template("Sendt.html", melding = text)

