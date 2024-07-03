import streamlit as st
from st_pages import Page, show_pages, add_page_title, hide_pages

st.set_page_config(
    page_title="NBA 2023 stats",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "## Projeto de dados da temporada 2022-2023 da NBA.",
    },
)

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

st.write("Quer me conhcer? [Clique aqui!](https://github.com/joas005)")
st.title("Dashboard geral")

