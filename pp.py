import streamlit as st
from decimal import Decimal, ROUND_HALF_UP

# Page Config
st.set_page_config(page_title="Purchasing Power Calculator", page_icon="💰")

# Custom Styling for Banking Theme
st.markdown("""
    <style>
    .main {
        background-color: #F0F4F7;
    }
    .stButton>button {
        width: 100%;
        background-color: #0D2137;
        color: white;
        font-weight: bold;
        height: 3em;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FFD700;
        color: #0D2137;
    }
    .result-box {
        background-color: #0D2137;
        color: #FFD700;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #FFD700;
        margin-top: 20px;
    }
    .dev-text {
        color: #0D2137;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<p class='dev-text'>Developed by</p>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #0D2137;'>SHAMSUDEEN ABDULLA</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>INFLATION IMPACT CALCULATOR</h3>", unsafe_allow_html=True)
st.divider()

# Input Section
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Current Cash Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)
    years = st.number_input("Number of Years", min_value=1, value=20, step=1)

with col2:
    inflation_rate = st.number_input("Annual Inflation Rate (%)", min_value=0.0, value=6.0, step=0.1)

# Calculate Button
st.markdown("<br>", unsafe_allow_html=True)
calculate_btn = st.button("CALCULATE REAL VALUE")

if calculate_btn:
    # Calculation Logic
    p = Decimal(str(amount))
    r = Decimal(str(inflation_rate)) / 100
    n = int(years)

    # Formula: Purchasing Power = P / (1 + r)^n
    val = p / ((1 + r) ** n)
    res = val.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Word formatting for Lakhs/Crores
    word_res = ""
    if res >= 10000000:
        word_res = f"≈ {float(res)/10000000:.2f} Crore"
    elif res >= 100000:
        word_res = f"≈ {float(res)/100000:.2f} Lakh"

    # Result Display
    st.markdown(f"""
        <div class="result-box">
            <p style="color: #BDC3C7; margin-bottom: 5px; font-weight: bold;">REAL VALUE IN {n} YEARS</p>
            <h1 style="color: #FFD700; margin: 0;">₹ {res:,.2f}</h1>
            <h3 style="color: #FFFFFF; margin-top: 5px;">{word_res}</h3>
        </div>
        """, unsafe_allow_html=True)

    # Summary Message
    st.info(f"Summary: Today's ₹{amount:,.0f} will have the same purchasing power as ₹{res:,.2f} in {n} years due to inflation.")
else:
    st.write("താങ്കളുടെ പണത്തിന്റെ ഭാവി മൂല്യം അറിയാൻ Calculate ബട്ടൺ അമർത്തുക.")

# Footer/Book Reference
st.markdown("---")
st.caption("പണപ്പെരുപ്പത്തെ മറികടക്കാൻ കൃത്യമായ നിക്ഷേപം ശീലമാക്കൂ.")
