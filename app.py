from flask import Flask,render_template,request,redirect
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
def hello_world():
    return render_template("register.html")


'''trang web dung de nhap mat khau va ten nguoi dung'''
@app.route("/handle_post",methods=['POST'])
def handle_post():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users_value and users_value[user]==password:
                # Successful login, redirect to todolist
                return render_template("todolist.html")
        else:
            # Username not found
            return render_template("login.html", error=error)  # Pass error message
    else:
        # Not a POST request (unexpected)
        return render_template("login.html", error="Unexpected request method")                                            
if __name__ == "__main__":
    app.run()