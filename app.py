import streamlit as st
from filter_page import filter_ais_data_page
from monitor_page import monitor_anomalies_page
from sms_page import send_sms_page
from oil_spill_page import oil_spill_detection_page

def main():
    st.sidebar.title("Marine Vision Navigation")
    page = st.sidebar.radio("Go to", ("AIS Data Filter", "Monitor Anomalies", "Send Notifications", "Oil Spill Detection"))

    if page == "AIS Data Filter":
        filter_ais_data_page()
    elif page == "Monitor Anomalies":
        monitor_anomalies_page()
    elif page == "Send Notifications":
        send_sms_page()
    elif page == "Oil Spill Detection":
        oil_spill_detection_page()

if __name__ == '__main__':
    main()
