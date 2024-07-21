from flask import Flask,render_template,request,redirect,url_for
from markupsafe import escape
import pymongo
from werkzeug.security import check_password_hash,generate_password_hash
#===========================================================================================================
connection_str="mongodb+srv://nguyendakacun:htUezXTkL0llRnwa@dangkhang.nbpxo57.mongodb.net/?retryWrites=true&w=majority&appName=DangKhang"
users_value={}
try:
    print("Connect done")
    client = pymongo.MongoClient(connection_str)
except Exception:
    print("Error", Exception)
db = client["mydatabase"]
col = db['user_data']

for x in col.find():
    user = x["user"]
    password = x["password"]
    print(x)
    users_value.update({user:password})
#===========================================================================================================
app = Flask(__name__)

'''dict chua mat khau va tai khoan nguoi dung'''
#users = {"Khang": generate_password_hash("123456"), "username": generate_password_hash("password")}


'''trang web dau tien'''
@app.route("/")
def first_page():
    return render_template("first_page.html")
@app.route('/register_rq')
def register_rq():
    return redirect(url_for('register'))
@app.route("/register")
def register():
    return render_template("register.html")
@app.route('/login_rq')
def login_rq():
    return redirect(url_for('login'))
@app.route("/login")
def login():
    return render_template("login.html")
'''trang web dung de nhap mat khau va ten nguoi dung'''
@app.route("/handle_get",methods=['GET'])
def handle_get():
    error = None
    if request.method == "GET":
        username = request.form["username"]
        password = request.form["password"]
        print("username: "+ username+" password: "+ password)
        if username in users_value and users_value[username]==password:
                # Successful login, redirect to todolist
                return render_template("todolist.html")
        else:
            # Username not found
            return render_template("login.html", error=error)  # Pass error message
    else:
        # Not a POST request (unexpected)
        return render_template("login.html", error="Unexpected request method")
@app.route("/handle_post",methods=['GET','POST'])
def handle_post():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username != "" and password !="":
            add_user={"user": username,"password":password}
            X = col.insert_one(add_user)
            return render_template("todolist.html")
        else:
            # Username not found
            return render_template("register.html")  # Pass error message      
    return render_template("register.html")  # Pass error message      
if __name__ == "__main__":
    app.run()