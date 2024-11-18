import streamlit as st


def skills(skills_data):
    st.title("🚀 Technical Skills")

    for skill_category in skills_data['skills']:
        st.subheader(f"{skill_category['category']}")

        for skill in skill_category['skills']:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.markdown(f"**{skill['icon']} {skill['name']}**")

            with col2:
                st.markdown(f"{skill['description']}")

        st.markdown("---")
