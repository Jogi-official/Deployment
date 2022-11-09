import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder

import pickle

app = FastAPI()
pickle_in = open('classifier_new.pkl' ,'rb')
classifier = pickle.load(pickle_in)
df = pd.read_csv('Training Data.csv')
df.rename(columns={"Married/Single": "Married_Single"}, inplace=True)
encoder = LabelEncoder()
df["Married_Single"] = encoder.fit_transform(df["Married_Single"])
df["Car_Ownership"] = encoder.fit_transform(df["Car_Ownership"])
df = df.drop(['Id', 'Profession', 'CITY', 'STATE', 'House_Ownership'], axis=1)
X = df.drop("Risk_Flag", axis=1)
y = df["Risk_Flag"]
smote = SMOTE(sampling_strategy='minority')
X_sm_original, y_sm_original = smote.fit_resample(X, y)
sc = StandardScaler()
sc.fit(X_sm_original, y_sm_original)


@app.get('/')
def index():
    return {'messgae' : "Hello , Sir/Mam"}

@app.get('/{name')

def get_name(name : str):
    return {'messgae' :f'Hello ,{name}'}

@app.post('/predict')
def predict_species(data:BankNote):
    data = data.dict()
    print(data)
    print("Hello")


    # balance = data['balance']
    # # print(balance)
    # AnnualSalary = data['AnnualSalary']
    # # print(AnnualSalary)
    # Employed = data['Employed']
    # print(classifier.predict([[balance , AnnualSalary , Employed]]))
    print("Hello")

    Income = data['Income']
    Age = data['Age']
    Experience = data['Experience']
    Married_Single = data['MarriedSingle']
    Car_Ownership  = data['Car_Ownership']
    CURRENT_JOB_YRS = data['CurrentJob_YRS']
    CURRENT_HOUSE_YRS = data['CurrentHour_YRS']

    # sc.transform([Income , Age , Experience , Married_Single , Car_Ownership , CURRENT_JOB_YRS , CURRENT_HOUSE_YRS ])
    prediction = classifier.predict([[sc.transform([[Income , Age , Experience , Married_Single , Car_Ownership , CURRENT_JOB_YRS , CURRENT_HOUSE_YRS ]])]])
    if(prediction[0] == 0):
        prediction = "Not Approved"
    else:
        prediction = "Approved"
    return {
        "prediction": prediction
    }
if __name__ == '__main__':
    uvicorn.run(app , host = '127.0.0.1' , port = 8000)