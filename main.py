from fastapi import FastAPI
from routers.salon_router import router as salon_router
from routers.user_router import router as user_router
from routers.review_router import router as review_router
from routers.master_router import router as master_router

app = FastAPI(
    title="Sijil app"
)

app.include_router(salon_router)
app.include_router(user_router)
app.include_router(review_router)
app.include_router(master_router)


@app.get('/')
def root():
    return {"message: ": "hello world!"}
