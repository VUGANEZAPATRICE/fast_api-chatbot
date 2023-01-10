from fastapi import FastAPI

app = FastAPI()# variable name of the FastAPI instance

@app.get("/") # decorator: path/route
def index():
    return "This is the front page"

@app.get("/about")
def about():
    return "This is the about page"

# pip install fastapi uvicorn
# uvicorn app:app --reload: run the app==>app.py:app==>app.py is the file name, app is the variable name of the FastAPI instance

# render app name: uvicorn app:app --host 0.0.0.0 --port 10000
