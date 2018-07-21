import codecademylib
#1
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#2 - 33
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print total_ceballos
#3 - 47
percentage_ceballos = 100*total_ceballos/len(survey_responses)
print percentage_ceballos

total_survey = len(survey_responses)
print total_survey

#4


possible_surveys = np.random.binomial(70, .54, size=10000)/float(70)
print possible_surveys

#5
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show

#6
ceballos_loss_surveys = np.mean(possible_surveys < .5)
print ceballos_loss_surveys

#7
large_surveys = np.random.binomial(7000, .54, size=10000)/float(7000)
print large_surveys

#8
ceballos_loss_new = np.mean(large_surveys)
print large_surveys
