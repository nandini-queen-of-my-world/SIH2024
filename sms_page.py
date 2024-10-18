import streamlit as st
from twilio.rest import Client

def send_sms_page():
    st.title("Send Notifications via SMS")

    phone_number = st.text_input("Enter phone number (with country code)", placeholder="+911234567890")
    message_text = st.text_area("Enter message to send", "An anomaly has been detected!")

    if st.button("Send SMS"):
        if phone_number and message_text:
            try:
                # Initialize Twilio client (Replace with your Twilio credentials)
                account_sid = 'AC44d2807d3a5918893592fdb967162bb9'
                auth_token = '4020cb0851d86d8449f696a08d6c0c4b'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=message_text,
                    from_='+18647272568',  # Your Twilio number
                    to=phone_number
                )
                st.success(f"Message sent to {phone_number}!")
            except Exception as e:
                st.error(f"Failed to send message: {e}")
        else:
            st.error("Please enter a valid phone number and message.")
