from flask import Flask, jsonify, request, session, render_template
from flask_cors import CORS, cross_origin
from automation import Automation
from random import randint
from time import sleep
import csv
import requests
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
########read text file
    print("131313")
    accounts = []

    textFileHandle = open('C:/Users/Administrator/Desktop/bot_selenium/accounts.txt')
    lineList = textFileHandle.readlines()
    for line in lineList:
        temp = {}
        temp["no"] = line.split("&&&")[0]
        temp["email"] = line.split("&&&")[1]
        temp["password"] = line.split("&&&")[2]
        temp["proxy"] = line.split("&&&")[3]
        temp["port"] = line.split("&&&")[4]
        temp["date"] = line.split("&&&")[5]
        accounts.append(temp)

    print("15151515", accounts)
    #########
    return render_template("index.html", data=json.dumps(accounts))

@app.route("/automation/", methods=['POST'])
@cross_origin()
def automation():
    print("automation function called")

    csvfile=open('database.csv','r', newline='')
    obj=csv.reader(csvfile)

    for row in obj:
        if (row[0] == "No"):
            continue
        print(row)
        no = row[0]
        email = row[1]
        password = row[2]
        proxy = row[3]
        port = row[4]
        date = row[5]
        print(email, date)
        # call automation function
        do_automation = Automation()
        do_automation.main(no,email, password, port)

        duration = randint(3,12)
        print("59", duration)
        sleep(30)
    
    return "ok"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0')