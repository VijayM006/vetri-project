from flask import Flask, render_template, url_for, request, redirect,session
from flask_mysqldb import MySQL
vj = Flask(__name__)
vj.secret_key="Vijay@006"
vj.config["MYSQL_HOST"]='localhost'
vj.config["MYSQL_USER"]='root'
vj.config["MYSQL_PASSWORD"]='Vijay@006'
vj.config["MYSQL_DB"]='vetri'
mysql=MySQL(vj)
static_url_path='/static'
@vj.route("/")
def index():
    return render_template("index.html")

@vj.route("/colbutton")
def colbutton():
    return redirect(url_for('college'))

@vj.route("/college")
def college():

    return render_template("college.html")

@vj.route("/schbutton")
def  schbutton():
    return redirect(url_for('schools'))

@vj.route("/schools")
def schools():
    return render_template("school.html")

@vj.route("/unibutton")
def  unibutton():
    return redirect(url_for('university'))

@vj.route("/university")
def university():
    return render_template("university.html")

@vj.route("/websites")
def websites():
    return render_template("websites.html")


@vj.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        Name=request.form.get("Name")
        Password=request.form.get("Password")
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM signup WHERE name=%s AND Password=%s",(Name,Password))
        data=cur.fetchall
        cur.connection.commit()
        cur.close()
        if data:
            session["Name"]=Name
            return redirect(url_for('websites'))
        else:
            return "Invalid password"
    return render_template("login.html")

@vj.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("Name")
        password = request.form.get("Password")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO signup (Name, Password) VALUES (%s, %s)", (name, password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("login"))  # Assuming you have a login route
    return render_template("signup.html")

@vj.route('/')
def logout():
    session.pop("Name",None)
    redirect(url_for('home'))



if __name__ == "__main__":
    vj.run(debug=True)
