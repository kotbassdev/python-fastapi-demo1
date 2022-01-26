from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'status':200,'message':'hello fastapi'}



#run command
#>uvicorn basic:app --reload