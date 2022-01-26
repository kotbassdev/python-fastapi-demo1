from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/blog/1
@app.get('/blog/{blog_id}')
def blog_id(blog_id:int):
    return {"status":200,"message":"OK","blog_id":blog_id}