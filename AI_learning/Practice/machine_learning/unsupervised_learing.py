#unsupervised learing
#Clustering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("customer.csv")
print(data)

data["Sex"]=data["Sex"].astype("object")

data1=data.copy()
data1=data1.drop("Cust_Number",axis=1)

sns.pairplot(data1)
plt.show()

filt=data1[["Cust_Spend_Score","Yearly_Income"]]
filt

#sacaling  is mandatoty
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(filt)	
x=pd.DataFrame(x,columns=filt.columns)
x

from sklearn.cluster import KMeans
# Elbow method to find optimal cluster
wcss=[]

for i in range(2,21):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)# wcss calculating function
plt.plot(range(2,21),wcss)


#silhoutee score
from sklearn.metrics import silhouette_score
for i in range(2,20):
    cluster=KMeans(n_clusters=i)
    predict=cluster.fit_predict(x)
    score=silhouette_score(x,predict)
    print("for {} clusters the silcoutte score is {}".format(i,score))

# Model building
clusters=KMeans(n_clusters=5,init="k-means++")
clusters.fit_predict(x)

clusters.cluster_centers_

data["cluster"]=clusters.labels_

sns.scatterplot(x=data["Cust_Spend_Score"],y=data["Yearly_Income"],hue=data["cluster"])
plt.show()

data[data["cluster"]==4].describe(include="all")


##DBScan clustering
datas=pd.read_csv("db2.csv")
datas

datas.drop("Unnamed: 0",axis=1,inplace=True)

sns.scatterplot(x=datas["F1"],y=datas["F2"])
plt.show()

kmeans1=KMeans(n_clusters=2)
clu=kmeans1.fit_predict(datas)

sns.scatterplot(x=datas["F1"],y=datas["F2"],hue=clu)

#DBSCAN
from sklearn.cluster import DBSCAN
db1=DBSCAN(eps=0.15,min_samples=5)
dbclust=db1.fit_predict(datas)
sns.scatterplot(x=datas["F1"],y=datas["F2"],hue=dbclust)
dbclust=db1.fit_predict(datas)


















plt.axvline(x=5,color='red')
plt.show()