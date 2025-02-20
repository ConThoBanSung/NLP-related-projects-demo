import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Trực quan hóa dữ liệu")

# Tải dữ liệu lên
uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 📌 Dữ liệu tải lên:")
    st.write(df.head())

    # Mô tả dữ liệu
    st.write("### 📊 Mô tả dữ liệu:")
    st.write(df.describe(include='all'))

    # Chọn cột để vẽ biểu đồ
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    if numeric_columns:
        selected_column = st.selectbox("Chọn cột số để vẽ histogram:", numeric_columns)
        
        # Vẽ histogram
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        ax.set_title(f"Histogram của {selected_column}")
        st.pyplot(fig)

        # Vẽ boxplot
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_column], ax=ax)
        ax.set_title(f"Boxplot của {selected_column}")
        st.pyplot(fig)
    
        # Hiển thị ma trận tương quan
        st.write("### 🔗 Ma trận tương quan giữa các cột số:")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
        st.pyplot(fig)
    else:
        st.write("⚠️ Không có cột số trong dữ liệu để hiển thị biểu đồ.")
    
    if categorical_columns:
        selected_cat_column = st.selectbox("Chọn cột phân loại để vẽ biểu đồ:", categorical_columns)
        
        # Vẽ bar chart
        fig, ax = plt.subplots()
        df[selected_cat_column].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f"Biểu đồ cột của {selected_cat_column}")
        st.pyplot(fig)
        
        # Vẽ pie chart
        fig, ax = plt.subplots()
        df[selected_cat_column].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_title(f"Biểu đồ tròn của {selected_cat_column}")
        ax.set_ylabel('')
        st.pyplot(fig)
    else:
        st.write("⚠️ Không có cột phân loại trong dữ liệu để hiển thị biểu đồ.")
