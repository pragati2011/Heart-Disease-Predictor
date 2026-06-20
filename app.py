import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: #ff4b4b;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #ff4b2b, #ff416c);
}

.result-card {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Load files
model = joblib.load("knn_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# Header
st.markdown('<p class="title">❤️ Heart Disease Prediction System</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Heart disease risk assessment</p>',
    unsafe_allow_html=True
)

st.divider()

# Sidebar
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/833/833472.png",
        width=120
    )

    st.header("ℹ️ About")
    st.write("""
    This application predicts the likelihood of heart disease
    using a trained KNN Machine Learning model.
    """)

    st.success("Model: K-Nearest Neighbors")
    st.info("Developed by Pragati ❤️")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Information")

    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        80, 200, 120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        100, 600, 200
    )

with col2:
    st.subheader("🩺 Medical Information")

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

    max_hr = st.slider(
        "Maximum Heart Rate",
        60, 220, 150
    )

    exercise_angina = st.selectbox(
        "Exercise-Induced Angina",
        ["Y", "N"]
    )

    oldpeak = st.slider(
        "Oldpeak",
        0.0, 6.0, 1.0
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"]
    )

st.divider()

# Predict Button
if st.button("🔍 Predict Heart Disease Risk"):

    with st.spinner("Analyzing health data..."):

        raw_input = {
            'Age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain: 1,
            'RestingECG_' + resting_ecg: 1,
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }

        input_df = pd.DataFrame([raw_input])

        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]

        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        st.balloons()

        if prediction == 1:

            st.markdown("""
            <div class="result-card"
            style="background-color:#ffe5e5;color:#d90429;">
            ⚠️ HIGH RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)

            st.error(
                "Please consult a healthcare professional for further evaluation."
            )

        else:

            st.markdown("""
            <div class="result-card"
            style="background-color:#d8f3dc;color:#2d6a4f;">
            ✅ LOW RISK OF HEART DISEASE
            </div>
            """, unsafe_allow_html=True)

            st.success(
                "Your results indicate a lower likelihood of heart disease."
            )

        st.subheader("📊 Health Summary")

        m1, m2, m3 = st.columns(3)

        m1.metric("Age", age)
        m2.metric("Cholesterol", cholesterol)
        m3.metric("Max HR", max_hr)