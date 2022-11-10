
from flask import Flask, render_template , request

app = Flask(__name__)

import pickle
model = pickle.load(open(r'C:\Users\Praveen\Kidneyflask\CKD.pkl','rb'))

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

    a=[[float(p),float(q),float(r),float(s),float(t),float(u1),float(v),float(x),float(y),float(z)]]
    output= model.predict(a)
    print(output)
    #pred = render_template("index.html",y= " "+ str(output[0])

    return render_template("index.html",y= " "+ str(output[0]))

    #if(pred == 0):
        #print("Great, you dont have a kidney disease")
    #elif(pred == 1):
        #print("Oops, you have a chronic kidney disease")

if __name__ == '__main__':
    app.run(debug = True)
