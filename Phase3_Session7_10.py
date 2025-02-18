import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Cấu hình API Gemini
genai.configure(api_key="AIzaSyBm2qwV2cZ5jN_31QWK-mGoJOgcAhoM4T0")  # Thay bằng API thực của bạn

# Giao diện Streamlit
st.title("AI dự đoán số thông qua ảnh chữ viết tay")
st.write("Tải ảnh lên và nhập câu hỏi để AI xử lý!")

# Upload ảnh từ người dùng
uploaded_file = st.file_uploader("Chọn một hình ảnh", type=["png", "jpg", "jpeg"])

# Nhập câu hỏi
message = st.text_area("Nhập nội dung bạn muốn hỏi", "")

# Nút gửi yêu cầu
if st.button("Gửi yêu cầu"):
    if uploaded_file and message:
        # Mở ảnh bằng PIL
        image = Image.open(uploaded_file)
        
        # Hiển thị ảnh lên Streamlit (sử dụng use_container_width thay vì use_column_width)
        st.image(image, caption="Hình ảnh đã chọn", use_container_width=True)

        # Gửi dữ liệu lên Gemini
        model = genai.GenerativeModel("gemini-2.0-flash")  
        response = model.generate_content([image, message])  # Truyền thẳng ảnh PIL
        
        # Hiển thị kết quả
        st.subheader("Kết quả từ Gemini:")
        st.write(response.text)

        # Tạo file text để tải về
        output_text = response.text
        output_filename = "gemini_response.txt"
        output_bytes = io.BytesIO(output_text.encode("utf-8"))

        # Nút tải xuống kết quả
        st.download_button(
            label="📥 Tải xuống câu trả lời",
            data=output_bytes,
            file_name=output_filename,
            mime="text/plain"
        )
    else:
        st.warning("Vui lòng tải lên ảnh và nhập câu hỏi trước khi gửi!")
