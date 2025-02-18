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
