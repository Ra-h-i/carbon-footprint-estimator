import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EcoTrack AI | Carbon Estimator",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR BEAUTIFUL UI ---
custom_css = """
<style>
    /* Main Background & Text Color */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Header Card Styling */
    .header-card {
        background: linear-gradient(135deg, #1b4332 0%, #081c15 100%);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #2d6a4f;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }
    .header-title {
        color: #52b788;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #b7e4c7;
        font-size: 1.05rem;
    }

    /* Output Metric Card */
    .metric-box {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        transition: transform 0.2s ease-in-out;
    }
    .metric-box:hover {
        transform: translateY(-2px);
        border-color: #52b788;
    }
    .metric-val {
        font-size: 2.6rem;
        font-weight: 800;
        color: #74c69d;
    }
    .metric-lbl {
        font-size: 0.95rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Custom Recommendation Box */
    .rec-card {
        background: #162117;
        border-left: 4px solid #52b788;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- LOAD TRAINED ML MODEL ---
@st.cache_resource
def load_model():
    return joblib.load('carbon_model.pkl')

model = load_model()

# --- HEADER SECTION ---
st.markdown("""
<div class="header-card">
    <div class="header-title">🌱 EcoTrack AI</div>
    <div class="header-subtitle">Machine Learning Powered Personal & Campus Carbon Footprint Estimator</div>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR INPUTS ---
st.sidebar.markdown("<h2 style='color: #74c69d;'>📋 Usage Logs</h2>", unsafe_allow_html=True)
st.sidebar.markdown("Adjust your monthly activity metrics below:")

electricity = st.sidebar.number_input("⚡ Electricity (kWh):", min_value=0.0, value=150.0, step=10.0)
car = st.sidebar.number_input("🚗 Car Distance (km):", min_value=0.0, value=200.0, step=10.0)
transit = st.sidebar.number_input("🚌 Public Transit (km):", min_value=0.0, value=100.0, step=10.0)
devices = st.sidebar.slider("💻 Screen Time (Hrs/Day):", min_value=0.0, max_value=24.0, value=6.0)
waste = st.sidebar.number_input("🗑️ Waste Generated (kg):", min_value=0.0, value=15.0, step=1.0)

# --- ML PREDICTION ---
input_data = pd.DataFrame([[electricity, car, transit, devices, waste]], 
                          columns=['electricity_kwh', 'car_km', 'public_transit_km', 'device_hours_daily', 'waste_kg'])

predicted_co2 = model.predict(input_data)[0]

# --- MAIN DASHBOARD LAYOUT ---
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("<h3 style='color: #d8f3dc;'>📊 Impact Summary</h3>", unsafe_allow_html=True)
    
    # Styled Output Metric
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-lbl">Predicted Monthly Emission</div>
        <div class="metric-val">{predicted_co2:.1f} <span style="font-size: 1.2rem;">kg CO₂e</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Target Status Banner
    benchmark = 180.0
    if predicted_co2 <= benchmark:
        st.success("🟢 **Sustainable Level:** Your footprint is within eco-friendly target standards!")
    elif predicted_co2 <= benchmark * 1.5:
        st.warning("🟡 **Moderate Impact:** Slightly above recommended target limits.")
    else:
        st.error("🔴 **High Impact:** Urgent energy reduction action recommended.")

with col2:
    st.markdown("<h3 style='color: #d8f3dc;'>🔍 Emissions Breakdown</h3>", unsafe_allow_html=True)
    
    breakdown_data = pd.DataFrame({
        'Category': ['Electricity', 'Car Travel', 'Public Transit', 'Devices', 'Waste'],
        'CO2_kg': [
            electricity * 0.85,
            car * 0.18,
            transit * 0.05,
            devices * 30 * 0.03,
            waste * 1.2
        ]
    })
    
    # Donut Chart with matching color palette
    fig = px.pie(
        breakdown_data, 
        values='CO2_kg', 
        names='Category', 
        hole=0.55,
        color_discrete_sequence=['#2d6a4f', '#40916c', '#52b788', '#74c69d', '#b7e4c7']
    )
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0', size=13),
        showlegend=True,
        legend=dict(orientation="h", y=-0.1)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr style='border: 1px solid #30363d;'>", unsafe_allow_html=True)

# --- AI RECOMMENDATIONS ENGINE ---
st.markdown("<h3 style='color: #d8f3dc;'>💡 Actionable AI Recommendations</h3>", unsafe_allow_html=True)

recs = []
if electricity * 0.85 > 80:
    recs.append("⚡ **Energy Optimization:** Switch to high-efficiency LED lights and unplug idle appliances.")
if car * 0.18 > 40:
    recs.append("🚗 **Mobility Shift:** Try carpooling or substituting 2 short car trips per week with transit or cycling.")
if devices * 30 * 0.03 > 10:
    recs.append("💻 **Device Efficiency:** Enable automatic sleep and low-power modes during non-active hours.")
if waste * 1.2 > 15:
    recs.append("♻️ **Waste Management:** Practice dry/wet waste segregation and switch to reusable containers.")

if recs:
    for r in recs:
        st.markdown(f'<div class="rec-card">{r}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="rec-card">🎉 Outstanding habits! Your consumption profile is highly sustainable.</div>', unsafe_allow_html=True)