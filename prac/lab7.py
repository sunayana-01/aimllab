from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris=load_iris()
x=pd.DataFrame(iris.data)
x.columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y=pd.DataFrame(iris.target)
y.columns=['Target']

plt.figure(figsize=(14,7))
colormap = np.array(['red', 'lime', 'black'])

model = KMeans(n_clusters=3)
model.fit(x)

scaler = preprocessing.StandardScaler()
scaler.fit(x)
xsa = scaler.transform(x)
xs = pd.DataFrame(xsa, columns = x.columns)
gmm = GaussianMixture(n_components= 3)
gmm.fit(xs)
y_gmm=gmm.predict(xs)

plt.subplot(1,3,1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Target], s=40)
plt.title('Real Dataset')
plt.xlabel('Petal_Length')
plt.ylabel('Petal_Width')

plt.subplot(1,3,2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('KNN Clustering')
plt.xlabel('Petal_Length')
plt.ylabel('Petal_Width')

plt.subplot(1,3,3)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y_gmm], s=40)
plt.title('E-M')
plt.xlabel('Petal_Length')
plt.ylabel('Petal_Width')

plt.show()