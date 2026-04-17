import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# ---------- LOAD MODEL ----------
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("📊 Business Analytics")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Preview")
    st.dataframe(df.head())

    # preprocessing
    df["Contract"] = df["Contract"].map({
        "Month-to-month":0,"One year":1,"Two year":2
    })

    df["PaymentMethod"] = df["PaymentMethod"].map({
        "Electronic check":0,"Mailed check":1,
        "Bank transfer (automatic)":2,"Credit card (automatic)":3
    })

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
    df = df.dropna()

    features = df[["tenure","MonthlyCharges","TotalCharges","Contract","PaymentMethod"]]

    df["Churn_Probability"] = model.predict_proba(features)[:,1]

    # ---------- METRICS ----------
    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    high = (df["Churn_Probability"] > 0.6).sum()
    medium = ((df["Churn_Probability"] > 0.3) & (df["Churn_Probability"] <= 0.6)).sum()
    low = (df["Churn_Probability"] <= 0.3).sum()

    col1.metric("High Risk", high)
    col2.metric("Medium Risk", medium)
    col3.metric("Low Risk", low)

    # ---------- PIE CHART (FIXED SIZE) ----------
    st.subheader("Distribution")

    df["Risk"] = pd.cut(df["Churn_Probability"], bins=[0,0.3,0.6,1], labels=["Low","Medium","High"])
    counts = df["Risk"].value_counts()

    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")

    st.pyplot(fig)

    # ---------- TABLE ----------
    st.subheader("High Risk Customers")
    st.dataframe(df[df["Churn_Probability"] > 0.6].head(10))
