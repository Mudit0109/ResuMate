import streamlit as st
import http.client
import json
from urllib.parse import quote
import os

# Fetch job data from the API
def fetch_jobs(query, location, remote_only, employment_types):
    conn = http.client.HTTPSConnection("jobs-api14.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': st.secrets["API_KEYS"]["RAPIDAPI_KEY"],
        'x-rapidapi-host': "jobs-api14.p.rapidapi.com"
    }
    
    query_encoded = quote(query)
    location_encoded = quote(location)
    employment_types_str = "%3B".join(employment_types)
    remote_param = "true" if remote_only else "false"

    endpoint = (
        f"/v2/list?query={query_encoded}&location={location_encoded}"
        f"&autoTranslateLocation=false&remoteOnly={remote_param}"
        f"&employmentTypes={employment_types_str}"
    )
    conn.request("GET", endpoint, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)

# Set page configuration
st.set_page_config(page_title="Job Finder", page_icon="💼", layout="wide")
st.title("🌟 Job Opportunities Finder")
st.markdown(
    """
    <style>
        body {
            background-color: #F5F7FA;
        }
        .stTextInput > div:first-child {
            font-family: Arial, sans-serif;
            font-size: 16px;
            font-weight: bold;
        }
        .stCheckbox {
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        h3 {
            font-family: 'Arial', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Input fields
query = st.text_input("🔍 Job Title / Keywords", "Web Developer")
location = st.text_input("📍 Location", "India")
remote_only = st.checkbox("💻 Remote Only", value=False)
employment_types = st.multiselect(
    "⏳ Employment Types",
    options=["fulltime", "parttime", "intern", "contractor"],
    default=["fulltime"]
)

# Function to display job cards
def render_job_card(job):
    company = job.get("company", "Unknown Company")
    employment_type = job.get("employmentType", "Not Specified")
    date_posted = job.get("datePosted", "Unknown")
    description = job.get("description", "No Description Available")
    job_providers = job.get("jobProviders", [])
    
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(to right, #2C3E50, #e6e9ef);
            border: 1px solid #dcdcdc;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
        ">
            <h3 style="color: #FF0000;">{company}</h3>
            <p><strong>📌 Employment Type:</strong> {employment_type}</p>
            <p><strong>📅 Posted:</strong> {date_posted}</p>
            <p><strong>📝 Description:</strong> {description[:300]}...</p>
            <strong>🔗 Job Providers:</strong>
            <ul style="padding-left: 20px;">
                {''.join(f'<li><a href="{provider.get("url", "#")}" target="_blank" style="color: #2980B9; text-decoration: none;">{provider.get("jobProvider", "Unknown Provider")}</a></li>' for provider in job_providers)}
            </ul>
            <a href="{job_providers[0].get("url", "#")}" target="_blank" style="
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                background-color: #3498DB;
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            " onmouseover="this.style.backgroundColor='#2980B9'" onmouseout="this.style.backgroundColor='#3498DB'">Apply Now</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Search button and results
if st.button("🔎 Search Jobs"):
    with st.spinner("Fetching job opportunities..."):
        try:
            jobs_data = fetch_jobs(query, location, remote_only, employment_types)
            if jobs_data.get("jobs"):
                jobs = jobs_data["jobs"]
                st.success(f"✅ Found {len(jobs)} jobs!")
                
                for job in jobs:
                    render_job_card(job)
            else:
                st.warning("⚠️ No jobs found. Try adjusting your search.")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
