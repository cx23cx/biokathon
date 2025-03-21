import numpy as np
import streamlit as st

# Define the pages
page_1 = st.Page("page_1.py", title="Singapore Biodiversity Trend", icon="🎈")
page_2 = st.Page("page_2.py", title="The Pigathon Team", icon="❄️")

# Set up navigation
pg = st.navigation([page_1, page_2])

# Run the selected page
pg.run()
