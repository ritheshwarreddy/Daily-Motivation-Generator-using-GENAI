import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Daily Motivation Generator", page_icon="💡")
st.title("💡 Daily Motivation Generator")
st.write("Select your current mood or situation, and receive a quote tailored just for you.")

# Mood options
moods = [
    "Feeling anxious", 
    "Need focus", 
    "Low energy", 
    "Feeling lost", 
    "Lack of motivation", 
    "Excited but nervous", 
    "Feeling grateful"
]

selected_mood = st.selectbox("How are you feeling today?", moods)

if st.button("Get Motivation"):
    with st.spinner("Generating your quote..."):
        prompt = f"""You are a motivational coach. Give me a single short and powerful motivational quote 
        that suits someone who is currently: {selected_mood}. Keep it positive, encouraging, and inspiring."""
        
        response = model.generate_content(prompt)
        quote = response.text.strip()
        
        st.success("Here’s your motivational quote:")
        st.markdown(f"### ✨ _{quote}_")
