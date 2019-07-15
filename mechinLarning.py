import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = 'pima-indians-diabetes.csv'
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI','DiabetesPedigreeFunction','Age','Class']
dataset = pandas.read_csv(data, names = names)
dataset.plot(kind='pie',subplots=True)
#dataset.hist()
#scatter_matrix(dataset)
plt.show()