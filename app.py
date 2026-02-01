import streamlit as st

# Page config
st.set_page_config(
    page_title="Moses Seabi | Portfolio",
    layout="centered"
)

# Header
st.title("👋 Moses Seabi")
st.subheader("Aspiring Software / Web Developer")

st.write("""
Welcome to my portfolio built with **Streamlit**.
This single-page app highlights my background, skills, and projects.
""")

st.markdown("---")

# About Me
st.header("About Me")
st.write("""
I am a motivated and curious developer with a strong interest in
building clean, efficient, and user-friendly applications.

I enjoy learning new technologies and applying them to solve real-world problems.
""")

st.markdown("---")

# Skills
st.header("Skills")

col1, col2 = st.columns(2)

with col1:
    st.write("**Programming Languages**")
    st.write("""
    - Python  
    - JavaScript  
    - HTML  
    - CSS  
    """)

with col2:
    st.write("**Tools & Technologies**")
    st.write("""
    - Streamlit  
    - Git & GitHub  
    - VS Code  
    - Basic SQL  
    """)

st.markdown("---")

# Projects
st.header("Projects")

st.subheader("Portfolio Website")
st.write("""
A personal portfolio website showcasing my background,
skills, and projects using web technologies.
""")
st.write("🔗 GitHub: https://github.com/FargoSeabi")

st.subheader("Streamlit Applications")
st.write("""
Small Python applications built using Streamlit for
learning, experimentation, and problem-solving.
""")

st.markdown("---")

# Contact
st.header("Contact")
st.write("""
📧 **Email:** moses.seabi@example.com  
📍 **Location:** South Africa  
💻 **GitHub:** https://github.com/FargoSeabi  
""")

st.write("Open to internships, collaborations, and junior developer opportunities.")
