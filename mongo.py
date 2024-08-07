from flask import Flask,request,render_template
import pymongo 
app=Flask(_name_)
@app.route("/login",methods=["GET","POST"])
def check():
    if request.method=="GET":
        n=request.args.get("username")
        p=request.args.get("password")
        print("code successful")
    elif request.method=="POST":
        n=request.form["username"]
        p=request.form["password"]
        print("code successful")
        
                           
    else:
        print("Invalid Route")
    flag=data_check(n,p)
    if (flag):
        homepage()
    return None     
    
    
def data_check(n,p):
    
    db=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    if db!=None:
        print("connection Est...")
    dbcoll=db["ScholarshipData"]
    dbname=dbcoll["LoginData"]
    f=dbname.find_one({ "User Name": n,
                      "Password": p,})
    if  f!=None:    
        return True
    else:
        return False                 
                          
                            
@app.route("/signup",methods=["GET","POST"])
def create():
    if request.method=="GET":
        q=request.args.get("username")
        r=request.args.get("password")
        print("Login Successful")
    elif request.method=="POST":
        q=request.form["username"]
        r=request.form["password"]
        print("Login Successful")
        
                           
    else:
        print("Invalid Route")
    data_save(q,r)
    return "Account Succesfully Created" 
def data_save(q,r):
    
    db=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    if db!=None:
        print("connection Est...")
    dbcoll=db["ScholarshipData"]
    dbname=dbcoll["LoginData"]
    dbname.insert_one({ "User Name": q,
                      "Password": r,
                         
                          }
                         )   
@app.route("/search",methods=["GET"])
def search():
    b=request.args.get("Scholarship Name")
    c=request.args.get("Eligibility")
    d=request.args.get("Deadline")

    details(b,c,d) 
    return "succesfull"
def details(b,c,d):
            
            
    db=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    if db!=None:
        print("Connection est...")
    
    dbname=db["ScholarshipData"]
    dbcoll=dbname["ScholarshipDetails"]
    if dbcoll.find_one({ "Name": b
    })!=None or dbcoll.find_one({"Eligibility": c })!=None or dbcoll.find_one({"Deadline": d})!=None:
        return 
        
        
        
        
        return "succesfull"
@app.route("/home")
def homepage():
    return render_template("homepage[1].html")
app.run(port=80)