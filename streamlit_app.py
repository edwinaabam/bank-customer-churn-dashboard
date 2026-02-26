import streamlit as st
from PIL import Image
import os

# 1. Page Configuration
st.set_page_config(page_title="Veritas Bank Analytics", layout="wide")

# 2. Sidebar Navigation with Local Logo
with st.sidebar:
    # Pointing to the image in the root directory
    logo_path = "banklogo.png" 
    
    if os.path.exists(logo_path):
        image = Image.open(logo_path)
        st.image(image, use_container_width=True)
    else:
        st.warning("Logo file 'banklogo.png' not found in root directory.")

    st.title("Navigation")
    st.markdown("---")
    st.info("Use the navigation arrows at the bottom of the dashboard to switch between report pages.")

# 3. Custom CSS for the Top Banner (Navy Blue & Vanilla)
st.markdown("""
    <style>
    .top-banner {
        background-color: #003049; /* Navy Blue */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        border: 2px solid #EAE2B7; /* Thin Vanilla border */
    }
    .banner-title {
        color: #EAE2B7; /* Vanilla */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 32px;
        font-weight: 700;
        margin: 0;
        letter-spacing: 1px;
    }
    /* Hide Streamlit padding for a cleaner dashboard look */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Display the Top Banner
st.markdown('<div class="top-banner"><p class="banner-title">Veritas Bank Churn Risk Analysis</p></div>', unsafe_allow_html=True)

# 5. Single Tab Dashboard Logic
# We create one tab called "Analytics" as requested
tab_analytics = st.tabs(["Dashboard Analytics"])[0]

with tab_analytics:
    # Your specific Power BI Public Embed URL
    pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiOWEzMDI0NzctYzZiMC00Mjc4LWI5MzgtNDk3YmRiZTUxZmVjIiwidCI6IjhkMWE2OWVjLTAzYjUtNDM0NS1hZTIxLWRhZDExMmY1ZmI0ZiIsImMiOjN9"
    
    # We set height to 800 to ensure the full report and the bottom navigation bar are visible
    st.components.v1.iframe(pbi_url, height=850, scrolling=False)