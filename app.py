"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import pandas as pd
import streamlit as st

st.title("St Nicholas Girls School")

st.header("The Pigathon Team")

st.write("Click the button to show our school coordinate!")

if "show_map" not in st.session_state:
    st.session_state.show_map = False

def toggle_map():
    st.session_state.show_map = not st.session_state.show_map

st.button(
    "Hide Map" if st.session_state.show_map else "Show Map",
    on_click=toggle_map,
)

if st.session_state.show_map:
    data = pd.DataFrame({
        "lat": [1.3740],
        "lon": [103.8342],
    })
    st.map(data)
