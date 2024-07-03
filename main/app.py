import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="NBA 2023 stats",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "## Projeto de dados da temporada 2022-2023 da NBA.",
    },
    page_icon="main/static/favicon.ico",
)

with open("main/static/style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

show_pages(
    [
        Page("main/app.py", "Homepage", "💻"),
        Page(
            "main/pages/team_view.py",
            "Teams",
            "👥",
        ),
        Page(
            "main/pages/pos_view.py",
            "Postions",
            "1️⃣",
        ),
        Page(
            "main/pages/player_view.py",
            "Players",
            "⛹️‍♂️",
        ),
    ]
)


col1, col2 = st.columns(2)

with col1:
    st.write("Want to know more about me? [Click here!](https://github.com/joas005)")
    st.title("NBA 2023 stats analysis")
    st.write(
        "Explore the game beyond the scores. Dive into the heart of NBA action with our interactive data visualizations. From player performance trends to team statistics and game analyses, uncover the stories behind every shot, pass, and dunk. Whether you're a die-hard fan or a curious analyst, our tools empower you to see the game in new dimensions. Get started now and experience the NBA like never before!"
    )

with col2:
    st.markdown(
        f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img src="https://blog.bwin.pt/wp-content/uploads/2021/10/Lebron-James-o-King-da-NBA.png" alt="Image" style="max-width: 60%;">
            </div>
            """,
        unsafe_allow_html=True,
    )

st.header("About the data")

st.write(
    "This project pulls up the vibrant culture of NBA basketball with the dataset NBA Players Stats (2023 Season) skillfully gathered by AmirHossein Mirzaei. This extensive database allows to evaluate metrics of players of NBA throughout 2023 that depict general capabilities of the player and the team, certain tendencies within the league."
)

st.write(
    "It can therefore be concluded that the kind providence rendered by AmirHossein Mirzaei in maintaining parsimonious data whereby information is complete and accurate, makes this dataset not only informative but also credible for a host of analytic uses. No matter whether you are a machine learning engineer, working at a sports newspaper, or just love basketball, expand your knowledge on basketball with this dataset on Kaggle: [NBA Players Stats 2023 Season](https://www.kaggle.com/datasets/amirhosseinmirzaie/nba-players-stats2023-season)"
)

with st.container():
    st.header("About the project")

    st.subheader("Team-Based Insights:")
    st.write(
        "Investigates which teams were most successful in various statistical measures during the 2023 season. Find out the team that scored more points, made more blocks, assists and other set records. Hence, our bar-plots using Plotly Express show these team performances at a glance, summarizing the achievement of the teams at different occasions in the season."
    )

    st.subheader("Position-Based Insights:")
    st.write(
        "Explore the distribution of the players and their relations to the positions in NBA. For each of the mentioned positions, how many players do they have? How many points were produced by position? In addition to that, they should be able to analyze defensive actions inclusive of blocks and steals accordantly to the position they play. The positional dynamics in the league are further explored in the following insights which are embedded in the interactive charts using Plotly Express."
    )

    st.subheader("Player-Based Insights:")
    st.write(
        "Acquire a broad view of certain statistics of the players in each team in the league. We will look at each of the players by their shooting, passing, and other general attributes in order to appreciate them as worthy components of the respective teams. By using Pandas libraries for data manipulation and Streamlit for the interactive dashboard, the work includes player profiles and the real-time experience of different trends in players’ performances to perform the analysis of the specific player’s contribution and his/her trends during the match."
    )

    st.subheader("Project Goals:")
    st.write(
        "The objective of this project is to perform data analysis using Python programming language using Panda data manipulation library, Plotly express for data visualization and Streamlit for data interactive dashboards. This paper aims hence to advance our knowledge on basketball and the field of data analytics through data mining of the “NBA Players Stats (2023 Season)” dataset."
    )
