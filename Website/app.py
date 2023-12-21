from flask import Flask, render_template,request,url_for

app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def index():
    if "name" in request.args:
        name_variable =", " + request.args["name"]
    else:
        name_variable=""
    return render_template("index.html" , name_placeholder=name_variable)
#Here we will have a key value pair in the url ?name="some value" and desplay it onto the website
#The "name" in request.args is the key, the name variable and name placeholder could also be called "name", but for clarity's sake i'll leave it as is


@app.route("/music")
def route2():
    return render_template("music.html")

