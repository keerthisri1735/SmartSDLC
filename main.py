from fastapi import FastAPI
from app1.routes import upload, codegen, bugfix, tests, summarize, chat

app = FastAPI()

app.include_router(upload.router)
app.include_router(codegen.router)
app.include_router(bugfix.router)
app.include_router(tests.router)
app.include_router(summarize.router)
app.include_router(chat.router)
url = "http://127.0.0.1:8000/docs"
@app.get("/")
def read_root():
    return "Welcome to SmartSDLC", url
