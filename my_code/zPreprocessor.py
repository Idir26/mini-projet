#!/usr/bin/env python
# -*- coding: utf-8 -*-
from outils import *
from sys import argv
from sklearn.base import BaseEstimator
from DataManager import DataManager
from sklearn.preprocessing import OneHotEncoder



class Preprocessor:
	def __init__(self):
		self.table = []
		self.categories = []
		self.transformer = OneHotEncoder();
        def fit(self, X, y=None):
                return self.transformer.fit(X, y)

        def fit_transform(self, X, y=None):
                return self.transformer.fit_transform(X)

        def transform(self, X, y=None):
		return self.transformer.transform(X)		

