from fastapi import APIRouter
from app1.models.request_models import CodeRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/generate_code")
async def generate_code(req: CodeRequest):
    prompt = f"Generate code for: {req.story}"
    response = watsonx_client().generate_text(prompt)
    return {"code": response if response else "No Output"}