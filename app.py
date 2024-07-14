from flask import Flask,render_template,request
from markupsafe import escape
import pymongo
#===========================================================================================================
connection_str="mongodb+srv://nguyendakacun:htUezXTkL0llRnwa@dangkhang.nbpxo57.mongodb.net/?retryWrites=true&w=majority&appName=DangKhang"
try:
    print("Connect done")
    client = pymongo.MongoClient(connection_str)
except Exception:
    print("Error", Exception)
db = client["mydatabase"]
col = db['todolist']
for x in col.find():
    print(x)
#===========================================================================================================
app = Flask(__name__)

'''dict chua mat khau va tai khoan nguoi dung'''
users = {"Khang":"123456","username":"password"}


'''trang web dau tien'''
@app.route("/")
def hello_world():
    return render_template("register.html")


'''trang web dung de nhap mat khau va ten nguoi dung'''
@app.route("/handle_post",methods=['POST'])
def handle_post():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return render_template("todolist.html")
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login html')
if __name__ == "__main__":
    app.run()