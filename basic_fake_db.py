from unittest import skip
from fastapi import FastAPI

app = FastAPI()

fake_blog_db = [{"blog":"Blog-A"},{"blog":"Blog-B"},{"blog":"Blog-C"},{"blog":"Blog-D",}]

# fetch -X GET http://127.0.0.1:8000/blog?skip=0
@app.get("/blog")
async def blog(skip:int,limit:int = 10):
    return fake_blog_db[skip: skip + limit]