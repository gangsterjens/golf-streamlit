import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import pandas as pd

button = st.button('Press here')
if button:
  location = streamlit_geolocation()
  st.markdown(str(location))
