import pandas as pd
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

img = None
clicked = False
r = g = b = 0
X_pos = Y_pos = 0

def set_path(cls,al):
	path = cls
	algo = al
	doit(path,al)

def classify(X, y):
	model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
	model = model.fit(X,y)
	return model

def Logisticregression(X, y):
	# Training the model
	model = LogisticRegression()
	model = model.fit(X,y)
	return model

def SVM(X, y):
	# Training the model
	model = SVC()
	model = model.fit(X,y)
	return model

def DesicionTree(X, y):
	# Training the model
	model = DecisionTreeClassifier(random_state=0)
	model = model.fit(X,y)
	return model

def RandomForest(X, y):
	model = RandomForestClassifier()
	model = model.fit(X,y)
	return model

def calc_accuracy(model):
	index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
	dataset = pd.read_csv('colors.csv', names=index, header = None)
	dataset = dataset.drop(columns = ['color','hex'])
	X = dataset.drop(columns=['color_name'])
	y = dataset['color_name']
	dataset_test = dataset.sample(frac = 0.20)
	X_test = dataset_test.drop(columns=['color_name'])
	y_test = dataset_test['color_name']
	y_pred = model.predict(X_test)
	cm = confusion_matrix(y_test, y_pred)
	accuracy = accuracy_score(y_test, y_pred)

	accuracy = float("{:.2f}".format(accuracy*100))
	return accuracy
		

def accuracy_send():
	index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
	dataset = pd.read_csv('colors.csv', names=index, header = None)
	dataset = dataset.drop(columns = ['color','hex'])
	X = dataset.drop(columns=['color_name'])
	y = dataset['color_name']
	acc_model_KNN = calc_accuracy(classify(X,y))
	acc_model_LR =  calc_accuracy(Logisticregression(X, y))	
	acc_model_SVM =  calc_accuracy(SVM(X, y))	
	acc_model_DT =   calc_accuracy(DesicionTree(X, y))	
	acc_model_RF =   calc_accuracy(RandomForest(X, y))

	return acc_model_KNN,acc_model_LR,acc_model_SVM,acc_model_DT,acc_model_RF 

def Prediction(R,G,B,algo):
	index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
	dataset = pd.read_csv('colors.csv', names=index, header = None)
	dataset = dataset.drop(columns = ['color','hex'])
	X = dataset.drop(columns=['color_name'])
	y = dataset['color_name']
	model = None
	algo_name = None
	if algo == 'KNN':
		model = classify(X,y)
		algo_name = 'K-Nearest Neighbour'
	elif algo == 'LR':
		model =  Logisticregression(X, y)
		algo_name = 'Logistic Regression'
	elif algo == 'SVM':
		model = SVM(X, y)
		algo_name = 'Support Vector Machine'
	elif algo == 'DT':
		model = DesicionTree(X, y)
		algo_name = 'Decision Tree'
	elif algo == 'RF':
		model = RandomForest(X, y)
		algo_name = 'Random Forest'
	y_pred_color = model.predict([[R,G,B]])
	color = y_pred_color[0]
	return color

def DrawFunction(event,x,y,flag,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b,g,r,xpos,ypos, clicked,img
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)
		
def doit(path,al):
	global img,clicked,r,g,b
	img = cv2.imread(path)
	cv2.imshow('Output',img)
	img = cv2.resize(img, (750, 750))
	cv2.namedWindow('Output')
	cv2.setMouseCallback('Output',DrawFunction)
	while(1):
		cv2.imshow("Output",img)
		if (clicked):
			cv2.rectangle(img,(0,0), (750,60), (b,g,r), -1)
			text = Prediction(r,g,b,al) + ' R->'+ str(r) + '   G->'+ str(g) + '   B->'+ str(b)
			cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
			msg = "To exit press esc"
			cv2.putText(img, msg,(20,20),2,0.8,(255,255,255),2,cv2.LINE_AA)
			if(r+g+b>=600):
				cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
				cv2.putText(img, msg,(20,20),2,0.8,(0,0,0),2,cv2.LINE_AA)
			clicked=False
		if cv2.waitKey(20) & 0xFF ==27:
			break
	cv2.destroyAllWindows()
