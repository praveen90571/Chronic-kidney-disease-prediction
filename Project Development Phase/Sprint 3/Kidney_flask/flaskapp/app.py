
from flask import Flask, render_template , request

app = Flask(__name__)

import pickle
model = pickle.load(open(r'C:\Users\Praveen\Downloads\Praveen\CKD.pkl','rb'))

@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/login', methods =['POST'])
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
    

    a=[[float(p),float(q),float(r),float(s),float(t),float(u1),float(v1),float(x),float(y),float(z)]]
    output= model.predict(a)
    print(output)
    

    return render_template("index.html",y= " "+ str(output[0]))

   
if __name__ == '__main__':
    app.run(debug = True)
