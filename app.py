import streamlit as st
import google.generativeai as genai


st.title("My First Project")

genai.configure(api_key="AIzaSyA77A204c9dKawAZZLJ14Mv6mSnKvIPwk4")
text=st.text_input("Enter your Question")

if (text.strip() or st.button("Click Me")): 
 model = genai.GenerativeModel('gemini-pro')
 chat = model.start_chat(history=[])

 response = chat.send_message(text)
 st.write(response.text)

else:
    st.write("Please enter a question.")
