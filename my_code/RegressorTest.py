from regressor import Regressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from data_manager import DataManager




input_dir = "../public_data"
output_dir = "../res"
basename = 'movierec'

D = DataManager(basename, input_dir) # Load data
print D
myRegressor = Regressor()

Ytraint = D.data['Y_train']
myRegressor.fit(D.data['X_train'], Ytraint)

Ytrain_pred = myRegressor.predict(D.data['X_train'])
Yvalid_pred = myRegressor.predict(D.data['X_valid'])
Ytest_pred = myRegressor.predict(D.data['X_test'])
train_acc = accuracy_score(Ytrue_tr, Ypred_tr)

scores = cross_val_score(myRegressor, D.data['X_train'], Ytraint, cv=5)

#Le score moyen et l'intervalle de confiance à 95% sont donnés par :
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2

                                        
