from pydantic import BaseModel

class Car_Desc(BaseModel):
    Year:int
    Mileage:int
    City:str
    State:str
    Make:str
    Model:str