import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import cross_val_score
import pickle

def main():
	path ='/home/hackathontest/hackathonproject/venv/src/'
	#Data preparation
	df = pd.read_csv(path+'data.txt',sep=';\t',names = ["ip","last_rate","attacking"],engine = 'python')
	X1= df.last_rate.reshape(df.shape[0])
	X2= df.ip.reshape(df.shape[0],1)
	X = df[['ip','last_rate']]
	Y= df.attacking.reshape(df.shape[0],1)
	y = np.ravel(Y)
	#Training without validation
	model = LogisticRegression()
	model = model.fit(X, y)

	#Save model
	fileObject = open(path+'LR','wb')
	pickle.dump(model, fileObject)
	fileObject.close()

	print model.score(X, y)

	#10 fold cross validation
	pipeline = LogisticRegression()
	param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
	gs = GridSearchCV(pipeline, param_grid= param_grid, cv=10)
	gs.fit(X, y)
	pipeline1 = gs
	#Save model
	fileObject1 = open(path+'LRCV','wb')
	pickle.dump(pipeline1, fileObject1)
	fileObject1.close()

	#Get accuracy for 10 folds CV
	scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)
	print scores.mean()

if __name__ == "__main__":
	print("Start training")
    	main()
	print("Training finished!")
