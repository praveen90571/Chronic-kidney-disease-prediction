from flask import Flask, render_template , request

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "0LQTKaIU-zf6eoOYKE_5xaUY1A8dU5owCbBs1h4G1NJQ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = Flask(__name__)

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/index', methods =['POST','GET']) 
def index():
    return render_template("index.html")

@app.route('/result', methods =['POST','GET']) 
def result():
    return render_template("resut.html")

@app.route('/login', methods =['POST','GET'])
def login():
    p =request.form["sg"]
    q =request.form["hemo"]
    r =request.form["sc"]
    s =request.form["al"]
    t =request.form["pcv"]
    u =request.form["u"]
    if (u=="yes"):
        u1=1
    elif (u=="no"):
        u1=0
    v =request.form["v"]
    if (v=="yes"):
        v1=1
    elif (v=="no"):
        v1=0
    x=request.form["bgr"]
    y=request.form["rbc"]
    z=request.form["bu"]
    

    A=[[float(p),float(q),float(r),float(s),float(t),float(u1),float(v1),float(x),float(y),float(z)]]
    payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9"]], "values":A }]}


    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f96f18ff-539c-4339-9575-739a6a1c310b/predictions?version=2022-11-11', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())

    predictions = response_scoring.json()
    pred=predictions['predictions'][0]['values'][0][0]
    print(pred)
    
    return render_template("result.html", y = pred)


if __name__ == '__main__':
    app.run(debug = True)
