import os
from google import genai
import streamlit as st

# Nhập API Key từ Google Gemini
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))  # Đảm bảo rằng bạn đã thiết lập API Key trong biến môi trường

# Hàm gọi API Gemini
def answers_questions(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Dùng mô hình Gemini
            contents=f"Imagine that you are technical supprter in business. Answer the question: {text}",  # Truyền câu hỏi vào
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
