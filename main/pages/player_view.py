import time

import streamlit as st

from itertools import islice

from data_analysis.player_view import (
    offensive_data,
    defensive_data,
    data_to_plot,
    specific_player_data,
)

full_name_col = {
    "GP": "Games played",
    "W": "Games won",
    "L": "Games lost",
    "Min": "Minutes played",
    "PTS": "Points",
    "FGM": "Field goals made",
    "FGA": "Field goals attempted",
    "FG%": "Field goals efficiency",
    "3PM": "3 points made",
    "3PA": "3 points attempted",
    "3P%": "3 points efficiency",
    "FTM": "Free throws made",
    "FTA": "Free throws attempted",
    "FT%": "Free throws efficiency",
    "OREB": "Offensive rebounds",
    "DREB": "Deffensive rebounds",
    "REB": "Rebounds",
    "AST": "Assists",
    "TOV": "Turn-overs",
    "STL": "Steals",
    "BLK": "Blocks",
    "PF": "Personal fouls",
    "FP": "Foul plays",
    "2PM": "2 points made",
    "2PA": "2 points attempted",
    "2P%": "2 points efficiency",
}

st.title("NBA 2023 stats - Players")

my_bar = st.progress(0)

for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)
    time.sleep(0.03)
time.sleep(1)

my_bar.empty()

col1, col2 = st.columns(2)

st.markdown(
    """
    <style>
    .center-table {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with col1:
    st.header("Description")
    st.write(
        "Lorem ipsum dolor sit amet. Et accusamus consectetur vel tempora labore in harum quis qui delectus eius est assumenda dolores ab odit architecto. Qui consequuntur autem et quos impedit quo exercitationem eveniet nam Quis consectetur. Id repellat veritatis ea voluptas dolor non galisum consequuntur est quam quod qui excepturi quia."
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
            f"<p style='font-size: 1.1em;'>{chave}: <b style='color: #e11d48; font-size: 1.1em;'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    st.subheader("Top 10 players with the most triple doubles")
    st.markdown(
        f""" 
         <div class='center-table'>
            {offensive_data["Top 10 players with the most triple doubles"].to_html(index=False)}
         </div>
        """,
        unsafe_allow_html=True,
    )

    for chave, dado in islice(offensive_data.items(), 7, None):
        st.subheader(chave)
        st.plotly_chart(dado)

if option == "Defensive":
    st.subheader("Defensive")

    for chave, dado in islice(defensive_data.items(), 0, 4):
        st.markdown(
            f"<p style='font-size: 1.1em;'>{chave}: <b style='color: #e11d48; font-size: 1.1em;'>{dado}</b></p>",
            unsafe_allow_html=True,
        )

    st.subheader(
        "Top 10 players with the most defensive rebounds, steals and blocks per game"
    )
    st.markdown(
        f""" 
         <div class='center-table'>
            {defensive_data[
                "Top 10 players with the most defensive rebounds, steals and blocks per game"
            ].to_html(index=False)}
         </div>
        """,
        unsafe_allow_html=True,
    )

    for chave, dado in islice(defensive_data.items(), 5, None):
        st.subheader(chave)
        st.plotly_chart(dado)

if option == "Specific":
    st.subheader("Specific")

    player_selected = st.text_input(
        "Insert the full name of the player you wish to see",
        placeholder="Joel Embiid",
    )

    if player_selected == "":
        player_selected_data = specific_player_data("Joel Embiid")
        player_selected_df = player_selected_data[0]
        player_vs_avarage_graph = player_selected_data[1]

    else:
        player_selected_data = specific_player_data(player_selected)
        player_selected_df = player_selected_data[0]
        player_vs_avarage_graph = player_selected_data[1]

    col1, col2 = st.columns(2)

    with col1:
        st.header(player_selected_df["PName"].to_string(index=False))
        st.markdown(
            f"""
            <ul>
                <li>
                    <p style='font-size: 1.6em;'>Players's age: <span style='color: #4f46e5;'>{player_selected_df['Age'].to_string(index=False)}</span></p>
                </li>
                <li>
                    <p style='font-size: 1.6em;'>Player's position: <span style='color: #4f46e5;'>{player_selected_df['POS'].to_string(index=False)}</span></p>
                </li>
                <li>
                    <p style='font-size: 1.6em;'>Players's DD2: <span style='color: #4f46e5;'>{player_selected_df['DD2'].to_string(index=False)}</span></p>
                </li>
                <li>
                    <p style='font-size: 1.6em;'>Player's TD3: <span style='color: #4f46e5;'>{player_selected_df['TD3'].to_string(index=False)}</span></p>
                </li>
                <li>
                    <p style='font-size: 1.6em;'>Player's avarage points per game: <span style='color: #4f46e5;'>{player_selected_df['PTSperGP'].to_string(index=False)}</span></p>
                </li>
                <li>
                    <p style='font-size: 1.6em;'>Player's total defensive actions: <span style='color: #4f46e5;'>{player_selected_df['DEF_ACTIONS'].to_string(index=False)}</span></p>
                </li>
            </ul>""",
            unsafe_allow_html=True,
        )

    with col2:
        st.header(player_selected_df["team_name"].to_string(index=False))
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img src={player_selected_df["team_img"].to_string(index=False)} alt="Image" style="max-width: 65%;">
            </div>
            """,
            unsafe_allow_html=True,
        )

    data_col1, data_col2 = st.columns(2)

    for i in range(int(len(data_to_plot) / 2)):
        with data_col1:
            st.markdown(
                f"<p style='font-size: 1.1em;'>{full_name_col[data_to_plot[i]]}: <b style='color: #e11d48; font-size: 1.1em;'>{player_selected_df[data_to_plot[i]].to_string(index=False)}</b></p>",
                unsafe_allow_html=True,
            )

    for j in range(int(len(data_to_plot) / 2), int(len(data_to_plot))):
        with data_col2:
            st.markdown(
                f"<p style='font-size: 1.1em;'>{full_name_col[data_to_plot[j]]}: <b style='color: #e11d48; font-size: 1.1em;'>{player_selected_df[data_to_plot[j]].to_string(index=False)}</b></p>",
                unsafe_allow_html=True,
            )

    st.subheader("Player stats vs avarage stats from the league")
    st.plotly_chart(player_vs_avarage_graph)
