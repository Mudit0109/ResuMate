import streamlit as st


st.set_page_config(
    page_title="ResuMate - Your Career Companion",
    page_icon="📄",
    layout="centered",
)


st.markdown(
    """
    <style>
    /* Main Title */
    .main-title {
        font-size: 3.0rem;
        font-weight: bold;
        color: #FFC0CB; /* Soft Pink */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 0 5px #800080, 0 0 10px #800080, 0 0 15px #800080, 0 0 20px #800080; /* Purple Glow */
    }

    /* Subheader */
    .subheader {
        color: #FFFFFF
        font-size: 1.8rem;
        margin-bottom: 20px;
        text-align: center;
        text-shadow: 0 0 5px #ADD8E6, 0 0 10px #ADD8E6, 0 0 15px #ADD8E6, 0 0 20px #ADD8E6; /* Light Blue Glow */
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #2E8B57; /* Rich Green */
        color: #fff;
        padding: 15px;
        border-radius: 8px;
        font-size: 1.1rem;
    }
    .sidebar .sidebar-header {
        font-size: 1.5rem;
        margin-bottom: 15px;
    }
    
    /* Content Section */
    .content-section {
        font-size: 1.5rem;
        # background-color: #000; /* Light Gray */
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="main-title"><h1>Welcome to ResuMate!💼</h1></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheader"><br>Your AI-powered career companion to enhance resumes and ace interviews.</div>',
    unsafe_allow_html=True,
)


st.sidebar.header("Navigation")
st.sidebar.success("Select a page above to explore ResuMate's features.")


st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.markdown(
    '<h3 style=" font-size: 2rem ;text-shadow: 0 0 5px #0000FF, 0 0 10px #0000FF, 0 0 15px #0000FF, 0 0 20px #0000FF;">Why ResuMate?</h3>',
    unsafe_allow_html=True
)
st.markdown(
    """


    **ResuMate** addresses the challenges faced by job seekers in an increasingly competitive job market:
    
    - 📝 **Optimize resumes** for **Applicant Tracking Systems (ATS)**.
    - 📋 Provide **feedback** on formatting, keywords, and content.
    - 🌐 Find current **job opportunity postings**.
    - ✍️ Enable **manual creation** of ATS-compliant resumes.
    - 🎯 Offer **expected interview coaching and questions**.
    
    
    Whether you're a student entering the job market or a professional seeking career advancement, ResuMate empowers you to succeed.
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)
