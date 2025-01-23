import streamlit as st
import pickle

# Judul aplikasi
st.title("Prediksi Biaya Asuransi")
st.write("Nama: [Nama Anda], NIM: [NIM Anda]")

# Load model yang telah disimpan
with open("model_uas.pkl", "rb") as file:
    model = pickle.load(file)

# Input dari pengguna
age = st.number_input("Usia", min_value=0, max_value=120, value=25)
sex = st.selectbox("Jenis Kelamin", ["male", "female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, value=25.0)
children = st.number_input("Jumlah Anak", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Apakah Merokok?", ["yes", "no"])

# Encode data input
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0

# Prediksi
if st.button("Submit"):
    # Membentuk input ke dalam format yang sesuai
    input_data = [[age, sex_encoded, bmi, children, smoker_encoded]]
    prediction = model.predict(input_data)  # Prediksi menggunakan model
    st.success(f"Prediksi Biaya Asuransi: ${prediction[0]:.2f}")
