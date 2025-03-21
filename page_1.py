import pandas as pd
import streamlit as st

st.title('Singapore Biodiversity Trend')
st.subheader('Occurrences per Year')

data = pd.read_csv('SG-Occurrence-Cleaned.csv')

occ_per_year = data.groupby('year').size().reset_index(name='count')
occ_per_year['year'] = occ_per_year['year'].astype(str)

st.line_chart(occ_per_year.set_index('year'))
st.table(occ_per_year)
