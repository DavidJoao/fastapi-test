from fastapi import FastAPI

app = FastAPI()


@app.get('/hello') ##specifies path
def hello_world():
    return { "Hello": "World" }


@app.get('/')
def home():
    return { "Page": "Home" }

    