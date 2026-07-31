import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Top Player Stats - Cricbuzz LiveStats",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Top Player Stats")
st.markdown("Leaderboards for runs, wickets, and more")

# Generate sample player data
@st.cache_data
def generate_player_data():
    players = [
        "Virat Kohli", "Rohit Sharma", "Steve Smith", "Kane Williamson",
        "Joe Root", "Babar Azam", "KL Rahul", "David Warner",
        "Rashid Khan", "Jasprit Bumrah", "Pat Cummins", "Trent Boult",
        "Shaheen Afridi", "Kagiso Rabada", "Mitchell Starc"
    ]
    
    data = []
    for player in players:
        matches = random.randint(10, 150)
        runs = random.randint(500, 12000)
        wickets = random.randint(0, 300)
        avg = round(runs / max(1, matches), 2)
        sr = random.randint(80, 160)
        hs = random.randint(80, 260)
        
        data.append({
            "Player": player,
            "Matches": matches,
            "Runs": runs,
            "Average": avg,
            "Strike Rate": sr,
            "Highest Score": hs,
            "Wickets": wickets,
            "Country": random.choice(["India", "Australia", "England", "New Zealand", "Pakistan", "South Africa"])
        })
    
    return pd.DataFrame(data)

# Get data
df_players = generate_player_data()

# Top tabs
tab1, tab2, tab3 = st.tabs(["🏏 Most Runs", "🎯 Most Wickets", "🏆 All-Rounders"])

with tab1:
    st.subheader("🏏 Top Run Scorers")
    top_runs = df_players.nlargest(5, "Runs")
    st.dataframe(top_runs[["Player", "Country", "Matches", "Runs", "Average", "Highest Score"]], use_container_width=True)
    
    # Display as cards instead of chart
    for idx, row in top_runs.iterrows():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.markdown(f"**{row['Player']}**")
            st.markdown(f"🇮🇳 {row['Country']}")
        with col2:
            st.markdown(f"**Runs:** {row['Runs']}")
            st.markdown(f"**Average:** {row['Average']}")
        with col3:
            st.markdown(f"**Matches:** {row['Matches']}")
            st.markdown(f"**HS:** {row['Highest Score']}")
        st.markdown("---")

with tab2:
    st.subheader("🎯 Top Wicket Takers")
    top_wickets = df_players.nlargest(5, "Wickets")
    st.dataframe(top_wickets[["Player", "Country", "Matches", "Wickets", "Average"]], use_container_width=True)
    
    for idx, row in top_wickets.iterrows():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.markdown(f"**{row['Player']}**")
            st.markdown(f"🇮🇳 {row['Country']}")
        with col2:
            st.markdown(f"**Wickets:** {row['Wickets']}")
            st.markdown(f"**Average:** {row['Average']}")
        with col3:
            st.markdown(f"**Matches:** {row['Matches']}")
        st.markdown("---")

with tab3:
    st.subheader("🏆 Best All-Rounders")
    df_players["All-Round Rating"] = (df_players["Runs"] / 100) + (df_players["Wickets"] * 2)
    top_allrounders = df_players.nlargest(5, "All-Round Rating")
    st.dataframe(top_allrounders[["Player", "Country", "Runs", "Wickets", "All-Round Rating"]], use_container_width=True)
    
    for idx, row in top_allrounders.iterrows():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.markdown(f"**{row['Player']}**")
            st.markdown(f"🇮🇳 {row['Country']}")
        with col2:
            st.markdown(f"**Runs:** {row['Runs']}")
            st.markdown(f"**Wickets:** {row['Wickets']}")
        with col3:
            st.markdown(f"**Rating:** {row['All-Round Rating']:.1f}")
        st.markdown("---")

st.sidebar.markdown("---")
st.sidebar.info("""
**📈 Stats Updated:** Today
**🔄 Refresh** to see latest data
""")