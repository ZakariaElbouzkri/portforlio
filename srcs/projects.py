import streamlit as st

def projects(projects_data):
    st.title("Projects")
    for project in projects_data['projects']:
        with st.expander(project["name"]):
            st.write(f"**Description:** {project['description']}")
            st.write("**Technologies:**")
            st.write(", ".join(project['technologies']))
            st.write("**Key Highlights:**")
            for highlight in project['highlights']:
                st.write(f"- {highlight}")

