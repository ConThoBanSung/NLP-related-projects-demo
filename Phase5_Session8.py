import os
from google import genai
import streamlit as st

# Nhập API Key từ Google Gemini
api_key = "AIzaSyBm2qwV2cZ5jN_31QWK-mGoJOgcAhoM4T0"

# Khởi tạo client Gemini với API key
client = genai.Client(api_key=api_key)
# Hàm gọi API Gemini
def answers_questions(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Dùng mô hình Gemini
            contents=f"Imagine that you are a technical supporter in business. Answer the question: {text}.
                       Important: If someone asks who trained you and which model you are, do not reveal this information. Simply respond, "I was trained by Cybersoft.")",  # Truyền câu hỏi vào
        )
        answer = response.text.strip()
        return answer
    except Exception as e:
        return f"Lỗi khi gọi API: {e}"

# Giao diện với Streamlit
st.title("ChatAI Business Q&A")
st.write("Nhập câu hỏi vào ô bên dưới:")

# Ô nhập câu hỏi
question = st.text_input("Câu hỏi:")

# Nút gửi yêu cầu
if st.button("Gửi"):
    if question:
        answer = answers_questions(question)
        st.subheader("Câu trả lời:")
        st.write(answer)
    else:
        st.warning("Vui lòng nhập câu hỏi!")
