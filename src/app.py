import streamlit as st
from dotenv import load_dotenv
from ai_agent import generate_project_plan

load_dotenv()

st.title("Project Manager Application")
st.write("Welcome to the Project Manager App.\n Type in you project details and let the AI agent assist in planning it for you.")
input_text = st.text_area("Enter your project details here:")

if st.button("Plan Project"):
    if not input_text.strip():
        st.warning("Please enter project details.")
    else:
        with st.spinner("Planning your project..."):
            plan = generate_project_plan(input_text)

        st.success("Project plan generated successfully!")
        st.write(plan)