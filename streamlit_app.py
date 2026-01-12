import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    return joblib.load("churn.joblib")

model = load_model()

st.title("Subscription-Based Customer Churn Prediction")
st.write("Please fill in the customer details below to predict churn.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Select Age", 18, 65, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.slider("Tenure", 1, 60, 30)
    usage_frequency = st.slider("Frequency of Usage", 1, 30, 15)
    calls = st.slider("Support Calls", 0, 10, 5)

with col2:
    payment_delay = st.slider("Payment Delay", 0, 30, 15)
    subs = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
    contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
    spent = st.number_input("Total Spend", 100, 10000, 500)
    last_interaction = st.slider("Last Interaction", 1, 30, 15)

gender = 1 if gender == "Male" else 0

s_b = 1 if subs == "Basic" else 0
s_s = 1 if subs == "Standard" else 0
s_p = 1 if subs == "Premium" else 0

c_m = 1 if contract == "Monthly" else 0
c_q = 1 if contract == "Quarterly" else 0
c_a = 1 if contract == "Annual" else 0

test_df = pd.DataFrame(
    [[
        age,
        gender,
        tenure,
        usage_frequency,
        calls,
        payment_delay,
        spent,
        last_interaction,
        s_b,
        s_p,
        s_s,
        c_a,
        c_m,
        c_q
    ]],
    columns=model.feature_names_in_
)

st.write("You have entered the following details:")
st.write(test_df)

if st.button("Predict"):
    pred = model.predict(test_df)[0]
    prob = model.predict_proba(test_df)[0][1]
    if pred == 1:
        st.error(f"Customer is likely to churn")
    else:
        st.success(f"Customer is not likely to churn")