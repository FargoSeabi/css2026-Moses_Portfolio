import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Moses Seabi | Portfolio",
    layout="wide",
    page_icon="👨‍💻"
)

# Function to safely load images
def load_image(path):
    try:
        return Image.open(path)
    except:
        return None  # Image missing, return None

# Load images
profile_pic = load_image("profile-pic.png")
python_logo = load_image("python-pic.png")
js_logo = load_image("pic.png")
html_logo = load_image("html.png")
css_logo = load_image("css.png")
git_logo = load_image("git.png")
sql_logo = load_image("mysql.png")

# HEADER
col1, col2 = st.columns([1, 3])
with col1:
    if profile_pic:
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

# EDUCATION
st.header("Education")

st.subheader("🎓 Bachelor of Science in Mathematical Sciences")
st.write("""
**University:** University of Limpopo, South Africa  
**Duration:** 2023 – Present (Expected graduation: 2026)  
**Relevant Courses:** Data Structures & Algorithms, Web Development, Databases, Artificial Intelligence, Software Engineering  
**Achievements:** Dean’s List (2023),Participated in Hackathons and Coding Competitions
""")

st.subheader("🎓 National Senior Certificate")
st.write("""
**School:** Limpopo Province  
**Duration:** 2018 – 2022  
**Highlights:**  
- Top 5% of class  
- Awarded Best Academic Performance in Class 
- Participated in provincial science and tech competitions
""")

st.markdown("---")

# EXPERIENCE & ACHIEVEMENTS
st.header("Experience & Achievements")

st.subheader("💼 Branch Leader at Geekulcha")
st.write("""
**Organization:** Geekulcha – University of Limpopo Branch  
**Role:** President
**Duration:** 2024 – Present  
**Highlights:**  
- Coordinated tech-related workshops and mentorship programs for students.  
- Led branch activities during Right to Learn campaigns, assessed by NEC member Cde Penny.  
- Promoted digital literacy and coding initiatives across campus.  
""")

st.subheader("🌍 G20 Tourism Hackathon Participant")
st.write("""
**Event:** G20 Tourism Hackathon  
**Date:** September 2025  
**Highlights:**  
- Collaborated with an interdisciplinary team to develop tech-based solutions for tourism challenges.  
- Presented a functional prototype and technical report to a panel of judges.  
- Gained practical experience in data-driven tourism solutions and project management.  
""")
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
    if skill["image"]:
        col.image(skill["image"], width=60)
    col.write(f"**{skill['name']}**")

st.markdown("---")
# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")

