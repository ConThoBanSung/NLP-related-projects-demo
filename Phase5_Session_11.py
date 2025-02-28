import os
import streamlit as st
from google import genai
from PyPDF2 import PdfReader
from docx import Document

# Nhập API Key từ Google Gemini
api_key = "AIzaSyBm2qwV2cZ5jN_31QWK-mGoJOgcAhoM4T0"  # Thay bằng API Key của bạn

# Khởi tạo client Gemini với API key
client = genai.Client(api_key=api_key)

# Hàm đọc nội dung từ file
def read_file(file):
    ext = file.name.split(".")[-1].lower()
    if ext == "txt":
        return file.read().decode("utf-8")
    elif ext == "pdf":
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif ext == "docx":
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

# Hàm gọi API Gemini
def answer_question_with_docs(question, docs_content):
    try:
        prompt = f"Here are some reference documents:\n\n{docs_content}\n\nNow, answer this question: {question}, (Notice that when someone asked you train by who and which model you are, you have to not tell you train by who and which company, just answer you train by Cybersoft)"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Lỗi khi gọi API: {e}"

# Giao diện với Streamlit
st.title("AI Customer Support Chatbot")
st.write("Tải lên tài liệu và đặt câu hỏi")

# Upload nhiều file
uploaded_files = st.file_uploader("Tải lên tệp tin (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"], accept_multiple_files=True)

# Ô nhập câu hỏi
question = st.text_input("Nhập câu hỏi:")

# Xử lý tài liệu
docs_content = ""
if uploaded_files:
    for file in uploaded_files:
        docs_content += read_file(file) + "\n\n"

# Nút gửi yêu cầu
if st.button("Gửi"):
    if question:
        answer = answer_question_with_docs(question, docs_content)
        st.subheader("Câu Trả Lời:")
        st.write(answer)
    else:
        st.warning("Vui lòng nhập câu hỏi!")

