import streamlit as st
import requests


def convert_markdown_to_pdf(markdown_content, Resume_file="Resume.pdf", engine="weasyprint"):
    cssfile = """
                body {
                    padding: 0px;
                    margin: 0px;
                }
                h1 {
                    color: MidnightBlue;
                    margin: 0px;
                    padding: 0px;
                }
                h3 {
                    color: MidnightBlue;
                    padding-bottom: 0px;
                    margin-bottom: 0px;
                }
                li {
                    margin-top: 5px;
                }
    """
    url = "https://md-to-pdf.fly.dev"

    data = {
        'markdown': markdown_content,
        'css': cssfile,
        'engine': engine
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        with open(Resume_file, 'wb') as f:
            f.write(response.content)
        return f"PDF saved to {Resume_file}", Resume_file
    else:
        return f"Error {response.status_code}: {response.text}", None


def generate_markdown(name, email, mobile, education, skills, experience, projects, achievements, activities):
    markdown_text = f"<h1 style=\"text-align:center;\">{name}</h1>\n" \
                    f"<p style=\"text-align:center;\">Email: {email} | Mobile: {mobile}</p>\n\n"
    markdown_text += "### Education\n\n---\n\n"
    for edu in education:
        markdown_text += f"- {edu['level']}: {edu['institution']} | {edu['field']} | " \
                         f"Score: {edu['score']} | {edu['duration']}.\n\n"

    markdown_text += "### Skills\n\n---\n\n"
    markdown_text += f"{skills}\n\n"

    markdown_text += "### Experience\n\n---\n\n"
    for exp in experience:
        markdown_text += f"- **{exp['job_role']} ({exp['company_name']})**: {exp['description']}\n"

    markdown_text += "\n### Projects\n\n---\n\n"
    for proj in projects:
        markdown_text += f"- **{proj['name']}**: {proj['description']}\n"

    markdown_text += "\n### Achievements\n\n---\n\n"
    for ach in achievements:
        markdown_text += f"- {ach}\n"

    markdown_text += "\n### Other Activities\n\n---\n\n"
    markdown_text += activities + '\n'

    return markdown_text


# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
        }
        .main-header {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .sub-header {
            color: #343a40;
            font-weight: bold;
            margin-top: 20px;
            font-size: 1.5em;
        }
        .input-section {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .button-primary {
            background-color: #ff7e5f;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            margin-top: 10px;
            cursor: pointer;
        }
        .button-primary:hover {
            background-color: #e76e50;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main-header">Resume Generator</div>', unsafe_allow_html=True)

# Input Fields
st.markdown('<div class="sub-header">Personal Information</div>', unsafe_allow_html=True)
with st.container():
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    mobile = st.text_input("Enter your mobile number:")

# Section for Education
st.markdown('<div class="sub-header">Education</div>', unsafe_allow_html=True)
if "education_list" not in st.session_state:
    st.session_state["education_list"] = []

with st.expander("Add Education"):
    edu_level = st.text_input("Education Level (e.g., High School, Graduation):")
    edu_institution = st.text_input("Institution Name:")
    edu_field = st.text_input("Field of Study:")
    edu_duration = st.text_input("Passing Year:")
    edu_score = st.text_input("Score (e.g., GPA/Percentage):")
    if st.button("Save Education"):
        st.session_state["education_list"].append({
            "level": edu_level,
            "institution": edu_institution,
            "field": edu_field,
            "duration": edu_duration,
            "score": edu_score
        })

for edu in st.session_state["education_list"]:
    st.write(edu)

# Skills
st.markdown('<div class="sub-header">Skills</div>', unsafe_allow_html=True)
skills = st.text_area("Enter your skills (comma-separated):")

# Experience
st.markdown('<div class="sub-header">Experience</div>', unsafe_allow_html=True)
if "experience_list" not in st.session_state:
    st.session_state["experience_list"] = []

with st.expander("Add Experience"):
    exp_job = st.text_input("Job Role:")
    exp_company = st.text_input("Company Name:")
    exp_description = st.text_area("Job Description:")
    if st.button("Save Experience"):
        st.session_state["experience_list"].append({
            "job_role": exp_job,
            "company_name": exp_company,
            "description": exp_description
        })

for exp in st.session_state["experience_list"]:
    st.write(exp)

# Projects
st.markdown('<div class="sub-header">Projects</div>', unsafe_allow_html=True)
if "project_list" not in st.session_state:
    st.session_state["project_list"] = []

with st.expander("Add Project"):
    proj_name = st.text_input("Project Title:")
    proj_description = st.text_area("Project Description:")
    if st.button("Save Project"):
        st.session_state["project_list"].append({
            "name": proj_name,
            "description": proj_description
        })

for proj in st.session_state["project_list"]:
    st.write(proj)

# Achievements
st.markdown('<div class="sub-header">Achievements</div>', unsafe_allow_html=True)
achievements = st.text_area("Enter your achievements (one per line):").split("\n")

# Other Activities
st.markdown('<div class="sub-header">Other Activities</div>', unsafe_allow_html=True)
activities = st.text_area("Enter your other activities or hobbies:")

# Generate Resume Button
if st.button("Generate Resume"):
    markdown_text = generate_markdown(
        name, email, mobile,
        st.session_state["education_list"], skills,
        st.session_state["experience_list"], st.session_state["project_list"],
        achievements, activities
    )
    status, file_path = convert_markdown_to_pdf(markdown_text)
    st.success(status)
    if file_path:
        with open(file_path, "rb") as pdf_file:
            st.download_button("Download Resume", pdf_file, file_name="Resume.pdf", key="download_resume")
