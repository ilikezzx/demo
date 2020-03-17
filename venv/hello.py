from flask import Flask,request,render_template,redirect
import pymysql
import os

app = Flask(__name__)

db=pymysql.connect("localhost", 'root', '', 'spring')
cursor = db.cursor()
cursor.execute("select * from accounts")
dataTuple = cursor.fetchall()
data=[]
for itemTuple in dataTuple:
    item=[]
    for smallItem in itemTuple:
        item.append(smallItem)
    data.append(item)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="POST":
        userName=request.form.get("username")
        password = request.form.get("password")

        result=False
        for item in data:
            if item[1] == userName and item[2] == password:
                result=True
        if result ==False: return render_template('login.html',result="登录失败")
        else :return render_template('index.html',data={"username":userName,"password":password})

    return render_template('login.html')

@app.route('/')
def begin():
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)