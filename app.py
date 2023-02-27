import streamlit as st
import random

st.title("Hi!!")
st.header("Welcome to my Page")
st.image("anime.png")
st.write("Want to see magic click it")



if st.button(f"Click Me👈 "):
    st.snow()
    st.balloons()
    st.write(":100:")
    st.write("Check the dashboards")
    video_file = open('bear.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    






