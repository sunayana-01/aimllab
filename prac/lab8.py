from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris = load_iris()

print('Iris data features:', iris.feature_names)
print('Iris data targets:', iris.target_names) 
for i in range(len(iris.target_names)):
    print('Label', i, '-', str(iris.target_names[i]))

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

print('Target:\n', iris.target)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

for i in range(len(x_test)):
    x=x_test[i]
    x_new = np.array([x])
    ypred=knn.predict(x_new)
    print('Actual:', y_test[i], iris.target_names[y_test[i]] , 'Predicted:', ypred, iris.target_names[ypred])

print('Accuracy:', knn.score(x_test, y_test))