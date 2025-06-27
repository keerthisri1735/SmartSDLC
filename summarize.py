from fastapi import APIRouter
from app1.models.request_models import SummarizeRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/summarize")
async def summarize_code(req: SummarizeRequest):
    prompt = f"Summarize the purpose and logic of this code:\n{req.code}"
    response = watsonx_client().generate_text({"input": prompt})
    return {"summary": response.get("generated_text", "No output")}