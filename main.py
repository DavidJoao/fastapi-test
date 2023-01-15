from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()


## Models
class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str


with open('data/people.json', 'r') as f:
    people = json.load(f)['people']

# Routes
@app.get('/')
def show_people():
    return (people)


@app.get('/person/{p_id}', status_code=200)
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.get('/person/name/{name}')
def get_by_name(name: str):
    person = [p for p in people if p['name'] == name]
    return person


@app.get('/people/gender/{gender}')
def get_by_gender(gender: str):
    person = [p for p in people if p['gender'] == gender]
    return person


@app.get('/person/age/{age}')
def get_by_age(age: int):
    person = [p for p in people if p['age'] == age]
    return person