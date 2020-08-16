import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import BernoulliNB

class Dota_NB:
    def __init__(self):
        fo=open("id_name.json","r")
        self.id_name_dic=json.loads(fo.read())
        fo.close()
        self.hero_num=0
        for i in self.id_name_dic:
            if int(i)>self.hero_num:
                self.hero_num=int(i)

        dataset=pd.read_csv("X.csv",header=None).values
        X_0=dataset[:,0:10]
        self.Y=dataset[:,10]

        self.X=np.zeros([X_0.shape[0],self.hero_num*2],dtype=np.bool_)
        for i in range(0,X_0.shape[0]):
            for k in range(0,5):
                self.X[i][X_0[i][k]-1]=True
            for j in range(5,10):
                self.X[i][X_0[i][j]-1+self.hero_num]=True

        self.clf=BernoulliNB()
        self.clf.fit(self.X,self.Y)

    def predict_one(self,X_test):
        return self.clf.predict([X_test])[0]
    def predict_one_proba(self,X_test):
        return max(self.clf.predict_proba([X_test])[0])

    def predict_many(self,X_test):
        return self.clf.predict(X_test)
