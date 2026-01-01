import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Project Manager Application")
st.write("Welcome to the Project Manager App.\n Type in you project details and let the AI agent assist in planning it for you.")
input_text = st.text_area("Enter your project details here:")

if st.button("Plan Project"):
    st.write("Planning your project...")
    # Write the logic here to interact with the AI agent and generate the project plan
    st.write("Project plan generated successfully!")

