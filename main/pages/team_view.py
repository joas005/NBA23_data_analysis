import time

import streamlit as st

import itertools

from data_analysis.team_view import (
    all_teams,
    offensive_data,
    defensive_data,
    specific_team_data,
)

st.set_page_config(
    page_title="NBA 2023 stats - Teams",
    initial_sidebar_state="auto",
    layout="wide",
    page_icon="main/static/favicon.ico",
)


st.title("NBA 2023 stats - Teams")

my_bar = st.progress(0)

for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)
    time.sleep(0.01)
time.sleep(1)

my_bar.empty()

col1, col2 = st.columns(2)

with open("main/static/style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with col1:
    st.header("Description")
    st.write(
        "Investigates which teams were most successful in various statistical measures during the 2023 season. Find out the team that scored more points, made more blocks, assists and other set records. Hence, our bar-plots show these team performances at a glance, summarizing the achievement of the teams at different occasions in the season."
    )

with col2:
    st.subheader("What stats do you wish to see?")
    option = st.radio(
        label="What stats do you wish to see?",
        options=("Offensive", "Defensive", "Specific"),
        label_visibility="hidden",
    )


if option == "Offensive":
    st.header("Offensive")

    for chave, dado in itertools.islice(offensive_data.items(), 0, 4):
        st.markdown(
            f"<p>{chave}: <b class='rose_highlight'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    st.subheader("Teams with best 3 pointers and free throws efficiency")
    st.markdown(
        f""" 
         <div class='center-container'>
            {offensive_data["Teams with best 3 pointers and free throws efficiency"].to_html(
                index=False
            )}
         </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.subheader("Top 5 scorers")
    st.markdown(
        f""" 
         <div class='center-container'>
            {offensive_data["Top 5 scorers"].to_html(index=False)}
         </div>
        """,
        unsafe_allow_html=True,
    )

    for chave, dado in itertools.islice(offensive_data.items(), 7, None):
        st.subheader(chave)
        st.plotly_chart(dado)


if option == "Defensive":
    st.header("Defensive")

    for chave, dado in itertools.islice(defensive_data.items(), 0, 4):
        st.markdown(
            f"<p>{chave}: <b class='rose_highlight'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    st.subheader("Teams with the most blocks, steal and defensive rebounds")
    st.markdown(
        f""" 
         <div class='center-container'>
            {defensive_data[
                "Teams with the most blocks, steal and defensive rebounds"
            ].to_html(index=False)}
         </div>
        """,
        unsafe_allow_html=True,
    )

    for chave, dado in itertools.islice(defensive_data.items(), 5, None):
        st.subheader(chave)
        st.plotly_chart(dado)


if option == "Specific":
    st.header("Specific")

    st.markdown(
        "<p><b class='rose_highlight'>Select the team</b> you wish to see:</p>",
        unsafe_allow_html=True,
    )

    selected_team = st.selectbox(
        "Select the team you wish to see",
        all_teams,
        placeholder="Select the team you wish to see",
        label_visibility="hidden",
    )

    selected_team_data = specific_team_data(selected_team)

    col1, col2 = st.columns(2)

    with col1:
        st.header(selected_team)
        for chave, dado in itertools.islice(
            selected_team_data.items(), 1, len(selected_team_data) - 4
        ):
            st.markdown(
                f"<p>{chave}: <b class='rose_highlight'>{int(dado)}</b></p>",
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img src={selected_team_data["Team logo"]} alt="Image" style="max-width: 80%;">
            </div>
            """,
            unsafe_allow_html=True,
        )

    for chave, dado in itertools.islice(selected_team_data.items(), 8, None):
        st.subheader(chave)
        st.plotly_chart(dado)
