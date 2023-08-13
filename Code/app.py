#Loading libraries
import uvicorn
from fastapi import FastAPI
import joblib
#from CarDesc import Car_Desc
import os
import numpy as np

from pydantic import BaseModel

class Car_Desc(BaseModel):
    Year:int
    Mileage:int
    City:str
    State:str
    Make:str
    Model:str

app=FastAPI()
#Fetching the file name for model to load
curr_dir=os.getcwd()
parent_path=os.path.dirname(curr_dir)
folder_name='Model'

model_filename=os.path.join(parent_path,folder_name,'linear_reg.joblib')
model=joblib.load(model_filename)

#Index route
@app.get('/')
def index():
    return {'message': 'Its working'}

#responding user
@app.get('/{name}')
def get_name(name:str):
    return {'message':'Hello ,{0}'.format(name)}

#responding for pred request
@app.post('/predict')
def get_pred(data:Car_Desc):
    data=data.model_dump()
   
    Year=data['Year']
    Mileage=data['Mileage']
    City=data['City']
    State=data['State']
    Make=data['Make']
    Model=data['Model']
    query=[Year,Mileage,City,State,Make,Model]

    
    res=model.predict([query])
    return {
        'Price':res[0]
    
    }

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)





