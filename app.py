import streamlit as st

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# ---------- SAFE MINIMAL STYLE ----------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("Customer Churn Dashboard")

st.write("Analyze and predict customer churn using AI")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🔍 Single Prediction</h3>
        <p>Analyze one customer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📊 Bulk Analysis</h3>
        <p>Analyze dataset</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info("Use sidebar to navigate →")