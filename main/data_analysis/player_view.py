from data_analysis.__init__ import data_merged, px, pd

# # Perguntas - Visão de Jogadores
#

# ## Ataque
#

# ### Quantos jogadores há na liga
#

num_players = data_merged.shape[0]

# ### Qual é o jogador com maior número de pontos
#

most_pts = (
    data_merged.sort_values(by="PTS", ascending=False)
    .iloc[0][["PName", "PTS"]]
    .to_string(index=False)
)

# ### Qual é o jogador com maior número de bolas de 3
#

most_3_pts = (
    data_merged.sort_values(by="3PM", ascending=False)
    .iloc[0][["PName", "3PM"]]
    .to_string(index=False)
)

# ### Qual o jogador com maior número de cestas de quadras
#

most_fg = (
    data_merged.sort_values(by="FGM", ascending=False)
    .iloc[0][["PName", "FGM"]]
    .to_string(index=False)
)

# ### Qual o jogador com maior número de lances livres arremessados
#

most_fta = (
    data_merged.sort_values(by="FTA", ascending=False)
    .iloc[0][["PName", "FGA"]]
    .to_string(index=False)
)

# ### Qual é o jogador com maior número de assistências
#

most_ast = (
    data_merged.sort_values(by="AST", ascending=False)
    .iloc[0][["PName", "AST"]]
    .to_string(index=False)
)

# ### Como estão distribuidos os jogadores em termos de bolas de 3 feitas, volume de bolas de 2 pontos feitas e lances livres (em tabela)
#

ft_3_2_mean_table = data_merged[["PName", "team_name", "3P%", "FG%", "FT%"]].head()
ft_3_2_mean_table.rename(
    columns={"team_name": "Team name", "PName": "Player name"}, inplace=True
)


# ### Como estão distribuidos os jogadores em termos de volume bolas de 3 feitas, volume de bolas de 2 pontos feitas e lances livres convertidos (em dipersão 3d)
#

ft_3_2_made_3d_graph = (
    px.scatter_3d(
        data_frame=data_merged,
        x="3PM",
        y="2PM",
        z="FTM",
        hover_data="PName",
        template="plotly_dark",
        color="PName",
        labels={
            "3PM": "3 points made",
            "2PM": "2 points made",
            "FTM": "Free throws made",
            "PName": "Player name",
        },
    )
    .update_traces(marker=dict(line=dict(width=1, color="DarkSlateGrey")))
    .update_layout(showlegend=False)
)

# ### Como estão distribuidos os jogadores em termos de assitências feitas e pontos feitas em relação aos minutos em quadra (em dipersão)
#

ast_pts_min_graph = (
    px.scatter(
        data_frame=data_merged,
        x="AST",
        y="PTS",
        size="Min",
        hover_data="PName",
        template="plotly_dark",
        color="PName",
        height=700,
        labels={
            "AST": "Assists made",
            "PTS": "Points made",
            "Min": "Minutes played",
            "PName": "Player name",
        },
    )
    .update_traces(marker=dict(line=dict(width=1, color="DarkSlateGrey")))
    .update_layout(showlegend=False)
)

# ### Quais foram os 10 jogadores com mais triplos duplos

top_10_td3 = (
    data_merged[["PName", "team_name", "TD3"]]
    .sort_values(by="TD3", ascending=False)
    .head(10)
)
top_10_td3.rename(
    columns={"team_name": "Team name", "PName": "Player name", "TD3": "Number of TD3"},
    inplace=True,
)


offensive_data = {
    "Number of players on the league": num_players,
    "Player with the most points": most_pts,
    "Player with the most 3 pointers": most_3_pts,
    "Player with the most field goals made": most_fg,
    "Player with the most field goals attempted": most_fta,
    "Player with the most assists": most_ast,
    "Top 10 players with the most triple doubles": top_10_td3,
    "Distribution of assists vs poits with size proportional to minutes played by each player": ast_pts_min_graph,
    "Players 3 pointers, 2 pointers and free throws - 3D": ft_3_2_made_3d_graph,
}

# ## Defesa

# ### Quantos jogadores há na liga
#

data_merged.shape[0]

# ### Qual o jogador com maior número de rebotes defensivos

most_dreb = (
    data_merged.sort_values(by="DREB", ascending=False)
    .iloc[0][["PName", "DREB"]]
    .to_string(index=False)
)

# ### Qual o jogador com maior número de roubos

most_stl = (
    data_merged.sort_values(by="STL", ascending=False)
    .iloc[0][["PName", "STL"]]
    .to_string(index=False)
)

