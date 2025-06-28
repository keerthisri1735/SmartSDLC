from fastapi import APIRouter, UploadFile, File, HTTPException
from app1.services.pdf_utils import extract_text_from_pdf

router = APIRouter()

@router.post("/upload")
async def classify(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Uploaded file must be a PDF.")

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    try:
        text = extract_text_from_pdf(content)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
