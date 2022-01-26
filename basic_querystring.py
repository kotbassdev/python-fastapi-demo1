
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/blog?q=python
@app.get("/blog")
def blog(q:Optional[str] = None):
    return {"status":200,"message":"OK","q":q}