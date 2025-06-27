from fastapi import APIRouter
from app1.models.request_models import TestCaseRequest
from app1.services.watsonx import watsonx_client

router = APIRouter()

@router.post("/generate_tests")
async def generate_tests(req: TestCaseRequest):
    prompt = f"Write test cases using pytest for the following code:\n{req.code}"
    response = watsonx_client().generate_text({"input": prompt})
    return {"test_cases": response.get("generated_text", "No output")}