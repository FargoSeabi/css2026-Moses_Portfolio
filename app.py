import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Moses Seabi | Portfolio",
    layout="wide",
    page_icon="👨‍💻"
)

# Load images (replace with your own file paths)
try:
    profile_pic = Image.open("profile-pic.jpg")  # Your profile picture
    python_logo = Image.open("python-pic.png")
    js_logo = Image.open("pic.png")
    html_logo = Image.open("html.png")
    css_logo = Image.open("css.png")
    git_logo = Image.open("git.png")
    sql_logo = Image.open("mysql.png")
    
except:
    st.warning("Images not found. Make sure your image files are in the same folder.")

# HEADER
col1, col2 = st.columns([1, 3])
with col1:
    if 'profile_pic' in locals():
        st.image(profile_pic, width=150)
with col2:
    st.title("👋 Moses Seabi")
    st.subheader("Aspiring Software / Web Developer")
    st.write("""
    Welcome to my **Streamlit Portfolio**!
    Explore my skills, projects, and contact info.
    """)

st.markdown("---")

# ABOUT ME
st.header("About Me")
st.write("""
I am a motivated and curious developer with a passion for
building **clean, efficient and user-friendly applications**.

I enjoy learning new technologies and applying them to solve real-world problems.
""")

st.markdown("---")

# SKILLS
st.header("Skills")

cols = st.columns(4)

skills = [
     {"name": "Python", "image": python_logo},
    {"name": "JavaScript", "image": js_logo},
    {"name": "HTML", "image": html_logo},
    {"name": "CSS", "image": css_logo},
    {"name": "Git & GitHub", "image": git_logo},
    {"name": "Basic SQL", "image": sql_logo},
]

for i, skill in enumerate(skills):
    col = cols[i % 4]
    if 'image' in skill and skill["image"] is not None:
        col.image(skill["image"], width=60)
    col.write(f"**{skill['name']}**")

st.markdown("---")

# PROJECTS
st.header("Projects")

projects = [
    {
        "name": "MosesSeabi-portfolio-website",
        "description": "Personal portfolio website showcasing my projects and experience.",
        "link": "https://github.com/FargoSeabi/MosesSeabi-portfolio-website"
    },
    {
        "name": "RootsToRealitiesApp",
        "description": "Platform connecting local communities with sustainable opportunities.",
        "link": "https://github.com/FargoSeabi/RootsToRealitiesApp"
    },
    {
        "name": "Thinkable-LMS",
        "description": "Intelligent Learning Management System for neurodiverse learners.",
        "link": "https://github.com/FargoSeabi/Thinkable-LMS"
    },
    {
        "name": "netflix",
        "description": "Netflix UI clone demonstrating responsive design and interactivity.",
        "link": "https://github.com/FargoSeabi/netflix"
    }
]

for project in projects:
    st.subheader(f"📂 {project['name']}")
    st.write(project["description"])
    st.write(f"🔗 GitHub: [Repo Link]({project['link']})")

st.markdown("---")

# CONTACT
st.header("Contact Me 📫")
col1, col2 = st.columns(2)

with col1:
    st.write("""
    📧 **Email:** moses.seabi@example.com  
    📍 **Location:** South Africa  
    💻 **GitHub:** [FargoSeabi](https://github.com/FargoSeabi)  
    """)

with col2:
    st.write("""
Let's connect and collaborate! I am open to internships, projects and junior developer opportunities.
""")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
