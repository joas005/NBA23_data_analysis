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

st.header("Description")
st.write(
    "Lorem ipsum dolor sit amet. Et accusamus consectetur vel tempora labore in harum quis qui delectus eius est assumenda dolores ab odit architecto. Qui consequuntur autem et quos impedit quo exercitationem eveniet nam Quis consectetur. Id repellat veritatis ea voluptas dolor non galisum consequuntur est quam quod qui excepturi quia."
)

st.header("Offensive positions")

st.subheader("Number of player per positions")
st.markdown(
    offensive_data["Number of player per positions"].to_html(index=False),
    unsafe_allow_html=True,
)

for chave, dado in itertools.islice(offensive_data.items(), 1, None):
    st.subheader(chave)
    st.plotly_chart(dado)

st.header("Defensive positions")

for chave, dado in defensive_data.items():
    st.subheader(chave)
    st.plotly_chart(dado)
