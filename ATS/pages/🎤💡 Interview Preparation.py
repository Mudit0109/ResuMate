import os
import io
import base64
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get AI response
def get_interview_coaching_response(job_description, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([job_description, prompt])
    return response.text

# Set page configuration
st.set_page_config(
    page_title="Interview Coach",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Header with styling
st.markdown(
    """
    <div style="background-color:#2E86C1; padding:15px; border-radius:10px; text-align:center;">
        <h1 style="color:white; font-family:Arial, sans-serif;">🤖 AI-Powered Interview Coach</h1>
        <p style="color:white; font-size:16px; font-family:Arial, sans-serif;">
            Generate interview questions, answers, and expert coaching tips tailored to your job description!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Job description input
st.markdown(
    """
    <div style="margin-top:20px;">
        <label style="font-family: Arial, sans-serif; font-size: 18px; font-weight: bold;">📄 Enter Job Description:</label>
    </div>
    """,
    unsafe_allow_html=True
)
job_description = st.text_area("", placeholder="Paste the job description here...", key="job_description", height=200)

# Generate button
submit = st.button(
    "🚀 Generate Interview Questions & Coaching",
    help="Click to generate interview questions and tips based on the job description",
)

# AI Prompt
interview_prompt = """
You are an experienced recruiter with a deep understanding of the job market. Based on the provided job description, 
generate a set of possible interview questions along with detailed answers. 
For each question, also provide coaching tips on how to answer them effectively, including key points the candidate should mention.
"""

# Results
if submit:
    if job_description:
        with st.spinner("Generating interview coaching tips..."):
            try:
                response = get_interview_coaching_response(job_description, interview_prompt)
                st.markdown(
                    """
                    <div style="margin-top:20px; padding:10px; background-color:#E8F6F3; border:1px solid #AED6F1; border-radius:10px;">
                        <h2 style="font-family:Arial, sans-serif; color:#1A5276;">🎯 Generated Interview Questions & Tips</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.info(response)
            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")
    else:
        st.warning("⚠️ Please enter the job description before generating questions.")


