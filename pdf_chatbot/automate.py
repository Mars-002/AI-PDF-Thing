import requests

# URL of the FastAPI application
BASE_URL = "http://127.0.0.1:8000"

def upload_pdf(file_path):
    url = f"{BASE_URL}/upload/"
    with open(file_path, "rb") as file:
        files = {'file': file}
        response = requests.post(url, files=files)
    if response.status_code == 200:
        return response.json()["text"]
    else:
        print("Failed to upload PDF:", response.text)
        return None

def ask_question(question, context):
    url = f"{BASE_URL}/ask/"
    payload = {"question": question, "context": context}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["answer"]
    else:
        print("Failed to get answer:", response.text)
        return None

def main():
    pdf_path = input("Enter the path to your PDF file: ")  # Get PDF file path from user
    question = input("Enter your question: ")  # Get question from user

    # Upload the PDF
    print("Uploading PDF...")
    context = upload_pdf(pdf_path)
    if context:
        print("PDF uploaded successfully.")
        print("Extracted text snippet:", context[:500])  # Print a snippet of the extracted text

        # Ask a question using the extracted context
        print("Asking question...")
        answer = ask_question(question, context)
        if answer:
            print("Answer:", answer)
        else:
            print("Failed to get an answer.")
    else:
        print("Failed to extract text from PDF.")

if __name__ == "__main__":
    main()
