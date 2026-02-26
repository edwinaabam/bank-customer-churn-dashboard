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
        st.image(image)
    else:
        st.warning("Logo file 'banklogo.png' not found in root directory.")

    st.title("Navigation")
    st.markdown("---")
    st.info("Use the navigation arrows at the bottom of the dashboard to switch between report pages.")

# 3. Custom CSS for the Top Banner (Navy Blue & Vanilla)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

    /* Keep the top of the screen clear so the banner isn't cut off */
    .block-container {
        padding-top: 4rem !important; 
    }

    .top-banner {
        background-color: #003049; /* Navy Blue */
        /* Tight padding makes the big font fill the box height */
        padding-top: 20px;    
        padding-bottom: 20px; 
        border-radius: 15px;   
        text-align: center;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .banner-title {
        color: #EAE2B7; /* Vanilla */
        font-family: Segoe UI;
        font-size: 200px; /* Massive font size */
        font-weight: 900; /* Maximum thickness for the letters */
        margin: 0;
        line-height: 0.9; /* Tightens the space around the letters */
        letter-spacing: 1px;
        text-transform: uppercase;
        white-space: nowrap; /* Prevents the giant text from breaking into two lines */
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


