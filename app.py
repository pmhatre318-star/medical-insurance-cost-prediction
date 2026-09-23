import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)

# =========================
# LOAD TRAINED MODEL
# =========================
model = joblib.load("insurance_model.pkl")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f4f7fb;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

.header {
    background-color: #173F5F;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.header h1 {
    margin: 0;
    font-size: 32px;
}

.header p {
    margin-top: 8px;
    font-size: 16px;
}

.section {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    margin-bottom: 20px;
}

.result {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #1B8A5A;
    text-align: center;
    margin-top: 20px;
}

.result-title {
    font-size: 18px;
    color: #666666;
}

.result-value {
    font-size: 38px;
    font-weight: bold;
    color: #1B8A5A;
}

.footer {
    text-align: center;
    color: #888888;
    font-size: 13px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header">
    <h1>🏥 Medical Insurance Cost Predictor</h1>
    <p>Machine Learning Based Insurance Cost Prediction System</p>
</div>
""", unsafe_allow_html=True)

# =========================
# DESCRIPTION
# =========================
st.write(
    "Enter the patient's information below to estimate the medical insurance cost."
)

# =========================
# PATIENT INFORMATION
# =========================
st.markdown("""
<div class="section">
<h3>👤 Patient Information</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25,
        step=1
    )

    bmi = st.number_input(
        "BMI",
        min_value=1.0,
        max_value=100.0,
        value=25.0,
        step=0.1
    )

    smoker = st.selectbox(
        "Smoker",
        ["No", "Yes"]
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    children = st.number_input(
        "Children",
        min_value=0,
        max_value=20,
        value=1,
        step=1
    )

    region = st.selectbox(
        "Region",
        [
            "Northeast",
            "Northwest",
            "Southeast",
            "Southwest"
        ]
    )

# =========================
# PREDICTION BUTTON
# =========================
st.write("")

predict_button = st.button(
    "🔮 Predict Insurance Cost",
    use_container_width=True
)

# =========================
# PREDICTION
# =========================
if predict_button:

    # Convert categorical values
    sex = 1 if gender == "Male" else 0

    smoker_value = 1 if smoker == "Yes" else 0

    region_dict = {
        "Northeast": 0,
        "Northwest": 1,
        "Southeast": 2,
        "Southwest": 3
    }

    region_value = region_dict[region]

    # Create DataFrame
    data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker_value],
        "region": [region_value]
    })

    # Make prediction
    prediction = model.predict(data)

    cost = prediction[0]

    # Display result
    st.markdown(f"""
    <div class="result">
        <div class="result-title">
            Estimated Insurance Cost
        </div>
        <div class="result-value">
            ₹ {cost:,.2f}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    Medical Insurance Cost Prediction using Machine Learning
</div>
""", unsafe_allow_html=True)