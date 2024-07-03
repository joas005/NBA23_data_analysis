from data_analysis.__init__ import df_teams, data_merged, px

# # Perguntas - Visão de times
#

# ## Ataque
#

# ### Qual o total de times de times
#

number_teams = df_teams.shape[0]

# ### QUais são todos os times
#

all_teams = list(df_teams["team_name"].unique())

# ### Qual o time com mais pontos
#

most_points = (
    df_teams.sort_values(by="PTS", ascending=False)
    .iloc[0][["team_name", "PTS"]]
    .to_string(index=False)
)

# ### Time com mais bolas de 3 pontos
#

most_3_pointers = (
    df_teams.sort_values(by="3PM", ascending=False)
    .iloc[0][["team_name", "3PM"]]
    .to_string(index=False)
)

# ### Time com mais cestas de quadra
#

most_fg = (
    df_teams.sort_values(by="FGM", ascending=False)
    .iloc[0][["team_name", "FGM"]]
    .to_string(index=False)
)

# ### Time com mais turn-overs
#

most_tov = (
    df_teams.sort_values(by="TOV", ascending=False)
    .iloc[0][["team_name", "TOV"]]
    .to_string(index=False)
)

# ### Como está a porcentagem de bolas de 3 e de lances de livres
#

mean_3_ft_table = df_teams[["team_name", "3P%", "FT%"]].head()
mean_3_ft_table.rename(columns={"team_name": "Team name"}, inplace=True)

# ### Como está o rankeamento total de pontos dos times
#

top_5_scorers_table = df_teams[["team_name", "PTS"]].head()
top_5_scorers_table.rename(columns={"team_name": "Team name"}, inplace=True)

points_graph = px.bar(
    data_frame=df_teams,
    x="PTS",
    y="Team",
    orientation="h",
    color="Team",
    template="plotly_dark",
    height=800,
    width=800,
).update_layout(xaxis_title="Points made", showlegend=False)
# ### Quais são os times que mais tiveram mais volumes de 3 e quais tiveram em infiltrações e bola de meia distância
#

most_3_2_graph = (
    px.scatter(
        data_frame=df_teams,
        x="2PM",
        y="3PM",
        color="Team",
        template="plotly_dark",
        opacity=0.6,
    )
    .update_traces(marker_size=30)
    .update_layout(xaxis_title="3 points made", yaxis_title="2 points made")
)

# ### Quais são os times que mais tiveram mais efetividade em bolas de 3 pontos e quais tiveram em infiltrações e bola de meia distância
#

efficiency_3_2_graph = (
    px.scatter(
        data_frame=df_teams,
        x="2P%",
        y="3P%",
        color="Team",
        template="plotly_dark",
        opacity=0.6,
        hover_data="Team",
    )
    .update_traces(marker_size=30)
    .update_layout(xaxis_title="3 points mean", yaxis_title="2 points mean")
)

offensive_data = {
    "Team with the most points": most_points,
    "Team with the most 3 pointers": most_3_pointers,
    "Team with the most field goals": most_fg,
    "Team with the most turn-overs": most_tov,
    "Teams with best 3 pointers and free throws efficiency": mean_3_ft_table,
    "Top 5 scorers": top_5_scorers_table,
    "Points per team": points_graph,
    "Distribution of 3 pointers and 2 pointers per team": most_3_2_graph,
    "Distribution of 3 pointers and 2 pointers efficiency per team": efficiency_3_2_graph,
}

# ## Defesa
#

# ### Time com mais rebotes defensivos
#

most_dreb = (
    df_teams.sort_values(by="DREB", ascending=False)
    .iloc[0][["team_name", "DREB"]]
    .to_string(index=False)
)

# ### Time com mais bloqueios
#

most_blk = (
    df_teams.sort_values(by="BLK", ascending=False)
    .iloc[0][["team_name", "BLK"]]
    .to_string(index=False)
)

# ### Time com mais roubos de bola
#

most_stl = (
    df_teams.sort_values(by="STL", ascending=False)
    .iloc[0][["team_name", "STL"]]
    .to_string(index=False)
)

# ### Time com mais faltas pessoais
#

most_pf = (
    df_teams.sort_values(by="PF", ascending=False)
    .iloc[0][["team_name", "PF"]]
    .to_string(index=False)
)

# ### Como está o número de rebotes defensivos, roubos de bola e bloqueios por time (em tabela)
#

blk_stl_dreb_table = df_teams[["team_name", "BLK", "STL", "DREB"]].head()
blk_stl_dreb_table.rename(columns={"team_name": "Team name"}, inplace=True)

# ### Como está o rankeamento total de atos defensivos dos time (em grafico)
#

df_teams = df_teams.sort_values(by="DEF_ACTIONS", ascending=False)

most_defactions_graph = px.bar(
    data_frame=df_teams,
    x="DEF_ACTIONS",
    y="Team",
    color="Team",
    template="plotly_dark",
    height=800,
    width=800,
).update_layout(
    xaxis_title="Defensive actions",
    showlegend=False,
)

