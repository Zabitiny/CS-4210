#-------------------------------------------------------------------------
# AUTHOR: Zack Muraca
# FILENAME: find_s.py
# SPECIFICATION: Use Find-S algorithm on the contact_lens.csv dataset
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
hypothesis[0] = db[3][0]
hypothesis[1] = db[3][1]
hypothesis[2] = db[3][2]
hypothesis[3] = db[3][3]

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
for row in db:
	if row[4] == 'No':
		continue
	for i in range(num_attributes):
		if hypothesis[i] != row[i]:
			hypothesis[i] = '?'


print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)