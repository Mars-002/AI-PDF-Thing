from fastapi import APIRouter, File, UploadFile, HTTPException
from app.models import extract_text_from_pdf, answer_question

router = APIRouter()

@router.post("/upload_and_ask/")
async def upload_and_ask(file: UploadFile = File(...), question: str = None):
    try:
        # Read the PDF content
        content = await file.read()
        
        # Extract text from the PDF
        context = extract_text_from_pdf(content)
        
        if question:
            # Answer the question using the extracted context
            answer = answer_question(question, context)
            return {"context": context, "answer": answer}
        else:
            return {"context": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
