import streamlit as st
from PIL import Image

st.set_page_config(
   page_title="About Us - On Guard",
)

logo = Image.open("on_guard_logo.jpg")
st.image(logo, width=400)

st.title('About Us')
st.subheader('On Guard is a parental control app created to assist parents and guardians to be a digital protector of their children in the online world.')
st.subheader('We aim to keep every Filipino child safe from the potential threats online and empower parents to their highest.')

st.subheader("Our Team")
st.markdown("**Jickle Clain Ong**: Team Leader")
st.markdown("**Luna Rinoa Batungbakal**: Lead Programmer")
st.markdown("**Jana Annika Uy**: Front-End Developer")
st.markdown("**Jameela Ysabelle Clay Ong**: Multimedia Artist")
st.markdown("Representing Victory Christian International School")
