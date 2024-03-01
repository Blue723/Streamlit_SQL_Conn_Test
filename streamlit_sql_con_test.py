import streamlit as st
import pyodbc

import pandas as pd

import sqlalchemy as sal
from sqlalchemy import create_engine
from sqlalchemy.sql import text


def conn_sql_pyodbc ():
    servername = 'DESKTOP-5IAPFQC'
    dbname = 'NFL_Data'
    trusted_conneciton = '?trusted_conneciton=yes'
    driver = '{ODBC Driver 17 for SQL Server}'
    username = 'MAKeith92'
    password = 'Lopez!123'
    
    pyodbc_conn = pyodbc.connect(f'Driver={driver};SERVER={servername},1433;DATABASE={dbname};UID={username};PWD={password};')

    return pyodbc_conn
    
pyodbc_conn = conn_sql_pyodbc()







#query user selected table

def query_team_year(select_table: str, year: int, team: str, con: str):

    query = f'select * from {select_table} where Year = {year} and Team = \'{select_team}\';'

    df = pd.read_sql(query, con, index_col='Player').drop(columns=['index'])

    return df


#years
years = range(2010,2024)

team_names=[
     '49ers',
     'Bears',
     'Bengals',
     'Broncos',
     'Browns',
     'Buccaneers',
     'Buffalos',
     'Cardinals',
     'Chargers',
     'Chiefs',
     'Colts',
     'Commanders',
     'Cowboys',
     'Dolphins',
     'Eagles',
     'Falcons',
     'Giants',
     'Jaguars',
     'Jets',
     'Lions',
     'Packers',
     'Panthers',
     'Patriots',
     'Raiders',
     'Rams',
     'Ravens',
     'Saints',
     'Seahawks',
     'Steelers',
     'Texans',
     'Titans',
     'Vikings'
]

select_table_name_li = [
    'team_stats_and_ranking',
    'schedule_and_game_results',
    'team_conversions',
    'passing',
    'rushing_and_receiving',
    'kick_and_punt_returns',
    'kicking',
    'punting',
    'defense_and_fumbles',
    'scoring_summary',
    'touchdown_log',
    'opponent_touchdown_log'
]


# table name list with team and year to format
table_name_li = [
    'team_stats_and_ranking*',
    'schedule_and_game_results*',
    'team_conversions*',
    'passing*',
    'rushing_and_receiving*',
    'kick_and_punt_returns*',
    'kicking*',
    'punting*',
    'defense_and_fumbles*',
    'scoring_summary*',
    'touchdown_log*',
    'opponent_touchdown_log*'
]



#sidebar

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#titles
st.sidebar.write('Select the table you would lke to view')

#sidebar selections
# select years
select_year = st.sidebar.selectbox('Years', years)

#select table
select_table = st.sidebar.selectbox('Tables', select_table_name_li)

#select team
select_team = st.sidebar.selectbox('Teams', team_names)


#Main area

#title
st.title('NFL Data {} {}'.format(select_team, select_year))


def run_query(query):
    with pyodbc_conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query(f"SELECT * from {select_table};")

st.write(rows)

#select dataframe
#select_df = query_team_year(select_table, select_year, select_team, conn)


#show dataframe
#st.write(select_df)