import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

x_train = np.array([[2, 1],[3, 2],[3, 4],[5, 5],[7, 5],[2, 5],[8, 9],[9, 10],[6, 12]])
x_test = np.array([[9, 2],[6, 10],[2, 4]])
y_train = np.array([3, 5, 7, 10, 12, 7, 13, 13, 12])
y_test = np.array([13, 12, 6])

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(x_train, y_train)

pred = knr.predict([[3, 3]])
print(pred)

# plt.scatter(x_train[:,0],y_train,label='x[0] and y')
# plt.scatter(x_train[:,1],y_train,label='x[1] and y')
# plt.xlabel('xdata')
# plt.ylabel('ydata')
# plt.savefig('x0_x1_y1.png')
# plt.figure()
# plt.scatter(x_train[:,0],x_train[:,1],label='x_train[:,0],x_train[:,1]')
# plt.savefig('x0_x1_y2.png')
# plt.figure()

plt.scatter(x_train[:,0],x_train[:,1],label='x_train[:,0],x_train[:,1]')
plt.scatter(3,3)
for count,i in enumerate(x_train):
    plt.text(i[0]+0.1,i[1]+0.1,y_train[count])
plt.savefig('x0_x1_y4.png')

