from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_pdf():
    with open("sample.pdf", "rb") as f:
        response = client.post("/upload/", files={"file": ("filename", f, "application/pdf")})
    assert response.status_code == 200
    assert "text" in response.json()

def test_ask_question():
    response = client.post("/ask/", json={"question": "What is the capital of France?", "context": "Paris is the capital of France."})
    assert response.status_code == 200
    assert response.json()["answer"] == "Paris"