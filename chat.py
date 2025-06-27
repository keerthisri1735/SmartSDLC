from fastapi import APIRouter
from app1.models.request_models import ChatRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/chat")
async def chat(req: ChatRequest):
    prompt = f"{req.message}"
    response = watsonx_client().generate_text({"input": prompt})
    return {"response": response.get("generated_text", "No output")}