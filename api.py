from fastapi import FastAPI, File, UploadFile
import uvicorn
from pydantic import BaseModel
import pickle
import pandas as pd

class Credit(BaseModel) :
    age:int
    job:int
    marital:int
    education:int
    default:int
    balance:int
    housing:int
    loan:int
    campaign:int
    pdays:int
    previous:int
    poutcome:int

tags =[
     {
          "name": "Hello",
          "description":"Hello World"
     },
     {
          "name":"Predict",
          "description":"Predict"
     },
     {
          "name":"Predict",
          "description":"Predict"
     },
     {
          "name":"upload",
          "description":"chargement de fichier"
     },
     {
          "name":"Root Square",
          "description":"Calcul de carré"
     }
]

app = FastAPI(
     title="Appli de prédiction",
     description="API de prédiction",
     version="1.0.0",
     openapi_tags = tags
)

@app.get("/", tags=["Hello", "Root Square"])
def index():
    return {"message" : "Hello world"}

@app.get("/hello")
def hello(name:str="World"):
    return{"message" : f"hello {name}"}

@app.get("/hello/{name}")
def hello(name:str):
    return{"message" : f"hello {name}"}

@app.post("/root_square")
def root_square(number:int=1):
    return {"result":number**0.5}

@app.post("/predict")
def predict(credit: Credit) -> str:
        with open('model.pkl', 'rb') as f: model=pickle.load(f)
        predict_value = int(model.predict([list(credit.model_dump().values())])[0])
        # credit = credit.model_dump()
        return {"pred" : predict_value}

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile =File(...)):
    with open(file.filename, 'r') as fichier_csv:
         credit = pd.read_csv(fichier_csv)

    with open('model.pkl', 'rb') as f: model=pickle.load(f)

    predict_value=model.predict(credit)  

    return str(predict_value)


if __name__ == "__main__" :
    uvicorn.run(app, host="0.0.0.0", port=8080)