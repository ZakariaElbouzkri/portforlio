import streamlit as st

def about(contact_data):
    # Professional Summary
    st.title("👨‍💻 About Me")
    st.markdown(contact_data['about']['professional_summary'])

    # Professional Highlights
    st.subheader("🌟 Professional Highlights")
    for highlight in contact_data['about']['professional_highlights']:
        st.markdown(f"- {highlight}")

    # Education Section
    st.subheader("🎓 Education")
    education = contact_data['about']['education']
    st.markdown(f"""
    **{education['institution']}** | {education['location']}
    - {education['program']}
    """)
    for highlight in education['highlights']:
        st.markdown(f"- {highlight}")


    # Contact Information
    st.title("📞 Contact Information")
    personal = contact_data['personal']
    social = contact_data['social_links']

    contact_info = [
        {"icon": "✉️", "label": "Email", "value": personal['email']},
        {"icon": "📱", "label": "Phone", "value": personal['phone']},
        {"icon": "📍", "label": "Location", "value": personal['location']}
    ]

    for info in contact_info:
        st.markdown(f"{info['icon']} **{info['label']}:** {info['value']}")
