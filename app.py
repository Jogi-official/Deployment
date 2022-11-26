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
    Income = (data['Income'] - 10310)/(9999938-10310)
    Age = (data['Age'] - 21)/(79-21)
    Experience = data['Experience']/20
    Married_Single = data['Married_Single']
    Car_Ownership  = data['Car_Ownership']
    CURRENT_JOB_YRS = data['CURRENT_JOB_YRS']/14
    CURRENT_HOUSE_YRS = (data['CURRENT_HOUSE_YRS']-10)/(14-10)


    prediction = classifier.predict([[Income , Age , Experience , Married_Single , Car_Ownership , CURRENT_JOB_YRS , CURRENT_HOUSE_YRS]])
    if(Income < 300000 or Age < 20 ):
        prediction = "Not Approved"

    elif(prediction[0] == 0):
        prediction = "Approved"
    else:
        prediction = "Not Approved"
    return {
        "prediction": prediction
    }
if __name__ == '__main__':
    uvicorn.run(app , host = '127.0.0.1' , port = 8000)