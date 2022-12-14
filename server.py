from flask import Flask, render_template, request
from fileutils import myfile
import pymysql

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

from ml.knclf import MyKNclf
import cv2

app = Flask(__name__)
app.register_blueprint(myfile.app)

kclf = MyKNclf().getModel()
data = pd.read_excel('static/data/carprice/carprice.xlsx')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/member")
def member():
    db = pymysql.connect(
        host="localhost",
        user='do1',
        password='do1',
        charset='utf8',
        database='python')
    cur = db.cursor()
    cur.execute('select * from member')
    rs = cur.fetchall()
    cur.close()
    return render_template("member.html", rs=rs)


# GET: ????????????????????? / POST: submit button

@app.route("/memberform", methods=['GET', 'POST'])
def memberform():
    if request.method == 'GET':
        print('get')
        pass
    elif request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']
        name = request.form['name']
        db = pymysql.connect(
            host="localhost",
            user='do1',
            password='do1',
            charset='utf8',
            database='python')
        cur = db.cursor()
        cur.execute(f'''insert into member 
                    (email,password,name,regdate)
                    values
                    ('{email}', '{pwd}', '{name}', now())''')
        db.commit()
        cur.close()
    return render_template("memberform.html")


@app.route("/KNeighbors", methods=['GET', 'POST'])
def test():
    pred1 = 'x0??? x1??? ??????????????? ?????????.'
    pred2 = '????????? ????????? ????????? ?????????.'
    knre = ""
    kcl = ""
    x1 = 4
    x2 = 5
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            x_train = np.array([[2, 1], [3, 2], [3, 4], [5, 5], [
                               7, 5], [2, 5], [8, 9], [9, 10], [6, 12]])
            x_test = np.array([[9, 2], [6, 10], [2, 4]])
            y_train = np.array([3, 5, 7, 10, 12, 7, 13, 13, 12])
            y_test = np.array([13, 12, 6])

            knr = KNeighborsRegressor(n_neighbors=3)
            knr.fit(x_train, y_train)
            x, y = int(request.form['x0']), int(request.form['x1'])
            x1=x
            x2=y
            pred1 = knr.predict([[x, y]])
            pred1 = f'???????????? ???????????? = {pred1} ?????????'
            knre = "show"
        except Exception as e:
            print(e)
            pred1 = e
        try:
            f = request.files['filename']
            f.save('upload.png')
            data = cv2.imread('upload.png', cv2.IMREAD_GRAYSCALE)
            pred2 = kclf.predict(data.reshape(-1, 25))
            pred2 = f'??????????????? ????????? ???????????? {pred2}?????????.'
            kcl = "show"
        except Exception as e:
            print(e)
            pred2 = e
    return render_template("KNeighbors.html", pred1=pred1, pred2=pred2, knre=knre, kcl=kcl, x1=x1, x2=x2)

@app.route("/car", methods=['GET','POST'])
def car():
    train_input = data[['??????','??????','??????','??????','??????','??????','??????','???????????????','?????????','??????','?????????']].to_numpy()
    train_target = data['??????'].to_numpy()
    table_data = data[['??????','??????','??????','??????','??????','??????','???????????????','?????????','??????','?????????','??????']].to_numpy()
    return render_template("car.html",table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
