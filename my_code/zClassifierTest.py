#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:04:23 2017

@author: isabelleguyon

This is an example of program that tests the Iris challenge Classifier class.
Another style is to incorporate the test as a main function in the Data manager class itself,
but having both is not incompatible (a smaller test with the program and a more developped use case here).

This module could perform hyper-parameter selection by cross-validation
See: http://scikit-learn.org/stable/modules/cross_validation.html.
"""
from zDataManager import DataManager
from zClassifier import Classifier
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import cross_val_score

input_dir = "../public_data"
output_dir = "../res"

basename = 'Iris'
D = DataManager(basename, input_dir) # Load data
print D

myclassifier = Classifier()
 
# Train
Ytrue_tr = D.data['Y_train']
myclassifier.fit(D.data['X_train'], Ytrue_tr)

# Making predictions
Ypred_tr = myclassifier.predict(D.data['X_train'])
Ypred_va = myclassifier.predict(D.data['X_valid'])
Ypred_te = myclassifier.predict(D.data['X_test'])  

# We can compute the training success rate 
acc_tr = accuracy_score(Ytrue_tr, Ypred_tr)
# But it might be optimistic compared to the validation and test accuracy
# that we cannot compute (except by making submissions to Codalab)
# So, we can use cross-validation:
acc_cv = cross_val_score(myclassifier, D.data['X_train'], Ytrue_tr, cv=5, scoring='accuracy')

print "One sigma error bars:"
print "Training Accuracy = %5.2f +-%5.2f" % (acc, ebar(acc, Ytrue_tr.shape[0]))
print "Cross-validation Accuracy = %5.2f +-%5.2f" % (acc_cv.mean(), acc_cv.std())

# If you want to be more conservative and use a 95% confidence interval, use 2*sigma                                          
