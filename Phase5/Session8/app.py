import openai
import streamlit as st

# Thay API Key thật của bạn vào đây
openai.api_key = "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"  # Thay bằng API Key thật

# Hàm gọi API OpenAI
def answers_questions(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that helps with business Q&A (answer only in 100 tokens)"},
                {"role": "user", "content": f"Answer the question: {text}"}
            ],
            max_tokens=200
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return answer
    except Exception as e:
        return f"Lỗi khi gọi API: {e}"

# Giao diện với Streamlit
st.title("ChatGPT Business Q&A")
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

