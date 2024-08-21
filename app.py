import streamlit as st
import google.generativeai as genai

st.image(".\Black Minimal Motivation Quote LinkedIn Banner.png")

st.title("My First Project")

genai.configure(api_key="AIzaSyCwPGS6ofVU7HS1win48RWx1-Jf0CBRa54")
text=st.text_input("Enter your Question")

if (text.strip() or st.button("Click Me")): 
 model = genai.GenerativeModel('gemini-pro')
 chat = model.start_chat(history=[])

 response = chat.send_message(text)
 st.write(response.text)

else:
    st.write("Please enter a question.")
