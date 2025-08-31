# ui.py
import streamlit as st

def render_title():
    st.markdown("""
        <h1 style='text-align: center; white-space: nowrap; overflow-x: auto; font-size: 2.2rem;'>
            🌿 GreenPrint AI: Carbon Footprint Detector
        </h1>
    """, unsafe_allow_html=True)


def user_input_form():
    with st.form("activity_form"):
        car_km = st.number_input("🚗 Car travel per week (km)", 0, 1000, 50)
        electricity = st.number_input("💡 Electricity usage per month (units)", 0, 1000, 200)
        meat = st.number_input("🍖 Meat meals per week", 0, 21, 7)
        flights = st.number_input("✈️ Flights per year", 0, 20, 1)
        submitted = st.form_submit_button("Calculate")
    return submitted, car_km, electricity, meat, flights
