from flask import Flask, render_template , request

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "MKIOcGLAjy6Vfgbf0RlcITEBGW4hdRQ4sj2TeNNInKsq"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)

import pickle
#model = pickle.load(open(r'C:\Users\Praveen\Kidneyflask\CKD.pkl','rb'))

@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/login', methods =['POST'])
def login():
    p =request.form["hemo"]
    q =request.form["rc"]
    r =request.form["sg"]
    s =request.form["sc"]
    t =request.form["al"]
    u =request.form["u"]
    if (u=="yes"):
        u1=1
    elif (u=="no"):
        u1=0
    v =request.form["sod"]
    x =request.form["bp"]
    y =request.form["wc"]
    z =request.form["age"]

    A=[[float(p),float(q),float(r),float(s),float(t),float(u1),float(v),float(x),float(y),float(z)]]
    payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9"]], "values":A }]}
    

   
     

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7584b8a4-70b2-4545-8cdb-74d7173ebe80/predictions?version=2022-11-08', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())


    predictions = response_scoring.json()
    pred=predictions['predictions'][0]['values'][0][0]
    
    
    
    if (pred == 0):
        output = "No Kidney Disease"
        print("No Kidney Disease")
    else:
        output = "you have kidney disease"
        print("you have kidney disease")
    


    return render_template("index.html", y = output)
    

if __name__ == '__main__':
    app.run(debug = False)
