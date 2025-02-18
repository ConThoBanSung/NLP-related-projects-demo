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
            contents=f"Imagine that you are a machine that summarize paragraph about finance. Summarize the question: {text}(only summarize about financial, if not return I only summarize financial docs)",  # Truyền câu hỏi vào
        )
        answer = response.text.strip()
        return answer
    except Exception as e:
        return f"Lỗi khi gọi API: {e}"

# Giao diện với Streamlit
st.title("ChatAI Summarize")
st.write("Nhập văn bản cần rút gọn:")

# Ô nhập câu hỏi
question = st.text_input("Văn bản:")

# Nút gửi yêu cầu
if st.button("Gửi"):
    if question:
        answer = answers_questions(question)
        st.subheader("Văn bản đã rút gọn:")
        st.write(answer)
    else:
        st.warning("Vui lòng nhập văn bản!")
