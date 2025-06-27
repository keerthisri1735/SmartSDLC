from fastapi import APIRouter
from app1.models.request_models import BugFixRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/fix_bug")
async def fix_bug(req: BugFixRequest):
    prompt = f"Fix the bugs in this {req.lang} code:\n{req.code}"
    response = watsonx_client().generate_text({"input": prompt})
    return {"fixed_code": response.get("generated_text", "No output")}