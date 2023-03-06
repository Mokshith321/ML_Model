from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/naveenm/Desktop/SKILL_WEBDEV/ML_Model/static/Naukri_Jobs_Data.csv")
df = df[:24000:]
df = df.drop(columns=["Posted_as_on_22_5_2022", "job_description"])

# Changing the object type to numerical representation
le = preprocessing.LabelEncoder()

df["job_post"] = le.fit_transform(df["job_post"])
df["required_skills"] = le.fit_transform(df["required_skills"])
df["exp_required"] = le.fit_transform(df["exp_required"])
df["salary_offered"] = le.fit_transform(df["salary_offered"])
df["job_location"] = le.fit_transform(df["job_location"])

x = df.drop(columns=["company"])
y = df["company"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(x, y)

