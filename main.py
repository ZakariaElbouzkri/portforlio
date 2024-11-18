import streamlit as st
import json

from srcs import (
    about, projects, skills
)

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


MENU = {
    'About': {
        'data': load_json('data/contact_info.json'),
        'func': about,
    },
    'Skills': {
        'data': load_json('data/skills_info.json'),
        'func': skills,
    },
    'Projects': {
        'data': load_json('data/projects_info.json'),
        'func': projects,
    },
}

FULL_NAME = 'zakaria el bouzkri'
PROFILE_IMAGE_PATH = 'assets/profile.jpg'

def main():

    st.set_page_config(
        page_title=f"{FULL_NAME.capitalize()} Portfolio",
        page_icon=":computer:"
    )


    # Sidebar Navigation
    st.sidebar.title(f'{FULL_NAME.upper()}')
    st.sidebar.image(
        PROFILE_IMAGE_PATH,
        caption=FULL_NAME.capitalize(),
        use_container_width=True
    )

    choice = st.sidebar.radio(
        "menu",
        [item for item in MENU]
    )

    func = MENU[choice]['func']
    data = MENU[choice]['data']

    func(data)

if __name__ == "__main__":
    main()
