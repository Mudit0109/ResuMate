import base64
import streamlit as st
import io
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

# Load Gemini API Key from secrets
GOOGLE_API_KEY = st.secrets["API_KEYS"]["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get Gemini AI response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to convert first page of uploaded PDF to base64-encoded JPEG
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        page = doc.load_page(0)  # Get first page
        pix = page.get_pixmap()  # Convert to image
        img_byte_arr = io.BytesIO(pix.tobytes("jpeg"))

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr.getvalue()).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ----- Streamlit UI -----

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.5em;
    }
    .btn-primary {
        background-color: #ff7e5f;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 10px;
        cursor: pointer;
    }
    .btn-primary:hover {
        background-color: #e76e50;
    }
    .subheader {
        color: #343a40;
        font-weight: bold;
        margin-top: 20px;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main-header"><h1>📄 Resume Analyzer Using AI Expertise</h1></div>', unsafe_allow_html=True)

# Input fields
st.markdown('<div class="subheader">Enter Job Description:</div>', unsafe_allow_html=True)
input_text = st.text_area("Paste the Job Description below:", key="job_description")

uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type=["pdf"])
if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully!")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    submit1 = st.button("Analyze Resume", use_container_width=True)
with col2:
    submit2 = st.button("Match Percentage", use_container_width=True)
with col3:
    submit3 = st.button("Keyword Optimization", use_container_width=True)

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Provide a percentage match for the resume's alignment, 
missing keywords, and final thoughts.
"""

input_prompt3 = """
You are an experienced ATS optimizer. Analyze the provided resume and job description for important keywords. 
Identify the key terms, skills, and qualifications in the job description and compare them with the resume. 
List missing keywords and suggest improvements to better align the resume with the job description.
"""

# Handlers
if submit1:
    if uploaded_file is not None and input_text.strip():
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.markdown('<div class="subheader">Analysis Response:</div>', unsafe_allow_html=True)
        st.success(response)
    else:
        st.error("⚠️ Please upload your resume and provide a job description.")

elif submit2:
    if uploaded_file is not None and input_text.strip():
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.markdown('<div class="subheader">Percentage Match:</div>', unsafe_allow_html=True)
        st.warning(response)
    else:
        st.error("⚠️ Please upload your resume and provide a job description.")

elif submit3:
    if uploaded_file is not None and input_text.strip():
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.markdown('<div class="subheader">Keyword Optimization:</div>', unsafe_allow_html=True)
        st.info(response)
    else:
        st.error("⚠️ Please upload your resume and provide a job description.")
