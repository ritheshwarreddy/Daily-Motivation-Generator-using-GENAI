import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Daily Motivation Generator", page_icon="💡")
st.title("💡 Daily Motivation Generator")

moods = ["Feeling anxious", "Need focus", "Low energy", "Feeling lost", 
         "Lack of motivation", "Excited but nervous", "Feeling grateful"]
selected_mood = st.selectbox("How are you feeling today?", moods)

@st.cache_data
def generate_quote(mood):
    prompt = f"Give a short, uplifting motivational quote for someone who is {mood.lower()}."
    resp = model.generate_content(prompt, stream=True)
    return "".join(chunk.text for chunk in resp).strip()

if st.button("Get Motivation"):
    with st.spinner("Generating..."):
        quote = generate_quote(selected_mood)
        st.success("Here’s your motivational quote:")
        st.markdown(f"### ✨ _{quote}_")
