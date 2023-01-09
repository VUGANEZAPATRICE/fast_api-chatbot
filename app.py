from fastapi import FastAPI

app = FastAPI()# variable name of the FastAPI instance

@app.get("/") # decorator: path/route
def index():
    return "This is the front page"
# pip install fastapi uvicorn
# uvicorn app:app --reload: run the app==>app.py:app==>app.py is the file name, app is the variable name of the FastAPI instance