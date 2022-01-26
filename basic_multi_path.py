from unittest import skip
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/{blog_id},comment/{comment_id}")
async def blog_comment_update(blog_id:int,comment_id:int):
    return {"status":200,"message":"test"}