# ============================================================
# pages/4_ _SQL_Analytics.py - SQL Analytics Page
# ============================================================

import streamlit as st
import sys
import os

# Add utils to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from db_connection
from utils.db_connection import get_db_connection, execute_query, get_table_names

# Import SQL queries
from utils.sql_queries import SQL_QUERIES

st.set_page_config(
    page_title="SQL Analytics - Cricbuzz LiveStats",
    page_icon="🔍",
    layout="wide"
)

def show():
    """Display the SQL Analytics page"""
    
    st.title("🔍 SQL Analytics")
    st.markdown("Execute and view results of 25+ SQL queries")
    
    # ============================================================
    # SIDEBAR - Database Status
    # ============================================================
    st.sidebar.markdown("---")
    st.sidebar.subheader("🗄️ Database Status")
    
    # Test connection
    conn = get_db_connection()
    if conn:
        st.sidebar.success("✅ Connected to MySQL")
        st.sidebar.info("📊 Database: crickbuzz_db")
        
        # Show tables
        tables = get_table_names()
        if tables:
            st.sidebar.write(f"📋 Tables found: {len(tables)}")
            with st.sidebar.expander("View Tables"):
                for table in tables:
                    st.sidebar.write(f"- {table}")
        conn.close()
    else:
        st.sidebar.error("❌ Database connection failed")
        st.sidebar.info("💡 Make sure MySQL is running and credentials are correct")
    
    # ============================================================
    # SIDEBAR - Query Filters
    # ============================================================
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎯 Filter Queries")
    
    level_filter = st.sidebar.radio(
        "Select Difficulty Level",
        ["All", "Beginner", "Intermediate", "Advanced"]
    )
    
    # Get filtered queries
    if level_filter == "All":
        filtered_queries = SQL_QUERIES
    else:
        filtered_queries = {k: v for k, v in SQL_QUERIES.items() if v.get('level') == level_filter}
    
    # ============================================================
    # MAIN CONTENT
    # ============================================================
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 Available Queries")
        query_names = list(filtered_queries.keys())
        
        if query_names:
            selected_query = st.selectbox("Select Query", query_names)
        else:
            st.warning("No queries found for selected level")
            selected_query = None
    
    with col2:
        if selected_query and selected_query in SQL_QUERIES:
            query_info = SQL_QUERIES[selected_query]
            st.subheader(f"📊 {selected_query}")
            
            # Display query info
            col_info1, col_info2 = st.columns(2)
            with col_info1:
                level = query_info.get('level', 'Not specified')
                st.info(f"**Level:** {level}")
                description = query_info.get('description', 'No description available')
                st.markdown(f"**Description:** {description}")
            with col_info2:
                st.code(query_info['query'], language="sql")
            
            # Execute button
            if st.button("▶️ Execute Query", type="primary"):
                with st.spinner("Executing query..."):
                    result = execute_query(query_info['query'])
                    if result is not None:
                        if not result.empty:
                            st.success(f"✅ Query executed successfully! Found {len(result)} rows")
                            st.dataframe(result, use_container_width=True)
                            st.caption(f"📊 {len(result)} rows × {len(result.columns)} columns")
                        else:
                            # ============================================================
                            # FRIENDLY MESSAGE FOR NO RESULTS
                            # ============================================================
                            st.warning("⚠️ No data matches the criteria for this question.")
                            
                            # Show helpful info based on the query
                            query_text = query_info['query'].lower()
                            
                            # Check if this is a data availability issue
                            if "q22" in query_text.lower() or "head_to_head" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - This query looks for teams that have played **5+ matches** against each other
                                - The current dataset doesn't have enough historical matches yet
                                - You need to add more match data to see results here
                                """)
                            elif "q23" in query_text.lower() or "player_form" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - This query requires players with **10+ innings** (10+ balls each)
                                - The current dataset doesn't have players with enough innings yet
                                - Try running Q13 first to populate match data
                                """)
                            elif "q24" in query_text.lower() or "partnerships" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - This query looks for batting pairs with **5+ partnerships**
                                - The current dataset doesn't have enough partnership data yet
                                - Try running Q13 first to populate partnership data
                                """)
                            elif "q25" in query_text.lower() or "career_trajectory" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - This query requires players with **6+ quarters** of data
                                - The current dataset doesn't have enough historical data yet
                                - You need matches spanning multiple quarters/years
                                """)
                            elif "q10" in query_text.lower() or "completed_matches" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - No completed matches found in the database
                                - Try running Q10 to populate completed matches data
                                """)
                            elif "q21" in query_text.lower() or "performance_ranking" in query_text:
                                st.info("""
                                💡 **Why no results?**
                                - Performance ranking requires batting, bowling, and fielding data
                                - The current dataset may not have all required data
                                - Try running Q18 and Q19 to populate more data
                                """)
                            else:
                                st.info("""
                                💡 **Why no results?**
                                - The query returned 0 rows because:
                                - The table might be empty, or
                                - No records match the filter conditions
                                - Check the table name and column names
                                """)
                            
                            # Show table info if available
                            st.caption("📌 Tip: Try running other queries first to populate data, or check if the table has data in MySQL Workbench.")
                    else:
                        st.error("❌ Failed to execute query.")

    # ============================================================
    # SHOW ALL QUERIES
    # ============================================================
    with st.expander("📋 View All Available Queries"):
        for q_name, q_info in SQL_QUERIES.items():
            st.markdown(f"**{q_name}**")
            st.markdown(f"📌 **Level:** {q_info.get('level', 'Not specified')}")
            st.markdown(f"📝 **Description:** {q_info.get('description', 'No description')}")
            st.code(q_info['query'], language="sql")
            st.markdown("---")
    
    # ============================================================
    # CUSTOM QUERY EXECUTOR
    # ============================================================
    st.sidebar.markdown("---")
    st.sidebar.subheader("✏️ Custom Query")
    
    custom_query = st.sidebar.text_area(
        "Write your own SQL query:", 
        height=150,
        placeholder="SELECT * FROM players_india LIMIT 10"
    )
    
    if st.sidebar.button("▶️ Run Custom Query", type="primary"):
        if custom_query:
            with st.spinner("Executing custom query..."):
                result = execute_query(custom_query)
                if result is not None:
                    if not result.empty:
                        st.sidebar.success("✅ Query executed!")
                        st.subheader("📊 Custom Query Results")
                        st.dataframe(result, use_container_width=True)
                        st.caption(f"📊 {len(result)} rows × {len(result.columns)} columns")
                    else:
                        st.sidebar.warning("No results returned")
        else:
            st.sidebar.error("Please write a query first")

# Call show() when this page is loaded
show()