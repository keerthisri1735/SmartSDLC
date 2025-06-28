from fastapi import APIRouter
from app1.models.request_models import ChatRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/chat")
async def chat(req: ChatRequest):
    prompt = f"{req.message}"
    response = watsonx_client().generate_text(prompt)
    return {"response": response if response else "No Output"}