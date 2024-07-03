import time

import streamlit as st

import itertools

from data_analysis.pos_view import offensive_data, defensive_data

st.title("NBA 2023 stats - Positions")

my_bar = st.progress(0)

for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)
    time.sleep(0.01)
time.sleep(1)

my_bar.empty()

with open("main/static/style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

st.header("Description")
st.write(
    "Explore the distribution of the players and their relations to the positions in NBA. For each of the mentioned positions, how many players do they have? How many points were produced by position? In addition to that, they should be able to analyze defensive actions inclusive of blocks and steals accordantly to the position they play. The positional dynamics in the league are further explored in the following insights which are embedded in the interactive charts."
)

st.header("Offensive positions")

st.subheader("Number of player per positions")
st.markdown(
    f""" 
        <div class='center-container'>
           {offensive_data["Number of player per positions"].to_html(index=False)}
        </div>
    """,
    unsafe_allow_html=True,
)

for chave, dado in itertools.islice(offensive_data.items(), 1, None):
    st.subheader(chave)
    st.plotly_chart(dado)

st.header("Defensive positions")

for chave, dado in defensive_data.items():
    st.subheader(chave)
    st.plotly_chart(dado)