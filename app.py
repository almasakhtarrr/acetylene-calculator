import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Acetylene Calculator", layout="centered")

st.title("⚗️ Acetylene Gas Calculator (Advanced)")

st.markdown("**Reaction:** CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂")
st.markdown("1 mole CaC₂ → 1 mole C₂H₂")

# ---- Inputs ----
st.header("🔢 Input Parameters")

mass = st.number_input("Calcium Carbide (grams)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", value=25.0)
pressure = st.number_input("Pressure (atm)", value=1.0)

# Convert temperature to Kelvin
T = temperature + 273.15

# Constants
R = 0.0821  # L·atm/mol·K
molar_mass = 64  # g/mol

# ---- Calculation ----
if st.button("Calculate"):

    if mass > 0 and pressure > 0:
        moles = mass / molar_mass
        volume = (moles * R * T) / pressure

        st.success(f"Gas Produced: {volume:.2f} Liters")

        # ---- Graph ----
        st.subheader("📊 Volume vs Temperature")

        temps = np.linspace(0, 100, 50)
        volumes = (moles * R * (temps + 273.15)) / pressure

        fig, ax = plt.subplots()
        ax.plot(temps, volumes)
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Volume (Liters)")
        ax.set_title("Volume vs Temperature")

        st.pyplot(fig)

    else:
        st.warning("Enter valid values")

# ---- Safety Panel ----
st.header("⚠️ Safety Information")

st.info("""
- Acetylene (C₂H₂) is highly flammable.
- Avoid any ignition sources (spark, flame).
- Do not confine gas in closed rigid containers.
- Perform experiments only under proper supervision.
- This app is for theoretical/educational use only.
""")
