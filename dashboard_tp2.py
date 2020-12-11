import pandas as pd
from pymongo import MongoClient
import streamlit as st

client = MongoClient('localhost', 4043)
db = client.api_fetch
table = db.table

st.write("""
Bonjour, 

bienvenue sur une représenation du fetch d'une api
""")

@st.cache
def load_data(year: int):
    victimWithEachWeapon = table.aggregate([
    {"$match": {"Year": year}},
    { "$group" : {
        "_id": "$Weapon", "victimes": {"$sum": "$Victim Count"}
    }}
])

    return list(victimWithEachWeapon)

user_input = st.number_input("Année du crime commis", value=1980)

data = load_data(user_input)
df = pd.DataFrame(data)

if(len(df)):
    st.write(df)
    st.bar_chart(df.rename(columns={'_id': 'index'}).set_index('index'))
else:
    st.write("""
    Aucun crime commis sur cette date
""")