import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Audio Driven Talking demo")

col1, col2 = st.columns(2)

with col1:
    webrtc_streamer(key="sample")

with col2:
    webrtc_streamer(key="demo")

st.radio(
    "Choose a Image for Talking Head",
    ('Obama', 'Trump', 'Morgan'))

