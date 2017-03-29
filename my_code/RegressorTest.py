#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from DataManager import DataManager
from Regressor import Regressor
from sklearn.metrics import accuracy_score 
#from sklearn.model_selection import cross_val_score

input_dir = "../public_data"
output_dir = "../res"

basename = 'movierec'
D = DataManager(basename, input_dir) # Load data
print D

myRegressor = Regressor()
 
# Train
Ytrue_tr = D.data['Y_train']
myRegressor.fit(D.data['X_train'], Ytrue_tr)

# Making predictions
Ypred_tr = myRegressor.predict(D.data['X_train'])
Ypred_va = myRegressor.predict(D.data['X_valid'])
Ypred_te = myRegressor.predict(D.data['X_test'])  

# We can compute the training success rate 
acc_tr = accuracy_score(Ytrue_tr, Ypred_tr)
# But it might be optimistic compared to the validation and test accuracy
# that we cannot compute (except by making submissions to Codalab)
# So, we can use cross-validation:
#acc_cv = cross_val_score(myRegressor, D.data['X_train'], Ytrue_tr, cv=5, scoring='accuracy')

                                        
