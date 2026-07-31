# ============================================================
# pages/1_🏏_Home.py - Home Page
# ============================================================

import streamlit as st

def show():
    """Display the Home page"""
    
    st.set_page_config(
        page_title="Home - Cricbuzz LiveStats",
        page_icon="🏠",
        layout="wide"
    )
    
    # Your home page content here
    st.markdown('<div class="main-header">🏏 Cricbuzz LiveStats</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Real-Time Cricket Insights & SQL-Based Analytics</div>', unsafe_allow_html=True)
    
    # Project overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📡 Live Matches", "Real-Time", "API")
        st.caption("Ongoing matches with scorecards")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📊 Players", "1000+", "Database")
        st.caption("Comprehensive player statistics")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🔍 SQL Queries", "25", "Analytics")
        st.caption("Beginner to Advanced queries")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Features section
    st.subheader("🎯 Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 📡 Live Match Updates
        - Real-time scores and scorecards
        - Batsmen/Bowler information
        - Match status and venue details
        - Auto-refresh for live matches
        """)
        
        st.markdown("""
        #### 📊 Top Player Stats
        - Most runs, highest scores
        - Most wickets, best economy
        - Filter by format (Test/ODI/T20)
        - Visual charts and tables
        """)
    
    with col2:
        st.markdown("""
        #### 🔍 SQL Analytics
        - 25+ SQL queries
        - Beginner to Advanced levels
        - Interactive query selection
        - Tabular results display
        """)
        
        st.markdown("""
        #### 🛠️ CRUD Operations
        - Create new player records
        - Read/View existing data
        - Update player statistics
        - Delete records
        """)
    
    st.markdown("---")
    
    # Tech stack
    st.subheader("🛠️ Technology Stack")
    
    tech_cols = st.columns(4)
    with tech_cols[0]:
        st.markdown("**🐍 Python**")
        st.caption("3.8+")
    with tech_cols[1]:
        st.markdown("**📊 Streamlit**")
        st.caption("1.28+")
    with tech_cols[2]:
        st.markdown("**🗄️ MySQL**")
        st.caption("8.0+")
    with tech_cols[3]:
        st.markdown("**🌐 REST API**")
        st.caption("Cricbuzz API")
    
    st.markdown("---")
    
    # Quick stats from database
    st.subheader("📊 Database Statistics")
    
    try:
        from utils.db_connection import get_db_connection
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # Count tables and records
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            total_records = 0
            for table in tables:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
                    count = cursor.fetchone()[0]
                    total_records += count
                except:
                    pass
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📋 Tables", len(tables))
            with col2:
                st.metric("📝 Total Records", f"{total_records:,}")
            with col3:
                st.metric("🏏 Players", "500+")
            
            cursor.close()
            conn.close()
        else:
            st.warning("⚠️ Database not connected. Please check your MySQL connection.")
        
    except Exception as e:
        st.warning(f"⚠️ Database connection: {e}")
    
    st.markdown("---")
    st.caption("💡 Use the sidebar to navigate between pages")

# Auto-run show() when this page is loaded directly
if __name__ == "__main__":
    show()