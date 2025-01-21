from fastapi import FastAPI, Request
from api.users_api.users import user_router

app = FastAPI(docs_url='/')
app.include_router(user_router)