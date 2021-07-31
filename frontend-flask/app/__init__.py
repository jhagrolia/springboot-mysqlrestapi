import requests as rq
from subprocess import getoutput, getstatusoutput
from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        backend_url = "http://localhost"
        userid = request.form.get("user_id")
        action = request.form.get("action")
        content = request.form.get("content")
                
        if action == "get":
            if userid == 0 or userid == None:
                userid = ""
            response = rq.get("{0}/api/v1/users/{1}/{2}/".format(backend_url, action, userid))
        elif action == "create":
            response = rq.post("{0}/api/v1/users/create/".format(backend_url), headers = {'Content-type': 'application/json'}, data = content)
        elif action == "update":
            if userid == None:
                userid = ""
            response = rq.put("{0}/api/v1/users/update/{1}".format(backend_url, userid), headers = {'Content-type': 'application/json'}, data = content)
        elif action == "delete":
            if userid == None:
                userid = ""
            response = rq.delete("{0}/api/v1/user/delete/{1}".format(backend_url, userid))

        try:
            json_output = pd.json_normalize(response.json())
            final_output = json_output.to_markdown(index=False)
        except:
            final_output = response.text
        return render_template("index.html", output = final_output, header = response)
    return render_template("index.html")
