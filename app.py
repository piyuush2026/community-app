from google import genai
import streamlit as st

st.title("🌱 Community Support Assistant")
st.write("Helping resolve local community issues using Google Gemini AI.")

# API Key input in sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    problem = st.text_area("Describe a local community issue (e.g., waste collection, health clinic access, street lighting):")
    
    if st.button("Generate Solution Plan"):
        if problem:
            with st.spinner("Analyzing with Gemini..."):
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"You are a civic helper AI. Provide 3 actionable, low-cost community solutions for: {problem}"
                )
                st.subheader("Actionable Steps:")
                st.write(response.text)
        else:
            st.warning("Please enter a problem description first.")
else:
    st.info("👈 Please enter your Gemini API key in the sidebar to test.")
