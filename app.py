import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()


api_key = st.secrets["GEMINI_API_KEY"] 

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"temperature": 0.8})

# Streamlit Page Setup
st.set_page_config(page_title="Daily Motivation Generator", page_icon="💡")
st.title("💡 Daily Motivation Generator")
st.write("Select your current mood or situation, and receive a quote tailored just for you.")

# Mood Options
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


# 🧠 Caching the result to speed up repeated moods
@st.cache_data(show_spinner=False)
def generate_quote(mood):
    prompt = f"Give a short, uplifting motivational quote for someone who is {mood.lower()}."
    response = model.generate_content(prompt, stream=True)
    quote = ""
    for chunk in response:
        quote += chunk.text
    return quote.strip()


if st.button("Get Motivation"):
    with st.spinner("🧠 Thinking... Generating quote..."):
        quote = generate_quote(selected_mood)
        st.success("Here’s your motivational quote:")
        st.markdown(f"### ✨ _{quote}_")
