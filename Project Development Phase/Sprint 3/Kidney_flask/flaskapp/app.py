
from flask import Flask, render_template , request

app = Flask(__name__)

import pickle
model = pickle.load(open(r'C:\Users\Praveen\Downloads\Kidney_flask\CKD.pkl','rb'))

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/index', methods =['POST','GET']) 
def index():
    return render_template("index.html")


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
    

    a=[[float(p),float(q),float(r),float(s),float(t),float(u1),float(v1),float(x),float(y),float(z)]]
    pred= model.predict(a)
    print(pred)

    if (pred == 1):
        output = "Oops,you have chronic Kidney Disease"
        print("Oops,you have chronic Kidney Disease")
    else: 
        output = "Great! you dont have chronic kidney disease"
        print("Great! you dont have chronic kidney disease")
    
    

    return render_template("index.html",y= output)

   
if __name__ == '__main__':
    app.run(debug = True)
