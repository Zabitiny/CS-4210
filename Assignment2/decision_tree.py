#-------------------------------------------------------------------------
# AUTHOR: Zack Muraca
# FILENAME: Decision Tree
# SPECIFICATION: Train, test, and examine the performance of training decsion trees with various data sets
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for count, ds in enumerate(dataSets):
   dbTraining = []
   X = [[]]
   Y = []

   #reading the training data in a csv file
   with open(ds, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for i, row in enumerate(reader):
         if i > 0: #skipping the header
            dbTraining.append(row)

   #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
   #--> add your Python code here
   # i = 0
   for i, row in enumerate(dbTraining):
      if i != 0: X.append([])
      for j, val in enumerate(row):
         if j == 4: break
         if val == 'Young' or val == 'Myope' or val == 'Yes' or val == 'Normal':
            X[i].append(1)
         elif val == 'Prepresbyopic' or val == 'Hypermetrope' or val == 'No' or val == 'Reduced':
            X[i].append(2)
         elif val == 'Presbyopic':
            X[i].append(3)
	 
   #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
   #--> add your Python code here
   for i, row in enumerate(dbTraining):
      for j, val in enumerate(row):
         if j == 4:
            if val == 'Yes': Y.append(1)
            else: Y.append(2)
						
   
   #loop your training and test tasks 10 times here
   lowest = 1.0
   for i in range (10):
      #fitting the decision tree to the data setting max_depth=3
      clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
      clf = clf.fit(X, Y)
	 
      #read the test data and add this data to dbTest
      #--> add your Python code here
      dbTest = []
      with open('contact_lens_test.csv', 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
            if i > 0: dbTest.append(row)

      #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
      #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
      #--> add your Python code here
      for i, data in enumerate(dbTest):
         for j, val in enumerate(data):
            if val == 'Young' or val == 'Myope' or val == 'Yes' or val == 'Normal':
               dbTest[i][j] = 1
            elif val == 'Prepresbyopic' or val == 'Hypermetrope' or val == 'No' or val == 'Reduced':
               dbTest[i][j] = 2
            elif val == 'Presbyopic':
               dbTest[i][j] = 3

      X_test = [[]]
      Y_test = []
      for i, row in enumerate(dbTest):
         if i != 0: X_test.append([])
         for j, val in enumerate(row):
            if j < 4:
               X_test[i].append(val)
            else:
               Y_test.append(val)
      
      #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
      #--> add your Python code here
      accuracy = 0.0
      for i, prediction in enumerate(clf.predict(X_test)):
         if prediction == Y_test[i]:
            accuracy += 1
      accuracy /= len(dbTest)
      #find the lowest accuracy of this model during the 10 runs (training and test set)
      #--> add your Python code here
      if accuracy < lowest:
         lowest = accuracy
   #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
   #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
   #--> add your Python code here
   print('final accuracy when training on contact_lens_training_{i}.csv:'.format(i=count+1), lowest)