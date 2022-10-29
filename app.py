import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle

app = FastAPI()
pickle_in = open('classifier.pkl' ,'rb')
classifier = pickle.load(pickle_in)

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
    balance = data['balance']
    print(balance)
    AnnualSalary = data['AnnualSalary']
    print(AnnualSalary)
    Employed = data['Employed']
    # print(classifier.predict([[balance , AnnualSalary , Employed]]))
    print("Hello")
    prediction = classifier.predict([[balance , AnnualSalary , Employed]])
    if(prediction[0] == 0):
        prediction = "Not Approved"
    else:
        prediction = "Approved"
    return {
        "prediction": prediction
    }
if __name__ == '__main__':
    uvicorn.run(app , host = '127.0.0.1' , port = 8000)