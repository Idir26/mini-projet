#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sklearn.base import BaseEstimator
from zPreprocessor import Preprocessor

from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
import pickle
    


    
class Regressor(BaseEstimator):
	def __init__(self):
         regressor = Pipeline([
                ('preprocessing', Preprocessor()),
                ('regression', DecisionTreeRegressor())])
         self.clf = regressor

	def fit(self, X, y):
         self.clf.fit(X, y)

	def predict(self, X):
         return self.clf.predict(X)

	def predict_proba(self, X):
         return self.clf.predict_proba(X) # The classes are in the order of the labels returned by get_classes

	def get_classes(self):
         return self.clf.classes_

	def save(self, path="./"):
         pickle.dump(self, open(path + '_model.pickle', "w"))

	def load(self, path="./"):
         self = pickle.load(open(path + '_model.pickle'))
         return self


