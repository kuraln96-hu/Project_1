# ============================================================
# app.py - Main Streamlit Application
# ============================================================

import streamlit as st

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="🏏 Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://img.icons8.com/color/96/000000/cricket.png", width=80)
st.sidebar.title("🏏 Cricbuzz LiveStats")
st.sidebar.markdown("---")

# Streamlit automatically handles page navigation
# This is the main/home page content
st.markdown('<p class="main-header">🏏 Welcome to Cricbuzz LiveStats</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Real-time cricket analytics, live scores, and player statistics</p>', unsafe_allow_html=True)

# Main dashboard content
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Matches", "124", "+12")
with col2:
    st.metric("Teams", "8", "+0")
with col3:
    st.metric("Players", "156", "+5")
with col4:
    st.metric("Live Now", "3", "🔥")

st.markdown("---")

# Quick links section
st.subheader("📊 Quick Access")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **📡 Live Matches**  
    View ongoing and upcoming matches with real-time updates
    """)
    
    st.info("""
    **📊 Top Player Stats**  
    Leaderboards for runs, wickets, and more
    """)

with col2:
    st.info("""
    **🔍 SQL Analytics**  
    Run custom queries and analyze match data
    """)
    
    st.info("""
    **🛠️ CRUD Operations**  
    Add, update, or delete player records
    """)

st.markdown("---")

# Features section
st.subheader("🚀 Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📡 Live Scores**  
    Real-time cricket match updates and scores
    """)

with col2:
    st.markdown("""
    **📊 Player Analytics**  
    In-depth statistics and performance metrics
    """)

with col3:
    st.markdown("""
    **🔍 Data Insights**  
    SQL-powered analytics and visualizations
    """)

st.sidebar.markdown("---")
st.sidebar.info("""
**Project:** Cricbuzz LiveStats  
**Tech:** Python • Streamlit • SQL • REST API  
**Domain:** Sports Analytics
""")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ using Streamlit")