#-------------------------------------------------------------------------
# AUTHOR: Zack Muraca
# FILENAME: naive_bayes
# SPECIFICATION: Naive bayes practice
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from numpy import NaN
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data
#--> add your Python code here
db = []
with open('weather_training.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for i, row in enumerate(reader):
		if i > 0:
				db.append(row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for i, row in enumerate(db):
	X.append([])
	for j, val in enumerate(row):
		if j == 5: break
		if val == 'Sunny' or val == 'Hot' or val == 'High' or val == 'Weak':
			X[i].append(1)
		elif val == 'Overcast' or val == 'Mild' or val == 'Normal' or val == 'Strong':
			X[i].append(2)
		elif val == 'Rain' or val == 'Cool':
			X[i].append(3)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for i, row in enumerate(db):
	for j, val in enumerate(row):
		if j == 5:
			if val == 'Yes': Y.append(1)
			else: Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
db_test = []
with open('weather_test.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for i, row in enumerate(reader):
		if i > 0:
			db_test.append(row)

X_test = []
for i, row in enumerate(db_test):
	X_test.append([])
	for j, val in enumerate(row):
		if j == 5: break
		if val == 'Sunny' or val == 'Hot' or val == 'High' or val == 'Weak':
			X_test[i].append(1)
		elif val == 'Overcast' or val == 'Mild' or val == 'Normal' or val == 'Strong':
			X_test[i].append(2)
		elif val == 'Rain' or val == 'Cool':
			X_test[i].append(3)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
predictions = clf.predict_proba(X_test)
for i, p in enumerate(predictions):
	if p[0] >= 0.75 and p[0] > p[1]:
		print(row[0].ljust(15) + row[1].ljust(15) + row[2].ljust(15) + row[3].ljust(15) + row[4].ljust(15), 'Yes'.ljust(15), p[0])
	elif p[1] >= 0.75 and p[1] > p[0]:
		print(row[0].ljust(15) + row[1].ljust(15) + row[2].ljust(15) + row[3].ljust(15) + row[4].ljust(15), 'No'.ljust(15), p[1])
	
