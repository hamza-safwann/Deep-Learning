from fastapi import FastAPI
from app.database import engine, Base
from app.routes import posts, users, comments

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the mini Facebook backend!"}
