from data_analysis.__init__ import data_merged, px, pd

# # Perguntas - Visão de posições
#

# ## Ataque
#

# ### Quantos jogadores há em cada posição
#

num_players_pos_table = data_merged["POS"].value_counts().reset_index()
num_players_pos_table.rename(
    columns={"POS": "Position", "count": "Count"}, inplace=True
)

# ### Como está a distribuição de pontos em cada posição (em barra)
#

pts_pos_graph = px.bar(
    data_frame=data_merged,
    x="POS",
    y="PTS",
    color="POS",
    template="plotly_dark",
    hover_data=["POS", "PName", "PTS"],
    labels={"POS": "Position", "PTS": "Points"},
).update_layout(showlegend=False)

# ### Distribuição de pontos por jogo em cada posição (em caixa)
#

pts_gp_pos_graph = px.box(
    data_frame=data_merged,
    x="POS",
    y="PTSperGP",
    template="plotly_dark",
    color="POS",
    labels={"POS": "Position", "PTSperGP": "Points per game"},
).update_layout(showlegend=False)

# ### Como estão distribuidas as médias de bolas de 3, assitências e lances livres em cada posição (em tabela e gráfico de dispersão)
#

efficiency_3_st_ftm_table = data_merged[["POS", "3PM", "AST", "FTM"]]

efficiency_3_st_ftm_graph = px.scatter(
    data_frame=data_merged,
    x="3PM",
    y="AST",
    size="FTM",
    color="POS",
    hover_data=["POS", "PName"],
    labels={
        "POS": "Position",
        "3PM": "3 pointers made",
        "AST": "Assists made",
        "FTM": "Free-throw mades",
    },
    template="plotly_dark",
).update_layout(showlegend=False)

# ### Como estão distruíbuidas as bolas de 3 convertidas de acordo com as posições (em caixa)
#

efficiency_3_pos_graph = px.box(
    data_frame=data_merged,
    x="POS",
    y="3P%",
    color="POS",
    labels={
        "3P%": "3 pointers eficiency",
        "POS": "Positions",
    },
    template="plotly_dark",
).update_layout(showlegend=False)

offensive_data = {
    "Number of player per positions": num_players_pos_table,
    "Points per each position": pts_pos_graph,
    "Points per game by each position": pts_gp_pos_graph,
    "Distribution of 3 pointers, assists, and free throws averages by position": efficiency_3_st_ftm_graph,
    "Distribution of 3 pointers percentage by position": efficiency_3_pos_graph,
}

# ## Defesa
#

# ### Como estão distribuídas as médias de bloqueios, roubos de bola, rebote em cada posição (em dispersão)
#

blk_stl_dreb_pos_graph = px.scatter(
    data_frame=data_merged,
    x="BLK",
    y="STL",
    size="DREB",
    color="POS",
    labels={
        "BLK": "Blocks",
        "STL": "Steals",
        "DREB": "Defensive rebound",
        "POS": "Position",
    },
    hover_data="PName",
    template="plotly_dark",
).update_layout(showlegend=False)

# ### Como estão distruibuidos os roubos de bola por posição (em caixa)
#

stl_pos_graph = px.box(
    data_frame=data_merged,
    x="POS",
    y="STL",
    color="POS",
    labels={
        "STL": "Steals",
        "POS": "Positions",
    },
    template="plotly_dark",
).update_layout(showlegend=False)

# ### Como estão distribuidas as ações defensivas por posição (em caixa)
#

defactions_pos_graph = px.box(
    data_frame=data_merged,
    x="POS",
    y="DEF_ACTIONS",
    color="POS",
    labels={
        "DEF_ACTIONS": "Defensive actions",
        "POS": "Positions",
    },
    template="plotly_dark",
).update_layout(showlegend=False)

# ### Como estão distribuidas as médias de bloqueios, roubos de bola e rebote em cada posição (em tabela e em dispersão 3D)
#

blk_stl_dreb_pos_3d_graph = px.scatter_3d(
    data_merged,
    x="BLK",
    y="STL",
    z="DREB",
    color="POS",
    size="DEF_ACTIONS",
    opacity=0.6,
    template="plotly_dark",
    hover_data='PName',
    labels={
        "BLK": "Blocks",
        "STL": "Steals",
        "DREB": "Defensive rebounds",
        "POS": "Position",
        "DEF_ACTIONS": "Defensive actions",
    },
)

defensive_data = {
    'Distribution of blocks, steals, and defensive rebounds averages per position': blk_stl_dreb_pos_graph,
    'Blocks percentage vs steals vs percentage per position - 3D': blk_stl_dreb_pos_3d_graph,
    'Distribution steals per position': stl_pos_graph,
    'Distribution defensive actions per position': defactions_pos_graph
}