from fastapi import APIRouter, UploadFile
from app1.services.pdf_utils import extract_text_from_pdf
from app1.services.watsonx import classify_sdlc

router = APIRouter()

@router.post("/upload")
async def classify(file: UploadFile):
    content = await file.read()
    text = extract_text_from_pdf(content)
    sentences = text.splitlines()
    result = classify_sdlc(sentences)
    return {"classified": result}