import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="ResumeMate - Your Career Companion",
    page_icon="assets/resumate_logo.png",
    layout="centered",
)

# ===== CSS For Glow Effect Around Image =====
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .glow-box {
        border-radius: 12px;
        padding: 5px;
        background: linear-gradient(50deg, #ff4d4d, #ff0000, #ff4d4d);
box-shadow: 0 0 30px #ff0000, 0 0 40px #ff0000;
        width: fit-content;
    }

    .glow-box img {
        display: block;
        border-radius: 12px;
        width: 400px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Display Image With Glow Effect (LOCAL FILE) =====
with open("assets/resumate_logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div class="centered">
        <div class="glow-box">
            <img src="data:image/png;base64,{encoded}" />
        </div>
    </div>
""", unsafe_allow_html=True)

# ===== Rest of App =====

st.markdown('<div class="main-title"><h1>Welcome to ResumeMate! 💼</h1></div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .main-title {
        font-size: 5.0rem;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 0 5px #FF0000, 0 0 10px #FF0000,
             0 0 15px #FF0000, 0 0 20px #FF0000;
    }
    .subheader {
        color: #FFFFFF;
        font-size: 1.8rem;
        margin-bottom: 20px;
        text-align: center;
        text-shadow: 0 0 5px #ADD8E6, 0 0 10px #ADD8E6,
                     0 0 15px #ADD8E6, 0 0 20px #ADD8E6;
    }
    .content-section {
        font-size: 1.5rem;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="subheader"><br>Your AI-powered career companion to enhance resumes and ace interviews.✨</div>', unsafe_allow_html=True)

with open("assets/sidebar.png", "rb") as image_file:
    encoded1 = base64.b64encode(image_file.read()).decode()
st.sidebar.header("Navigation")

st.sidebar.error("Select a page above to explore ResumeMate's features.")
st.sidebar.markdown(f"""
    <div class="centered">
        <div class="glow-box">
            <img src="data:image/png;base64,{encoded1}" />
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-section">', unsafe_allow_html=True)

st.markdown(
    '<h3 style="font-size: 2rem; text-shadow: 0 0 5px #FF3C00, 0 0 10px #FF3C00, 0 0 15px #FF3C00, 0 0 20px #FF3C00;">Why ResumeMate?</h3>',
    unsafe_allow_html=True
)

st.markdown("""
**ResumeMate** addresses the challenges faced by job seekers in an increasingly competitive job market:

- 📝 **Optimize resumes** for **Applicant Tracking Systems (ATS)**.
- 📋 Provide **feedback** on formatting, keywords, and content.
- 🌐 Find current **job opportunity postings**.
- ✍️ Enable **manual creation** of ATS-compliant resumes.
- 🎯 Offer **expected interview coaching and questions**.

Whether you're a student entering the job market or a professional seeking career advancement, ResumeMate empowers you to succeed.
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
