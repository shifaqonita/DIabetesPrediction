import pickle
import streamlit as st

diabetes_model = pickle.load(open('22611028_diabetes_model.sav', 'rb'))

st.markdown("<h1 style='text-align: center; color: #FF6347;'>Prediksi Diabetes</h1>", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #f0f8ff; padding: 10px; border-radius: 10px;'>
    <p style='text-align: center; font-size: 14px;'>Aplikasi ini akan memprediksi kemungkinan seseorang terkena diabetes berdasarkan beberapa parameter medis. Silakan masukkan data pada kolom di bawah untuk melakukan prediksi.</p>
    </div>
    """, unsafe_allow_html=True)

with st.form(key='prediction_form'):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Angka Kehamilan', min_value=0, max_value=20, step=1, format='%d')
        Glucose = st.number_input('Konsentrasi glukosa', min_value=0, max_value=300, step=1, format='%d')
        BloodPressure = st.number_input('Tekanan darah diastolik', min_value=0, max_value=200, step=1, format='%d')
        SkinThickness = st.number_input('Ketebalan lipatan kulit trisep', min_value=0, max_value=100, step=1, format='%d')

    with col2:
        Insulin = st.number_input('Insulin', min_value=0, max_value=1000, step=1, format='%d')
        BMI = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1, format='%.1f')
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, step=0.01, format='%.2f')
        Age = st.number_input('Usia', min_value=0, max_value=120, step=1, format='%d')

    submit_button = st.form_submit_button('Test Prediksi Diabetes', type='primary')

    if submit_button:
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        diab_prediction = diabetes_model.predict([inputs])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
            st.error(diab_diagnosis, icon="🚨")
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'
            st.success(diab_diagnosis, icon="✅")
