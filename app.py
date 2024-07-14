from flask import Flask,render_template,request
from markupsafe import escape
app = Flask(__name__)

'''dict chua mat khau va tai khoan nguoi dung'''
users = {"Khang":"123456","username":"password2"}


'''trang web dau tien'''
@app.route("/")
def hello_world():
    return render_template("index.html")


'''trang web dung de nhap mat khau va ten nguoi dung'''
@app.route("/handle_post",methods=['POST'])
def handle_post():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login html')
if __name__ == "__main__":
    app.run()