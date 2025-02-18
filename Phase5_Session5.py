import streamlit as st
from google import genai

# Thêm thẳng API Key vào code
api_key = "AIzaSyBm2qwV2cZ5jN_31QWK-mGoJOgcAhoM4T0"  # Thay "your_api_key_here" bằng API key thật của bạn

# Khởi tạo client Gemini với API key
client = genai.Client(api_key=api_key)

# Hàm phân loại cảm xúc
def classify_sentiment(text):
    # Gửi yêu cầu đến Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Dùng mô hình Gemini
        contents=f"Classify the content of the email (spam/ham) in 1 word {text}",
    )
    
    # Trích xuất cảm xúc từ phản hồi
    sentiment = response.text.strip()
    return sentiment

# Giao diện người dùng Streamlit
st.title("Phân loại Email")
st.write("Nhập nội dung email")

# Tạo input để người dùng nhập văn bản
user_input = st.text_area("Nhập nội dung:")

# Nút để người dùng gửi đánh giá
if st.button("Phân loại email"):
    sentiment = classify_sentiment(user_input)
    st.write(f"Email dự đoán: {sentiment}")
