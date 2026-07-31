# ============================================================
# pages/5_🛠️_CRUD_Operations.py - CRUD Operations Page
# ============================================================

import streamlit as st
import pandas as pd
import sys
import os

# Add utils to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.db_connection import get_db_connection

def show():
    """Display the CRUD Operations page"""
    
    st.set_page_config(
        page_title="CRUD Operations - Cricbuzz LiveStats",
        page_icon="🛠️",
        layout="wide"
    )
    
    st.title("🛠️ CRUD Operations")
    st.markdown("Create, Read, Update, and Delete player records")
    
    # ============================================================
    # OPERATION SELECTION
    # ============================================================
    operation = st.radio(
        "Select Operation",
        ["📋 View Records", "➕ Add Record", "✏️ Update Record", "❌ Delete Record"],
        horizontal=True
    )
    
    # ============================================================
    # DATABASE CONNECTION
    # ============================================================
    conn = get_db_connection()
    if not conn:
        st.error("❌ Database connection failed. Please check your MySQL connection.")
        return
    
    cursor = conn.cursor()
    
    # ============================================================
    # OPERATION: VIEW RECORDS
    # ============================================================
    if operation == "📋 View Records":
        st.subheader("📋 View Records")
        
        # Get list of tables
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        
        if tables:
            selected_table = st.selectbox("Select Table", tables)
            
            if selected_table:
                # Show table schema
                with st.expander("📋 Table Schema"):
                    cursor.execute(f"DESCRIBE {selected_table}")
                    schema = cursor.fetchall()
                    st.dataframe(
                        pd.DataFrame(schema, columns=['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']),
                        use_container_width=True
                    )
                
                # Show table data
                limit = st.slider("Rows to display", 5, 100, 20)
                cursor.execute(f"SELECT * FROM {selected_table} LIMIT {limit}")
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                
                if results:
                    df = pd.DataFrame(results, columns=columns)
                    st.dataframe(df, use_container_width=True)
                    st.caption(f"📊 Showing {len(results)} rows from {selected_table}")
                    
                    # Download button
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name=f"{selected_table}_data.csv",
                        mime="text/csv"
                    )
                else:
                    st.info(f"ℹ️ Table '{selected_table}' has no data")
        else:
            st.warning("⚠️ No tables found in the database")
    
    # ============================================================
    # OPERATION: ADD RECORD (FIXED)
    # ============================================================
    elif operation == "➕ Add Record":
        st.subheader("➕ Add New Player")
        
        # Check if players_india table exists
        cursor.execute("SHOW TABLES LIKE 'players_india'")
        if not cursor.fetchone():
            st.error("❌ Table 'players_india' not found. Please run Question 1 first to create the table.")
            cursor.close()
            conn.close()
            return
        
        with st.form("add_player_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                player_name = st.text_input("Player Name *", placeholder="Enter player name")
                player_role = st.selectbox(
                    "Playing Role",
                    ["Batsman", "Bowler", "All Rounder", "Wicket Keeper"]
                )
            
            with col2:
                batting_style = st.selectbox(
                    "Batting Style",
                    ["Right-hand bat", "Left-hand bat"]
                )
                bowling_style = st.text_input("Bowling Style", placeholder="e.g., Right-arm fast", value="N/A")
            
            submitted = st.form_submit_button("➕ Add Player", type="primary")
            
            if submitted:
                if not player_name:
                    st.warning("⚠️ Player Name is required!")
                else:
                    try:
                        # Get the max Player_id to generate a new one
                        cursor.execute("SELECT MAX(Player_id) FROM players_india")
                        max_id = cursor.fetchone()[0]
                        new_id = (max_id if max_id else 0) + 1
                        
                        cursor.execute("""
                            INSERT INTO players_india 
                            (Player_id, Player_name, Player_role, Batting_style, Bowling_style)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (new_id, player_name, player_role, batting_style, bowling_style))
                        conn.commit()
                        st.success(f"✅ Player '{player_name}' added successfully! (ID: {new_id})")
                        st.balloons()
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error adding player: {e}")
    
    # ============================================================
    # OPERATION: UPDATE RECORD
    # ============================================================
    elif operation == "✏️ Update Record":
        st.subheader("✏️ Update Player Record")
        
        # Check if players_india table exists
        cursor.execute("SHOW TABLES LIKE 'players_india'")
        if not cursor.fetchone():
            st.error("❌ Table 'players_india' not found. Please run Question 1 first to create the table.")
            cursor.close()
            conn.close()
            return
        
        # Get existing players
        cursor.execute("SELECT Player_id, Player_name, Player_role, Batting_style, Bowling_style FROM players_india ORDER BY Player_name")
        players = cursor.fetchall()
        
        if players:
            player_options = [f"{p[0]} - {p[1]}" for p in players]
            selected_player = st.selectbox("Select Player to Update", player_options)
            
            if selected_player:
                player_id = int(selected_player.split(" - ")[0])
                current_data = None
                for p in players:
                    if p[0] == player_id:
                        current_data = p
                        break
                
                if current_data:
                    with st.form("update_player_form"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            new_name = st.text_input("Player Name", value=current_data[1])
                            role_options = ["Batsman", "Bowler", "All Rounder", "Wicket Keeper"]
                            role_index = 0
                            if current_data[2] in role_options:
                                role_index = role_options.index(current_data[2])
                            new_role = st.selectbox("Playing Role", role_options, index=role_index)
                        
                        with col2:
                            batting_options = ["Right-hand bat", "Left-hand bat"]
                            batting_index = 0 if current_data[3] == "Right-hand bat" else 1
                            new_batting = st.selectbox("Batting Style", batting_options, index=batting_index)
                            new_bowling = st.text_input("Bowling Style", value=current_data[4] if current_data[4] else "N/A")
                        
                        submitted = st.form_submit_button("✏️ Update Player", type="primary")
                        
                        if submitted:
                            try:
                                cursor.execute("""
                                    UPDATE players_india 
                                    SET Player_name = %s, Player_role = %s, 
                                        Batting_style = %s, Bowling_style = %s
                                    WHERE Player_id = %s
                                """, (new_name, new_role, new_batting, new_bowling, player_id))
                                conn.commit()
                                st.success(f"✅ Player '{new_name}' updated successfully!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Error updating player: {e}")
        else:
            st.info("ℹ️ No players found to update. Add some players first!")
    
    # ============================================================
    # OPERATION: DELETE RECORD
    # ============================================================
    elif operation == "❌ Delete Record":
        st.subheader("❌ Delete Player Record")
        
        # Check if players_india table exists
        cursor.execute("SHOW TABLES LIKE 'players_india'")
        if not cursor.fetchone():
            st.error("❌ Table 'players_india' not found. Please run Question 1 first to create the table.")
            cursor.close()
            conn.close()
            return
        
        # Get existing players
        cursor.execute("SELECT Player_id, Player_name FROM players_india ORDER BY Player_name")
        players = cursor.fetchall()
        
        if players:
            player_options = [f"{p[0]} - {p[1]}" for p in players]
            selected_player = st.selectbox("Select Player to Delete", player_options)
            
            if selected_player:
                player_id = int(selected_player.split(" - ")[0])
                player_name = selected_player.split(" - ")[1]
                
                st.warning(f"⚠️ Are you sure you want to delete **{player_name}**? This action cannot be undone!")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🗑️ Yes, Delete Player", type="primary"):
                        try:
                            cursor.execute("DELETE FROM players_india WHERE Player_id = %s", (player_id,))
                            conn.commit()
                            st.success(f"✅ Player '{player_name}' deleted successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error deleting player: {e}")
                with col2:
                    if st.button("❌ Cancel"):
                        st.info("Deletion cancelled")
        else:
            st.info("ℹ️ No players found to delete. Add some players first!")
    
    # ============================================================
    # CLOSE CONNECTION
    # ============================================================
    cursor.close()
    conn.close()
    
    # ============================================================
    # SIDEBAR INFO
    # ============================================================
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **🛠️ CRUD Operations**
    
    - **View:** Browse all tables
    - **Add:** Insert new players
    - **Update:** Modify existing records
    - **Delete:** Remove players
    """)

# Auto-run show() when this page is loaded
if __name__ == "__main__":
    show()