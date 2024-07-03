import time

import streamlit as st

from itertools import islice

from data_analysis.player_view import (
    offensive_data,
    defensive_data,
    data_to_plot,
    full_name_stats_map,
    full_name_stats_list,
    create_player_vs_avarage_graph,
    specific_player_data,
)

st.set_page_config(
    page_title="NBA 2023 stats - Players",
    initial_sidebar_state="auto",
    layout="wide",
    page_icon="main/static/favicon.ico",
)

st.title("NBA 2023 stats - Players")

my_bar = st.progress(0)

for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)
    time.sleep(0.03)
time.sleep(1)

my_bar.empty()

col1, col2 = st.columns(2)

with open("main/static/style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with col1:
    st.header("Description")
    st.write(
        "Acquire a broad view of certain statistics of the players in each team in the league. We will look at each of the players by their shooting, passing, and other general attributes in order to appreciate them as worthy components of the respective teams. The work includes player profiles and the real-time experience of different trends in players’ performances to perform the analysis of the specific player’s contribution and his/her trends during the match."
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

    for chave, dado in islice(offensive_data.items(), 0, 6):
        st.markdown(
            f"<p>{chave}: <b class='rose_highlight'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    st.subheader("Top 10 players with the most triple doubles")
    st.markdown(
        f""" 
         <div class='center-container'>
            {offensive_data["Top 10 players with the most triple doubles"].to_html(index=False)}
         </div>
        """,
        unsafe_allow_html=True,
    )

    for chave, dado in islice(offensive_data.items(), 7, None):
        st.subheader(chave)
        st.plotly_chart(dado)

if option == "Defensive":
    st.header("Defensive")

    for chave, dado in islice(defensive_data.items(), 0, 4):
        st.markdown(
            f"<p>{chave}: <b class='rose_highlight'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    for chave, dado in islice(defensive_data.items(), 4, None):
        st.subheader(chave)
        st.plotly_chart(dado)


if option == "Specific":
    st.header("Specific")

    st.markdown(
        "<p>Enter the <b class='rose_highlight'>full name</b> of the player you wish to see:</p>",
        unsafe_allow_html=True,
    )
    player_selected = st.text_input(
        label="Insert the full name of the player you wish to see",
        placeholder="LeBron James",
        label_visibility="hidden",
    )

    if player_selected == "":
        player_selected = "LeBron James"
        player_selected_df = specific_player_data(player_selected)

    else:
        player_selected_df = specific_player_data(player_selected)

    if (
        player_selected_df["PName"].to_string(index=False).lower()
        != player_selected.lower()
    ):
        player_found = False
    else:
        player_found = True

    if not (player_found):
        st.markdown(
            f"<p>Player <b class='rose_highlight'>{player_selected}</b> not found! Please make sure you're typing the full name of a valid NBA 2023 player!</p>",
            unsafe_allow_html=True,
        )

    if player_found:
        col1, col2 = st.columns(2)

        with col1:
            st.header(player_selected_df["PName"].to_string(index=False))
            st.markdown(
                f"""
                <ul>
                    <li>
                        <p class='major_data'>Players's age: <b class='indigo_highlight'>{player_selected_df['Age'].to_string(index=False)}</b></p>
                    </li>
                    <li>
                        <p class='major_data'>Player's position: <b class='indigo_highlight'>{player_selected_df['POS'].to_string(index=False)}</b></p>
                    </li>
                    <li>
                        <p class='major_data'>Player's number of double doubles: <b class='indigo_highlight'>{player_selected_df['DD2'].to_string(index=False)}</b></p>
                    </li>
                    <li>
                        <p class='major_data'>Player's number of triple doubles: <b class='indigo_highlight'>{player_selected_df['TD3'].to_string(index=False)}</b></p>
                    </li>
                    <li>
                        <p class='major_data'>Player's avarage points per game: <b class='indigo_highlight'>{player_selected_df['PTSperGP'].to_string(index=False)}</b></p>
                    </li>
                    <li>
                        <p class='major_data'>Player's total defensive actions: <b class='indigo_highlight'>{player_selected_df['DEF_ACTIONS'].to_string(index=False)}</b></p>
                    </li>
                </ul>""",
                unsafe_allow_html=True,
            )

        with col2:
            st.header(player_selected_df["team_name"].to_string(index=False))
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <img src={player_selected_df["team_img"].to_string(index=False)} alt="Image" style="max-width: 50%;">
                </div>
                """,
                unsafe_allow_html=True,
            )

        data_col1, data_col2 = st.columns(2)

        for i in range(int(len(data_to_plot) / 2)):
            with data_col1:
                st.markdown(
                    f"<p>{full_name_stats_list[i]}: <b class='rose_highlight'>{player_selected_df[data_to_plot[i]].to_string(index=False)}</b></p>",
                    unsafe_allow_html=True,
                )

        for j in range(int(len(data_to_plot) / 2), int(len(data_to_plot))):
            with data_col2:
                st.markdown(
                    f"<p>{full_name_stats_list[j]}: <b class='rose_highlight'>{player_selected_df[data_to_plot[j]].to_string(index=False)}</b></p>",
                    unsafe_allow_html=True,
                )

        st.subheader("Player stats vs avarage stats from the league")
        st.markdown(
            "<p><b class='rose_highlight'>Wich stats</b> do you wish to compare:</p>",
            unsafe_allow_html=True,
        )

        selected_data_plot = st.multiselect(
            "Quais dados você deseja ver?",
            full_name_stats_list,
            default=[
                "Games played",
                "Field goals made",
                "3 points made",
                "3 points efficiency",
                "Free throws made",
                "Offensive rebounds",
            ],
            label_visibility="hidden",
        )
        player_vs_avarage_graph = create_player_vs_avarage_graph(
            player_selected_df, selected_data_plot
        )

        if len(selected_data_plot) >= 1:
            st.plotly_chart(player_vs_avarage_graph)

        else:
            st.write("Selected the data you want to see")
