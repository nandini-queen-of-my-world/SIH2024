import streamlit as st
import time
from twilio.rest import Client

def oil_spill_detection_page():
    st.title("Oil Spill Detection")

    st.image("0_0_0_img_01RNDdyOUhULo97s_SFr_cls_0.jpg", caption="Analyzing for oil spill...")

    with st.spinner("Detecting oil spill..."):
        time.sleep(7)  # Simulate detection time

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
        🚨 Alert!!!  Oil Spill is detected  🚨
    </div>
    """, unsafe_allow_html=True)

    # Send SMS notification after detection
    st.info("Sending notification to the higher authorities...")

    # Twilio credentials
    account_sid = 'AC44d2807d3a5918893592fdb967162bb9'  # Replace with your account SID
    auth_token = '4020cb0851d86d8449f696a08d6c0c4b'     # Replace with your auth token

    client = Client(account_sid, auth_token)

    try:
        # Send SMS using Twilio API
        message = client.messages.create(
            body="🚨 Alert: Oil spill has been detected! 🚨",
            from_='+18647272568',  # Your Twilio number
            to='+917569056212'      # Recipient number in correct format
        )

        st.success(f"Notification sent successfully: {message.sid}")

    except Exception as e:
        st.error(f"Failed to send notification: {str(e)}")  # Display the error message

if __name__ == '__main__':
    oil_spill_detection_page()
