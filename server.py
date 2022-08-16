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
        user='root',
        password='1234',
        charset='utf8',
        database='test')
    cur = db.cursor()
    cur.execute('select * from member')
    rs = cur.fetchall()
    cur.close()
    return render_template("member.html", rs=rs)


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
            user='root',
            password='1234',
            charset='utf8',
            database='test')
        cur = db.cursor()
        cur.execute(f'''insert into member 
                    (email,password,name,regdate)
                    values
                    ('{email}', '{pwd}', '{name}', now())''')
        db.commit()
        cur.close()
    return render_template("memberform.html")

# GET: 주소들어왔을때 / POST: submit button


@app.route("/KNeighbors", methods=['GET', 'POST'])
def test():
    pred1 = 'x0과 x1을 입력하셔야 합니다.'
    pred2 = '파일을 업로드 하셔야 합니다.'
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
            pred1 = f'예측하신 타겟값은 = {pred1} 입니다'
            knre = "show"
        except Exception as e:
            print(e)
            pred1 = e
        try:
            f = request.files['filename']
            f.save('upload.png')
            data = cv2.imread('upload.png', cv2.IMREAD_GRAYSCALE)
            pred2 = kclf.predict(data.reshape(-1, 25))
            pred2 = f'업로드하신 파일의 타겟값은 {pred2}입니다.'
            kcl = "show"
        except Exception as e:
            print(e)
            pred2 = e
    return render_template("KNeighbors.html", pred1=pred1, pred2=pred2, knre=knre, kcl=kcl, x1=x1, x2=x2)

@app.route("/car", methods=['GET','POST'])
def car():
    train_input = data[['가격','년식','종류','연비','마력','토크','연료','하이브리드','배기량','중량','변속기']].to_numpy()
    train_target = data['가격'].to_numpy()
    table_data = data[['년식','종류','연비','마력','토크','연료','하이브리드','배기량','중량','변속기','가격']].to_numpy()
    return render_template("car.html",table_data=table_data)

@app.route("/aaa")
def aaa():
    return render_template("aaa.html")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
