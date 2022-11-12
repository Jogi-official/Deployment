import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote


import pickle

app = FastAPI()
pickle_in = open('classifier_new.pkl' ,'rb')
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
    Married_Single = data['Married_Single']
    Car_Ownership  = data['Car_Ownership']
    CURRENT_JOB_YRS = data['CURRENT_JOB_YRS']
    CURRENT_HOUSE_YRS = data['CURRENT_HOUSE_YRS ']


    prediction = classifier.predict([[Income , Age , Experience , Married_Single , Car_Ownership , CURRENT_JOB_YRS , CURRENT_HOUSE_YRS]])
    if(prediction[0] == 0):
        prediction = "Approved"
    else:
        prediction = "Not Approved"
    return {
        "prediction": prediction
    }
if __name__ == '__main__':
    uvicorn.run(app , host = '127.0.0.1' , port = 8000)