import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Student_Marks.csv")
# print(data.head(10))

#data["number_courses"].value_counts()

correlation = data.corr()

x = np.array(data[["time_study", "number_courses"]])
y = np.array(data["Marks"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)
model = LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)


features = np.array([[4.508, 3]])
predt = model.predict(features)
print(predt)

