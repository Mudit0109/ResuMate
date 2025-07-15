import streamlit as st
import requests

# Set up page
st.set_page_config(page_title="Job Finder", page_icon="💼", layout="wide")
st.title("🌟 Job Opportunities Finder")

# Input fields
query = st.text_input("🔍 Job Title / Keywords", "Web Developer")
location = st.text_input("📍 Location", "India")
remote_only = st.checkbox("💻 Remote Only", value=False)

# Search Button
if st.button("🔎 Search Jobs"):
    with st.spinner("Fetching job opportunities..."):

        try:
            url = "https://jsearch.p.rapidapi.com/search"

            querystring = {
                "query": f"{query} in {location}",
                "remote_jobs_only": str(remote_only).lower(),
                "page": "1",
                "num_pages": "1"
            }

            headers = {
                "X-RapidAPI-Key": st.secrets["API_KEYS"]["RAPIDAPI_KEY"],  # Add this to secrets.toml
                "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            if data.get("data"):
                st.success(f"✅ Found {len(data['data'])} jobs!")
                for job in data["data"]:
                    st.markdown(f"""
                        <div style="padding:20px; margin-bottom:10px; border-radius:10px; border:1px solid #ccc;">
                            <h4 style="color:#FF5733;">{job['employer_name']}</h4>
                            <p><strong>📌 Job Title:</strong> {job['job_title']}</p>
                            <p><strong>📍 Location:</strong> {job['job_city']}, {job['job_country']}</p>
                            <p><strong>📅 Posted:</strong> {job['job_posted_at_datetime_utc']}</p>
                            <p><strong>📝 Summary:</strong> {job['job_description'][:300]}...</p>
                            <a href="{job['job_apply_link']}" target="_blank">🔗 Apply Here</a>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ No jobs found. Try changing your search.")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
