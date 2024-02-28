import streamlit as st
import pyodbc



# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    servername = 'DESKTOP-5IAPFQC'
    dbname = 'NFL_Data'
    trusted_conneciton = '?trusted_conneciton=yes'
    driver = '&driver=ODBC+Driver+17+for+SQL+Server'
    username = 'MAKeith92'
    password = 'Lopez!123'
    
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + servername
        + ";DATABASE="
        + dbname
        + ";UID="
        + username
        + ";PWD="
        + password
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from defense_and_fumbles;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")