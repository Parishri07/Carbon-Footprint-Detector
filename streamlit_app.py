import streamlit as st
from config.emission_factors import EMISSION_FACTORS
from components.pie_chart import create_pie_chart
from model.predictor import predict_footprint
from utils.reducer import suggest_reduction
from style.custom_css import inject_custom_css

# Page configuration
st.set_page_config(page_title="GreenPrint AI 🌱", layout="centered")

# Inject custom CSS styles
inject_custom_css()

# App title
st.markdown("""
    <h1 style='text-align: center; white-space: nowrap; overflow-x: auto; font-size: 2.2rem;'>
        🌿 GreenPrint AI: Carbon Footprint Detector
    </h1>
""", unsafe_allow_html=True)

# User Input Form
with st.form("activity_form"):
    car_km = st.number_input("🚗 Car travel per week (km)", 0, 1000, 50)
    electricity = st.number_input("💡 Electricity usage per month (units)", 0, 1000, 200)
    meat = st.number_input("🍖 Meat meals per week", 0, 21, 7)
    flights = st.number_input("✈️ Flights per year", 0, 20, 1)

    submitted = st.form_submit_button("Calculate")

if submitted:
    user_input = {
        "car_km_per_week": car_km,
        "electricity_units_per_month": electricity,
        "meat_meals_per_week": meat,
        "flights_per_year": flights
    }

    result = predict_footprint(user_input)
    st.success(f"Estimated Annual Carbon Footprint: **{result:.2f} kg CO₂**")

    # Calculate breakdown per activity
    yearly_values = {
        "Car Travel": car_km * 52 * EMISSION_FACTORS["Car Travel"],
        "Electricity": electricity * 12 * EMISSION_FACTORS["Electricity"],
        "Meat Consumption": meat * 52 * EMISSION_FACTORS["Meat Consumption"],
        "Flights": flights * EMISSION_FACTORS["Flights"]
    }

    # Show pie chart
    st.markdown("### 🧾 Activity-wise Contribution to Your Footprint")
    st.plotly_chart(create_pie_chart(yearly_values), use_container_width=True)

    # Suggestions
    st.markdown("---")
    st.subheader("♻️ Suggestions to Reduce Your Footprint")
    for tip in suggest_reduction(user_input):
        st.markdown(f"- {tip}")

    st.markdown("---")
    st.markdown("<div style='text-align:center;'>Made with 💚 by Parishri</div>", unsafe_allow_html=True)