# ### Qual o jogador com maior número de bloqueios

most_blk = (
    data_merged.sort_values(by="BLK", ascending=False)
    .iloc[0][["PName", "BLK"]]
    .to_string(index=False)
)

# ### Qual o jogador com maior número de faltas pessoais

most_pf = (
    data_merged.sort_values(by="PF", ascending=False)
    .iloc[0][["PName", "PF"]]
    .to_string(index=False)
)

# ### Qual é a média de rebotes defensivos, roubos de bola e bloqueio dos jogadores por jogo

dreb_stl_blk_pg_table = data_merged[
    ["PName", "DREBperGP", "STLperGP", "BLKperGP", "DEF_ACTIONS"]
]
dreb_stl_blk_pg_table.rename(columns={"PName": "Player name"}, inplace=True)
dreb_stl_blk_pg_table.sort_values(by="DEF_ACTIONS", ascending=False)
dreb_stl_blk_pg_table.head(50)

dreb_stl_blk_pg_3d_3graph = px.scatter_3d(
    data_frame=dreb_stl_blk_pg_table,
    x="DREBperGP",
    y="STLperGP",
    z="BLKperGP",
    hover_data="Player name",
    template="plotly_dark",
    color="Player name",
    labels={
        "BLK": "Blocks made",
        "STLperGP": "Steals per game",
        "DREBperGP": "Defensive rebounds per game",
        "BLKperGP": "Blocks per game",
    },
).update_traces(marker=dict(line=dict(width=1, color="DarkSlateGrey")))


# ### Como estão distribuidos os jogadores em termos de bloqueios e faltas pessoais proporcional à minutagem do jogador

blk_pf_min_graph = (
    px.scatter(
        data_frame=data_merged,
        x="BLK",
        y="PF",
        size="Min",
        hover_data="PName",
        template="plotly_dark",
        color="PName",
        labels={
            "BLK": "Blocks made",
            "PTS": "Personal fouls made",
            "Min": "Minutes played",
            "PName": "Player name",
        },
    )
    .update_traces(marker=dict(line=dict(width=1, color="DarkSlateGrey")))
    .update_layout(showlegend=False)
)

defensive_data = {
    "Player with the most defensive rebounds": most_dreb,
    "Player with the most steals": most_stl,
    "Player with the most blocks": most_blk,
    "Player with the most personal fouls": most_pf,
    "Players with the most defensive rebounds, steals and blocks per game in a 3d graph": dreb_stl_blk_pg_3d_3graph,
    "Distributions of blocks and personal fouls, with size proportional to minutes played by each player": blk_pf_min_graph,
}

data_to_plot = [
    "Age",
    "GP",
    "W",
    "L",
    "Min",
    "PTS",
    "FGM",
    "FGA",
    "FG%",
    "3PM",
    "3PA",
    "3P%",
    "FTM",
    "FTA",
    "FT%",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "TOV",
    "STL",
    "BLK",
    "PF",
    "FP",
    "2PM",
    "2PA",
    "2P%",
]

full_name_stats_map = {
    "Age": "Age",
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

full_name_stats_list = []
for chave, valor in full_name_stats_map.items():
    full_name_stats_list.append(valor)


def specific_player_data(selected_player):
    return data_merged[data_merged["PName"].str.lower() == selected_player.lower()]


def create_player_vs_avarage_graph(player_df, data_selected):
    keys_selected = []
    for item in data_selected:
        for chave, valor in full_name_stats_map.items():
            if valor == item:
                keys_selected.append(chave)

    mean_values = data_merged[keys_selected].mean()

    df_means = (
        pd.DataFrame(mean_values, columns=["Mean"])
        .reset_index()
        .rename(columns={"index": "Stats"})
    )
    df_means = df_means.set_index("Stats").transpose()

    df_means["PName"] = "Avarege"

    player_vs_avarage = pd.concat([player_df, df_means], ignore_index=True)

    player_vs_avarage_long = player_vs_avarage.melt(
        id_vars=["PName"], value_vars=keys_selected, var_name="Stats", value_name="Mean"
    )

    player_vs_avarage_long["Stat name"] = player_vs_avarage_long["Stats"].map(full_name_stats_map)

    player_vs_avarage_graph = px.bar(
        player_vs_avarage_long,
        x="Stat name",
        y="Mean",
        color="PName",
        barmode="group",
        hover_data="Stats",
        labels={
            "PName": "Player",
            "Mean": "Number",
        },
        template="plotly_dark",
        height=700,
    )

    return player_vs_avarage_graph
