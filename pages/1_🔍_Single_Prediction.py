import streamlit as st
import pickle
import numpy as np

# ---------- LOAD MODEL ----------
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("🔍 Customer Risk Analyzer")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure", 0, 100, 12)
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)

with col2:
    total_charges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

payment = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer", "Credit card"
])

contract_map = {"Month-to-month":0, "One year":1, "Two year":2}
payment_map = {"Electronic check":0, "Mailed check":1, "Bank transfer":2, "Credit card":3}

if st.button("Analyze Customer"):

    if monthly_charges <= 0 or total_charges <= 0:
        st.warning("Charges must be greater than 0")
        st.stop()

    data = np.array([[tenure, monthly_charges, total_charges,
                      contract_map[contract], payment_map[payment]]])

    prob = model.predict_proba(data)[0][1]

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Churn Risk", f"{round(prob*100,2)}%")

    with col2:
        if prob > 0.6:
            st.error("High Risk Customer")
        else:
            st.success("Customer Likely to Stay")
