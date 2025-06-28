from pydantic import BaseModel

class CodeRequest(BaseModel):
    story: str

class BugFixRequest(BaseModel):
    code: str
    lang: str

class TestCaseRequest(BaseModel):
    code: str

class SummarizeRequest(BaseModel):
    code: str

class ChatRequest(BaseModel):
    message: str