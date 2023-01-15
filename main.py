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
    people = json.load(f)

# Routes
@app.get('/')
def show_people():
    return (people)


## Post a person
@app.post('/addPerson', status_code=201)
def add_person( person: Person):
    p_id = max([p['id'] for p in people]) + 1
    new_person = {
        "id": p_id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender 
    }

    people.append(new_person)

    with open('data/people.json', 'w') as f:
        json.dump(people, f)

    return new_person


## Delete a Person
@app.delete('/deletePerson/{p_id}')
def delete_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    people.remove(person[0])

    with open('data/people.json', 'w') as f:
        json.dump(people, f)

    return person

## Get person by ID
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