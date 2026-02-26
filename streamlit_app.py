import streamlit as st
from PIL import Image
import os

# 1. Page Configuration
st.set_page_config(page_title="Veritas Bank Analytics", layout="wide")

# 2. Sidebar Navigation & AI Chat Integration
with st.sidebar:
    # Logo Section
    logo_path = "banklogo.png" 
    if os.path.exists(logo_path):
        image = Image.open(logo_path)
        st.image(image)
    else:
        st.warning("Logo 'banklogo.png' not found.")

    st.title("Navigation")
    st.info("Use the report navigation at the bottom of the dashboard.")
    st.markdown("---")

# 3. Custom CSS (Untouched - keeping your specific Banner style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

    .block-container {
        padding-top: 4rem !important; 
    }

    .top-banner {
        background-color: #003049;
        padding-top: 20px;    
        padding-bottom: 20px; 
        border-radius: 15px;   
        text-align: center;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    
    .banner-title {
        color: #EAE2B7;
        font-family: 'DIN Condensed', 'DIN Alternate', 'Oswald', sans-serif;
        font-size: 120px; 
        font-weight: 900; 
        margin: 0;
        line-height: 0.9; 
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Top Banner (Full Width)
st.markdown('<div class="top-banner"><p class="banner-title">Veritas Bank Churn Risk Analysis</p></div>', unsafe_allow_html=True)

# 5. Dashboard (Full Width)
pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiOWEzMDI0NzctYzZiMC00Mjc4LWI5MzgtNDk3YmRiZTUxZmVjIiwidCI6IjhkMWE2OWVjLTAzYjUtNDM0NS1hZTIxLWRhZDExMmY1ZmI0ZiIsImMiOjN9"
st.components.v1.iframe(pbi_url, height=850)