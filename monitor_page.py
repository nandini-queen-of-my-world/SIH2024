import streamlit as st
import time

def monitor_anomalies_page():
    st.title("Monitoring for Anomalies")
    uploaded_file = st.file_uploader("Upload filtered AIS data CSV", type="csv")
    
    if uploaded_file:
        st.info("Analyzing data for anomalies... This might take a moment.")
        with st.spinner("Monitoring anomalies..."):
            time.sleep(5)  # Simulate processing time
        st.markdown("""
    <div style="
        padding: 20px;
        background-color: #ffcccb;
        color: red;
        border: 2px solid red;
        border-radius: 10px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        ">
        🚨 Anomalies detected !!!!! 🚨
    </div>
""", unsafe_allow_html=True)
        # Display progress bar for illustration
        progress_bar = st.progress(0)
        for perc in range(100):
            time.sleep(0.02)
            progress_bar.progress(perc + 1)
