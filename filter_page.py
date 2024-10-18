import streamlit as st
import pandas as pd

def filter_ais_data(input_csv, output_csv, imo_number):
    try:
        ais_data = pd.read_csv(input_csv)
    except Exception as e:
        st.error(f"Error reading the input file: {e}")
        return None
    
    filtered_data = ais_data[ais_data['IMO'].astype(str) == str(imo_number)]
    if filtered_data.empty:
        st.warning(f"No data found for IMO number {imo_number}.")
        return None
    filtered_data.to_csv(output_csv, index=False)
    return filtered_data

def filter_ais_data_page():
    st.title("🚢 Marine Vision - AIS Data Filter")
    st.markdown("Enter the IMO number for tracking the AIS data.")
    
    imo_number = st.text_input("Enter Vessel IMO Number:", placeholder="e.g., IMO9704697")
    submit_button = st.button("Filter Data")

    input_csv_file = r'AIS_2020_04_20.csv'
    output_csv_file = 'filtered_AIS_2020_04_20.csv'
    
    if submit_button and imo_number:
        filtered_data = filter_ais_data(input_csv_file, output_csv_file, imo_number)
        if filtered_data is not None:
            st.success(f"Data filtered successfully for IMO number {imo_number}!")
            st.markdown(f"[Download the filtered data](./{output_csv_file})", unsafe_allow_html=True)
            st.write(filtered_data)
