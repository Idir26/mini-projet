from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeRegressor
import pickle


class Regressor(BaseEstimator):
	def __init__(self):
		pass

	def fit(self, X, y):
		self.clf = DecisionTreeRegressor()
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