# ### Quais times mais tiveram roubos de bola e quais tiveram mais rebotes defensivos (em dispersão)
#

most_stl_dreb_graph = (
    px.scatter(
        data_frame=df_teams,
        x="STL",
        y="DREB",
        color="Team",
        template="plotly_dark",
        opacity=0.6,
        hover_data="Team",
    )
    .update_traces(marker_size=30)
    .update_layout(xaxis_title="Steals", yaxis_title="Defensive rebounds")
)

# ### Quais times tiveram mais bloqueios e quias tiveram mais faltas pessoais (em dispersão)
#

most_blk_pf_graph = (
    px.scatter(
        data_frame=df_teams,
        x="BLK",
        y="PF",
        color="Team",
        template="plotly_dark",
        opacity=0.6,
        hover_data="Team",
    )
    .update_traces(marker_size=30)
    .update_layout(xaxis_title="Blocks", yaxis_title="Personal fouls")
)

defensive_data = {
    "Team with the most defensive rebounds": most_dreb,
    "Team with the most blocks": most_blk,
    "Team with the most steals": most_stl,
    "Team with the most personal fouls": most_pf,
    "Teams with the most blocks, steal and defensive rebounds": blk_stl_dreb_table,
    "Teams defensive actions": most_defactions_graph,
    "Distribution of steals and blocks per teams": most_stl_dreb_graph,
    "Distribution of blocks and personal fouls per teams": most_blk_pf_graph,
}

# ## Específicos
#

# ### Filtrando os dados por time
#


def specific_team_data(selected_team):
    df_selected_team = df_teams[df_teams["team_name"] == selected_team]
    players_selected_team = data_merged[
        data_merged["team_name"] == selected_team
    ]
    # -

    team_logo = df_selected_team["team_image"]

    # ### Quantos pontos o time fez
    #

    pts_selected_team = df_selected_team["PTS"]
    # ### Quantas assistentes o time fez
    #

    ast_selected_team = df_selected_team["AST"]

    # ### Quantos rebotes o time fez
    #

    dreb_selected_team = df_selected_team["REB"]

    # ### Quantos roubos de bola o time fez
    #

    stl_selected_team = df_selected_team["STL"]

    # ### Quantos bloqueios o time fez
    #

    blk_selected_team = df_selected_team["BLK"]

    # ### Quantos turn-overs o time concedeu
    #

    tov_selected_team = df_selected_team["TOV"]

    # ### Quais são os jogadores com mais volumes de bola de 3 vs bolas de 2, de acordo com o número de jogos jogados (em dispersão)
    #

    players_3_2_graph = px.scatter(
        data_frame=players_selected_team,
        x="3PM",
        y="2PM",
        size="GP",
        color="PName",
        template="plotly_dark",
        opacity=0.6,
        hover_data="PName",
    ).update_layout(xaxis_title="3 points made", yaxis_title="2 points made")

    # ### Quantos jogadores há em cada posição (em histograma)
    #

    count_players_pos_graph = px.histogram(
        data_frame=players_selected_team,
        x="POS",
        color="POS",
        template="plotly_dark",
        hover_data="POS",
    ).update_layout(
        showlegend=False,
        xaxis_title="Positions",
        yaxis_title="Number of players",
    )

    # ### Parcela de pontos que ficaram na mão de cada posição do time (em pizza)
    #

    pts_per_pos_graph = px.pie(
        data_frame=players_selected_team,
        values="PTS",
        names="POS",
        template="plotly_dark",
    ).update_layout(showlegend=False)

    # ### Quais jogadores de cada time tiveram mais roubos de bola e bloqueios de acordo com o número de rebote defensivos que eles pegaram (em dispersão)
    #

    players_stl_blk_graph = px.scatter(
        data_frame=players_selected_team,
        x="STL",
        y="BLK",
        size="DREB",
        color="PName",
        template="plotly_dark",
        opacity=0.6,
        hover_data="PName",
    ).update_layout(xaxis_title="Steals", yaxis_title="Blocks")

    dict_team_selected = {
        "Team logo": team_logo.to_string(index=False),
        "Team points": pts_selected_team.to_string(index=False),
        "Team assists": ast_selected_team.to_string(index=False),
        "Team defensive rebounds": dreb_selected_team.to_string(index=False),
        "Team ball steals": stl_selected_team.to_string(index=False),
        "Team blocks": blk_selected_team.to_string(index=False),
        "Team turn-overs": tov_selected_team.to_string(index=False),
        "Distribution of players 3 pointers and 2 pointers": players_3_2_graph,
        "Players per position": count_players_pos_graph,
        "Points per position": pts_per_pos_graph,
        "Distribution of steals vs blocks by each player with size porportional with defensive rebounds": players_stl_blk_graph,
    }

    return dict_team_selected
