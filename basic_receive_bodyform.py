from fastapi import FastAPI
from pydantic  import BaseModel

app = FastAPI()

class Workermodel(BaseModel):
    worker_name: str

# fetch -X 'PUT' 'http://127.0.0.1:8000/worker/1' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"worker_name\": \"kotbass\"}'
@app.put("/worker/{worker_id}")
def update_worker(worker_id: int, model: Workermodel):
    return {"status":200,"message":"OK",'model':model}
