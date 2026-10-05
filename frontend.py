import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Sentiment Analyzer",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* Main page */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    /* Main container */
    .main {
        padding-top: 30px;
    }

    /* Header */
    .header {
        text-align: center;
        padding: 20px 10px 10px 10px;
    }

    .header-icon {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .header h1 {
        font-size: 42px;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 8px;
    }

    .header p {
        font-size: 17px;
        color: #64748b;
    }

    /* Card */
    .card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.08);
        margin-top: 20px;
        margin-bottom: 20px;
        color: #334155;
    }

    .card h3 {
        color: #1e293b;
    }

    .card p, .card b {
        color: #475569;
    }

    /* Label */
    .input-label {
        font-size: 18px;
        font-weight: 700;
        color: #334155;
        margin-bottom: 8px;
    }

    /* Analyze button */
    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        font-size: 17px;
        font-weight: 700;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
    }

    /* Result cards */
    .positive-result {
        background: #ecfdf5;
        border: 1px solid #86efac;
        padding: 22px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .negative-result {
        background: #fef2f2;
        border: 1px solid #fca5a5;
        padding: 22px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .result-sentiment {
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .positive-result .result-sentiment {
        color: #059669;
    }

    .negative-result .result-sentiment {
        color: #dc2626;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 30px;
        padding-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# FastAPI URL
# -----------------------------
FASTAPI_URL = "http://127.0.0.1:8000/predict"


# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="header">
    <h1>Sentiment Analyzer</h1>
    <p>
        Analyze the emotional tone of your text using our
        <b>Deep Learning Model</b>.
    </p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Main Card
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    '<div class="input-label">Enter your text</div>',
    unsafe_allow_html=True
)

text_input = st.text_area(
    "",
    placeholder="Example: I really love this product. It works perfectly!",
    height=150,
    label_visibility="collapsed"
)

st.write("")

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Sentiment"):

    if text_input.strip():

        with st.spinner("Analyzing your text..."):

            try:

                response = requests.post(
                    FASTAPI_URL,
                    json={"text": text_input},
                    timeout=10
                )

                if response.status_code == 200:

                    data = response.json()

                    sentiment = data.get("sentiment")
                    score = data.get("score", 0)

                    # -----------------------------
                    # Positive Result
                    # -----------------------------
                    if sentiment == "Positive":

                        st.markdown(f"""
                        <div class="positive-result">
                            <div class="result-sentiment">
                                Positive
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    # -----------------------------
                    # Negative Result
                    # -----------------------------
                    else:

                        st.markdown(f"""
                        <div class="negative-result">
                            <div class="result-sentiment">
                                Negative
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                else:

                    st.error(
                        f"API Error: {response.status_code} - "
                        f"{response.text}"
                    )

            except requests.exceptions.RequestException:

                st.error(
                    "Failed to connect to the backend. "
                    "Please make sure your FastAPI server is running."
                )

    else:

        st.warning("Please enter some text to analyze.")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Information Section
# -----------------------------
st.markdown("""
<div class="card">

<h3>How it works</h3>

<p>
The application sends your text to a FastAPI backend,
where the trained deep learning model analyzes the text
and predicts its sentiment.
</p>

<div style="
display:flex;
justify-content:space-between;
text-align:center;
margin-top:20px;
">

<div>
    <b>1. Enter Text</b>
</div>

<div>
    <b>2. Send to API</b>
</div>

<div>
    <b>3. Model Predicts</b>
</div>

<div>
    <b>4. View Result</b>
</div>

</div>

</div>
""", unsafe_allow_html=True)


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    Sentiment Analyzer • FastAPI + Streamlit + Deep Learning
</div>
""", unsafe_allow_html=True)
