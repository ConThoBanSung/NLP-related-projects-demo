import os
from google import genai
import streamlit as st

# Nhập API Key từ Google Gemini
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))  # Đảm bảo rằng bạn đã đặt API Key trong biến môi trường

# Hàm phân loại cảm xúc
def classify_sentiment(text):
    # Gửi yêu cầu đến Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Dùng mô hình Gemini
        contents=f"Classify the sentiment of the following review in one word: {text}",
    )
    
    # Trích xuất cảm xúc từ phản hồi
    sentiment = response.text.strip()
    return sentiment

# Giao diện người dùng Streamlit
st.title("Phân loại Cảm xúc Đánh giá")
st.write("Nhập một đánh giá sản phẩm và AI sẽ phân loại cảm xúc của nó.")

# Tạo input để người dùng nhập văn bản
user_input = st.text_area("Nhập đánh giá:", "The product is great! I really love it.")

# Nút để người dùng gửi đánh giá
if st.button("Phân loại cảm xúc"):
    sentiment = classify_sentiment(user_input)
    st.write(f"Cảm xúc dự đoán: {sentiment}")
