import pandas as pd
import plotly.express as px

pd.set_option("display.max_colwidth", 1000)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 100)

data_raw = pd.read_csv("./main/data/nba_player_stats.csv")

# # Conhecendo os dados
#

# ## Limpando os valores nulos
#

# ### Preenchendo com valores conforme pesquisa na internet
#

data_raw.iloc[534, 1] = "PG"
data_raw.iloc[535, 1] = "SF"
data_raw.iloc[536, 1] = "SG"
data_raw.iloc[537, 1] = "PF"
data_raw.iloc[538, 1] = "SF"

# # Preparando os dados
#

# ### Obtendo as colunas de 2 pontos
#

data = data_raw.copy()

data["2PM"] = data["FGM"] - data["3PM"]
data["2PA"] = data["FGA"] - data["3PA"]
data["2Pperc"] = round(data["2PM"] / data["2PA"] * 100, 2)
data.rename(columns={"2Pperc": "2P%"}, inplace=True)

# ### Obtendo as estatíscas por jogos
#


def per_game(df, colmuns: list):
    aux = pd.DataFrame()
    for i in colmuns:
        aux[f"{i}perGP"] = round(df[i] / df["GP"], 2)

    aux["PName"] = df["PName"]
    return aux


# +
data_per_game = per_game(
    data,
    [
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
    ],
)

# -

data_merged = data.merge(data_per_game, how="left", left_on="PName", right_on="PName")

# ### Adicionando colunas de logos e nomes
#

teams_names_map = {
    "BOS": "Boston Celtics",
    "PHI": "Philadelphia 76ers",
    "DAL": "Dallas Mavericks",
    "OKC": "Oklahoma City Thunder",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NYK": "New York Knicks",
    "CLE": "Cleveland Cavaliers",
    "ATL": "Atlanta Hawks",
    "CHI": "Chicago Bulls",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "TOR": "Toronto Raptors",
    "UTA": "Utah Jazz",
    "DEN": "Denver Nuggets",
    "HOU": "Houston Rockets",
    "GSW": "Golden State Warriors",
    "BKN": "Brooklyn Nets",
    "MEM": "Memphis Grizzlies",
    "LAL": "Los Angeles Lakers",
    "NOP": "New Orleans Pelicans",
    "MIA": "Miami Heat",
    "WAS": "Washington Wizards",
    "ORL": "Orlando Magic",
    "PHX": "Phoenix Suns",
    "SAS": "San Antonio Spurs",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "CHA": "Charlotte Hornets",
    "DET": "Detroit Pistons",
}

teams_logo_map = {
    "BOS": "https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg",
    "PHI": "https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg",
    "DAL": "https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg",
    "OKC": "https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg",
    "MIL": "https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg",
    "MIN": "https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg",
    "NYK": "https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg",
    "CLE": "https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg",
    "ATL": "https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg",
    "CHI": "https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg",
    "POR": "https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg",
    "SAC": "https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg",
    "TOR": "https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg",
    "UTA": "https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg",
    "DEN": "https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg",
    "HOU": "https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg",
    "GSW": "https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg",
    "BKN": "https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg",
    "MEM": "https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg",
    "LAL": "https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg",
    "NOP": "https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg",
    "MIA": "https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg",
    "WAS": "https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg",
    "ORL": "https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg",
    "PHX": "https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg",
    "SAS": "https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg",
    "IND": "https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg",
    "LAC": "https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg",
    "CHA": "https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg",
    "DET": "https://cdn.nba.com/logos/nba/1610612765/global/L/logo.svg",
}

data_merged["team_img"] = data_merged["Team"].map(teams_logo_map)
data_merged["team_name"] = data_merged["Team"].map(teams_names_map)

# ### Dataframe agrupado por time
#

df_teams = (
    data_merged[
        [
            "Team",
            "PTS",
            "3PM",
            "3PA",
            "3P%",
            "FGM",
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
            "2PM",
            "2PA",
            "2P%",
        ]
    ]
    .groupby("Team")
    .agg(
        {
            "PTS": "sum",
            "3PM": "sum",
            "3PA": "sum",
            "3P%": "mean",
            "FGM": "sum",
            "FTM": "sum",
            "FTA": "sum",
            "FT%": "mean",
            "OREB": "sum",
            "DREB": "sum",
            "REB": "sum",
            "AST": "sum",
            "TOV": "sum",
            "STL": "sum",
            "BLK": "sum",
            "PF": "sum",
            "2PM": "sum",
            "2PA": "sum",
            "2P%": "mean",
        }
    )
    .sort_values(by="PTS", ascending=False)
    .round(2)
    .reset_index()
)

df_teams["team_image"] = df_teams["Team"].map(teams_logo_map)
df_teams["team_name"] = df_teams["Team"].map(teams_names_map)

# ### Criando colunas de ações defensivas ( DREB + REB + STL )
#

df_teams["DEF_ACTIONS"] = df_teams["DREB"] + df_teams["REB"] + df_teams["STL"]
data_merged["DEF_ACTIONS"] = (
    data_merged["DREB"] + data_merged["REB"] + data_merged["STL"]
)
