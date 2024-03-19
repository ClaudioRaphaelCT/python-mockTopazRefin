from fastapi import FastAPI
from modules.excluir_refin.controller.Refin import Refin
from modules.excluir_refin.Model.Refin_body import NumeroBeneficio

app = FastAPI()


@app.get('/')
def home():
    return {"tip": "/docs"}


@app.post('/excluir-refin')
def post_refin(numeroBeneficio: NumeroBeneficio = None):
    return Refin.get(numeroBeneficio)
