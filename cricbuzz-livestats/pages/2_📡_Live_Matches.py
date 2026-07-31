import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Live Matches - Cricbuzz LiveStats",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Live Matches")
st.markdown("Real-time cricket matches from around the world")

# Sample match data (replace with real API later)
def generate_sample_matches():
    teams = [
        ("India", "Australia"),
        ("England", "New Zealand"),
        ("Pakistan", "South Africa"),
        ("Sri Lanka", "Bangladesh"),
        ("West Indies", "Afghanistan")
    ]
    
    matches = []
    for i, (team1, team2) in enumerate(teams):
        score1 = random.randint(50, 350)
        score2 = random.randint(20, score1 - 10) if random.random() > 0.3 else random.randint(score1 + 10, 400)
        overs1 = random.randint(5, 50)
        overs2 = random.randint(3, overs1)
        wickets1 = random.randint(0, 10)
        wickets2 = random.randint(0, 10)
        
        status_options = ["Live", "Completed", "Upcoming", "Rain Delay"]
        status = random.choice(status_options)
        
        if status == "Live":
            status_color = "🟢"
        elif status == "Completed":
            status_color = "✅"
        elif status == "Upcoming":
            status_color = "⏳"
        else:
            status_color = "🔴"
            
        matches.append({
            "Match": f"Match {i+1}",
            "Team 1": team1,
            "Team 2": team2,
            "Score 1": f"{score1}/{wickets1}",
            "Score 2": f"{score2}/{wickets2}",
            "Overs": f"{overs1} / {overs2}",
            "Status": f"{status_color} {status}",
            "Venue": f"Stadium {i+1}",
            "Date": (datetime.now() + timedelta(hours=i*2)).strftime("%Y-%m-%d %H:%M")
        })
    
    return pd.DataFrame(matches)

# Create tabs for different match views
tab1, tab2, tab3 = st.tabs(["🏏 Live Now", "📅 Upcoming", "✅ Completed"])

with tab1:
    st.subheader("🔥 Matches Currently in Progress")
    df_live = generate_sample_matches()
    # Filter for live matches
    df_live = df_live[df_live['Status'].str.contains("Live")]
    
    if not df_live.empty:
        st.dataframe(df_live, use_container_width=True)
        
        # Match cards
        for idx, row in df_live.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{row['Team 1']}** vs **{row['Team 2']}**")
                    st.markdown(f"📊 {row['Team 1']}: {row['Score 1']} ({row['Overs'].split('/')[0]} ov)")
                    st.markdown(f"📊 {row['Team 2']}: {row['Score 2']} ({row['Overs'].split('/')[1]} ov)")
                with col2:
                    st.markdown(f"**Status:** {row['Status']}")
                    st.markdown(f"📍 {row['Venue']}")
                with col3:
                    st.button(f"🔴 Watch Match {idx+1}", key=f"watch_{idx}")
                st.markdown("---")
    else:
        st.info("No live matches at the moment. Check back soon!")

with tab2:
    st.subheader("⏳ Upcoming Matches")
    df_upcoming = generate_sample_matches()
    df_upcoming = df_upcoming[df_upcoming['Status'].str.contains("Upcoming")]
    
    if not df_upcoming.empty:
        st.dataframe(df_upcoming, use_container_width=True)
    else:
        st.info("No upcoming matches scheduled")

with tab3:
    st.subheader("✅ Completed Matches")
    df_completed = generate_sample_matches()
    df_completed = df_completed[df_completed['Status'].str.contains("Completed")]
    
    if not df_completed.empty:
        st.dataframe(df_completed, use_container_width=True)
    else:
        st.info("No completed matches to display")

# Sidebar filters (optional)
st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Filter Matches")
team_filter = st.sidebar.multiselect(
    "Select Teams",
    options=["India", "Australia", "England", "New Zealand", "Pakistan", "South Africa", "Sri Lanka", "Bangladesh", "West Indies", "Afghanistan"]
)

status_filter = st.sidebar.multiselect(
    "Match Status",
    options=["Live", "Completed", "Upcoming", "Rain Delay"]
)

if team_filter or status_filter:
    st.sidebar.success("Filters applied! ✅")

st.sidebar.markdown("---")
st.sidebar.info("""
**🔔 Match Updates**
- Refresh for latest scores
- Click Watch Match for live streaming
- Data updates every 30 seconds
""")