from flask import Flask,request,render_template
import csv

app=Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route("/loggedin", methods=['GET','POST'])

def logging_in():
    username = request.form.get("username")
    password = request.form.get("password")
    with open('login_credentials.csv','r+') as current_file:
        open_file=csv.DictReader(current_file)
        for line in open_file:
            if username == line['username']:
                if line['password']==password:
                    return render_template("logged_in.html", username_placeholder="Welcome back " + username)
                else:
                    return render_template("logged_in.html", username_placeholder='Wrong Password')
        return render_template("logged_in.html", username_placeholder='Username doesnt exists')
    
@app.route("/signup",methods=['GET','POST'])
def sign_up():
    username = request.form.get("username")
    password = request.form.get("password")
    with open('login_credentials.csv','r+') as current_file:
        for index,row in enumerate(csv.reader(current_file)):
            if index ==0:
                fieldnames=row
            else:
                break
        open_file = csv.DictWriter(current_file,fieldnames=fieldnames)
        open_file.writerow({'username':username,'password':password})
    return render_template("sign_up.html")
    