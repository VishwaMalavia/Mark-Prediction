import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df=pd.read_csv('Student_marks.csv')

x = df[["number_courses", "time_study"]]
y = df["Marks"]

model=LinearRegression()

model.fit(x,y)

pickle.dump(model,open('model.pkl','wb'))

print("model trained & saved")