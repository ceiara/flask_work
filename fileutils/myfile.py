from flask import Blueprint, send_file
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

app = Blueprint("myfile",__name__)

@app.route("/filedown/<ox>")
def filedownox(ox):
    if 'o' in ox:
        return send_file('./static/img/x_data[0]_cv.png', as_attachment=True)
    elif 'x' in ox:
        return send_file('./static/img/x_data[3]_cv.png', as_attachment=True)
    return f"ox = {ox}"

@app.route("/knrfiledown/<int:x1>/<int:x2>")
def knrfiledown(x1, x2):
    plt.title('Target Graph')
    x_train = np.array([[2, 1],[3, 2],[3, 4],[5, 5],[7, 5],[2, 5],[8, 9],[9, 10],[6, 12]])
    y_train = np.array([3, 5, 7, 10, 12, 7, 13, 13, 12])
    plt.scatter(x_train[:,0],x_train[:,1])
    for count,i in enumerate(x_train):
        plt.text(i[0]+0.1,i[1]+0.1,y_train[count])
    knr = KNeighborsRegressor(n_neighbors=3)
    knr.fit(x_train, y_train)
    pred = knr.predict([[x1,x2]])
    plt.scatter(x1,x2)
    plt.text(x1+0.1, x2+0.1,np.round(pred[0],decimals=3))
    plt.xlabel('x1')
    plt.xlabel('x2')
    img = BytesIO()
    plt.savefig(img,format="png",dpi=100)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')
    








