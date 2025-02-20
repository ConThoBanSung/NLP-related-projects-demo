import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_model(model_path='student_score_model.pkl'):
    """Load mô hình đã lưu"""
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    """Đánh giá mô hình trên dữ liệu test"""
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return mae, mse, rmse, r2

def main():
    st.title("Dự đoán và Đánh giá điểm số học sinh")
    model = load_model()
    
    columns = [
        'Hours_Studied',       # Số giờ học
        'Sleep_Hours',         # Số giờ ngủ trung bình
        'Extracurriculars',    # Hoạt động ngoại khóa (số lượng)
        'Health_Index',        # Chỉ số sức khỏe (từ 1-10)
        'Parental_Involvement',# Sự hỗ trợ của phụ huynh (từ 1-10)
        'Tutoring_Hours',      # Số giờ học thêm
        'Internet_Usage',      # Số giờ sử dụng internet
        'Self_Study',          # Số giờ tự học
        'Attendance',          # Tỷ lệ đi học (%)
        'Motivation_Level'     # Mức độ động lực học tập (từ 1-10)
    ]
    
    st.subheader("Nhập dữ liệu đầu vào:")
    user_data = [st.number_input(col, min_value=0.0, step=0.1) for col in columns]
    
    if st.button("Dự đoán"):
        user_input = np.array(user_data).reshape(1, -1)
        predicted_grade = model.predict(user_input)[0]
        st.success(f"Dự đoán điểm số của học sinh: {predicted_grade:.2f}")
    
    st.subheader("Tải lên dataset để đánh giá mô hình")
    uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Dữ liệu mẫu:")
        st.write(data.head())
        
        if 'Grades' in data.columns:
            X_test = data[columns]
            y_test = data['Grades']
            mae, mse, rmse, r2 = evaluate_model(model, X_test, y_test)
            
            st.subheader("Đánh giá mô hình:")
            st.write(f"MAE: {mae:.2f}")
            st.write(f"MSE: {mse:.2f}")
            st.write(f"RMSE: {rmse:.2f}")
            st.write(f"R2 Score: {r2:.2f}")
        else:
            st.error("Dataset không chứa cột 'Grades'. Hãy đảm bảo dữ liệu đầu vào đúng định dạng.")

if __name__ == "__main__":
    main()
