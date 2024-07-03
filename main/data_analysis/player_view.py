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
        }
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

top_10_dreb_stl_blk_pg_table = data_merged[
    ["PName", "DREBperGP", "STLperGP", "BLKperGP"]
].head(10)
top_10_dreb_stl_blk_pg_table.rename(
    columns={"PName": "Player name"}, inplace=True
)
top_10_dreb_stl_blk_pg_table.sort_values(
    by=["DREBperGP", "STLperGP", "BLKperGP"], ascending=False
)

top_10_dreb_stl_blk_pg_3d_3graph = (
    px.scatter_3d(
        data_frame=top_10_dreb_stl_blk_pg_table,
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
    )
)


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

# ### Como estão distribuidos os jogadores em termos de roubos de bola e rebotes proporcional ao número de jogos

stl_reb_min_graph = (
    px.scatter(
        data_frame=data_merged,
        x="STL",
        y="DREB",
        size="Min",
        hover_data="PName",
        template="plotly_dark",
        color="PName",
        labels={
            "STL": "Steals made",
            "DREB": "Defensive rebounds made",
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
    "Top 10 players with the most defensive rebounds, steals and blocks per game in a 3d graph": top_10_dreb_stl_blk_pg_3d_3graph,
    "Distributions of blocks and personal fouls, with size proportional to minutes played by each player": blk_pf_min_graph,
    "Distributions of steals and defensive rebounds, with size proportional to minutes played by each player": stl_reb_min_graph,
}

data_to_plot = [
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


def specific_player_data(selected_player):
    return data_merged[data_merged["PName"].str.lower() == selected_player.lower()]


def create_player_vs_avarage_graph(player_df, data_to_plot):
    mean_values = data_merged[data_to_plot].mean()

    df_means = (
        pd.DataFrame(mean_values, columns=["Mean"])
        .reset_index()
        .rename(columns={"index": "Stats"})
    )
    df_means = df_means.set_index("Stats").transpose()

    df_means["PName"] = "Avarege"

    player_vs_avarage = pd.concat([player_df, df_means], ignore_index=True)

    player_vs_avarage_long = player_vs_avarage.melt(
        id_vars=["PName"], value_vars=data_to_plot, var_name="Stats", value_name="Mean"
    )

    player_vs_avarage_graph = px.bar(
        player_vs_avarage_long,
        x="Stats",
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
