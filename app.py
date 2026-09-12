import streamlit as st
from google import genai

st.title("🌱 Community Support Assistant")
st.write("Helping resolve local community issues using Google Gemini AI.")

# 1. Capture API Key from sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if not api_key:
    st.info("👉 Please enter your Gemini API key in the sidebar to test.")
    st.stop()

# 2. Capture user input
problem = st.text_area("Describe a local community issue (e.g., waste collection, health clinic access, street lighting):")

# 3. Only run Gemini when the button is clicked
if st.button("Generate Solution Plan"):
    if not problem.strip():
        st.warning("Please enter a community issue first.")
    else:
        with st.spinner("Generating solutions..."):
            try:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"You are a civic helper AI. Provide 3 actionable, low-cost community solutions for: {problem}"
                )
                st.markdown(response.text)
            except Exception as e:
                st.error(f"API Error: {e}")
