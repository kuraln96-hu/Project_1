# ============================================================
# utils/db_connection.py - Database Connection
# ============================================================

import mysql.connector
import streamlit as st
import pandas as pd

# Database configuration
MYSQL_CONFIG = {
    'user': 'root',
    'password': 'Murugaku@9693',
    'host': '127.0.0.1',
    'database': 'crickbuzz_db'
}

def get_db_connection():
    """Get database connection"""
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        return conn
    except Exception as e:
        st.error(f"❌ Database connection failed: {e}")
        return None

def execute_query(query):
    """Execute a SQL query and return results as DataFrame"""
    conn = get_db_connection()
    if conn is None:
        st.error("❌ Database connection failed.")
        return None
    
    try:
        result = pd.read_sql(query, conn)
        conn.close()
        return result
    except Exception as e:
        st.error(f"❌ Query execution failed: {e}")
        conn.close()
        return None

def get_table_names():
    """Get list of all tables in the database"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        cursor.close()
        conn.close()
        return tables
    except Exception as e:
        st.error(f"❌ Failed to get tables: {e}")
        conn.close()
        return []