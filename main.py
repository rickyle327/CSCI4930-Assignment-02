# A sample driver program
# PLEASE DO NOT SUBMIT


from Assigned import *

q = Assigned(full_dataset_filename='./dataset/baby-weights-dataset.csv',
             judge_filename='dataset/judge-without-labels.csv')

tuple = q.Q_03(q.Q_02(q.full_dataset))
print(tuple[0])
print(tuple[1])