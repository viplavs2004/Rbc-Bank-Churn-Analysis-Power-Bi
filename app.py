import streamlit as st
import pandas as pd
import tensorflow as tf
import pickle

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Customer Churn Analysis", layout="wide")

# ----------------- LOAD MODEL & OBJECTS -----------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model.h5')

model = load_model()

@st.cache_resource
def load_objects():
    with open('label_encoder_gender.pkl', 'rb') as f:
        label_encoder_gender = pickle.load(f)
    with open('onehot_encoder_geo.pkl', 'rb') as f:
        onehot_encoder_geo = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return label_encoder_gender, onehot_encoder_geo, scaler

label_encoder_gender, onehot_encoder_geo, scaler = load_objects()

# ----------------- COMPACT CSS -----------------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 4rem;
        padding-bottom: 0.5rem;
    }
    .title {
        font-size: 26px;
        text-align: center;
        font-weight: bold;
        color: white;
    }
    .subtitle {
        text-align: center;
        font-size: 14px;
        color: white;
        margin-bottom: 10px;
    }
    .header-bg {
        background-color: #0d1b2a;
        padding: 10px;
        border-radius: 5px;
    }
    .result-box {
        background-color: #2E86C1;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #dcdcdc;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        margin-top: 5px;
        color: white;
    }
    .stProgress > div > div > div {
        background-color: #2E86C1;
    }
    /* Extra spacing between widgets */
    .stSelectbox, .stNumberInput, .stSlider {
        margin-bottom: 25px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- HEADER -----------------
st.markdown(
    '<div class="header-bg">'
    '<div class="title">Customer Churn Analysis</div>'
    '<div class="subtitle">Evaluate churn risk and gain actionable insights</div>'
    '</div>',
    unsafe_allow_html=True
)

# ----------------- INPUT SECTION (NO BUTTON) -----------------
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
    gender = st.selectbox('Gender', label_encoder_gender.classes_)
with c2:
    age = st.slider('Age', 18, 92, 30)
    balance = st.number_input('Balance', min_value=0.0, step=1000.0)
with c3:
    credit_score = st.number_input('Credit Score', min_value=0)
    estimated_salary = st.number_input('Estimated Salary', min_value=0.0, step=1000.0)
with c4:
    tenure = st.slider('Tenure', 0, 10, 5)
    num_of_products = st.slider('Products', 1, 4, 1)
with c5:
    has_cr_card = st.selectbox('Has Card', [0, 1])
    is_active_member = st.selectbox('Active Member', [0, 1])

# ----------------- PROCESS PREDICTION (RUNS INSTANTLY) -----------------
input_df = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(
    geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography'])
)

input_df_final = pd.concat([input_df, geo_encoded_df], axis=1)
input_df_final = input_df_final[scaler.feature_names_in_]
input_scaled = scaler.transform(input_df_final)

prediction_proba = model.predict(input_scaled, verbose=0)[0][0]

# ----------------- OUTPUT -----------------
st.markdown(f'<div class="result-box">Churn Probability: {prediction_proba:.2%}</div>', unsafe_allow_html=True)
st.progress(float(prediction_proba))

if prediction_proba > 0.5:
    st.success("Low Risk: Unlikely to churn.")
else:
    st.error("High Risk: Likely to churn.")
