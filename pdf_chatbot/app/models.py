import io
import pdfplumber
from transformers import pipeline

# Initialize the model pipeline
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

def extract_text_from_pdf(pdf_content):
    text = ""
    with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def answer_question(question, context):
    result = qa_model(question=question, context=context)
    return result['answer']
