import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import pandas as pd

if st.checkbox("Check my location"):
    loc = get_geolocation()
if loc:
    df = pd.DataFrame(loc)
    df2 = df.T
    df2 = df2.head(1)
    st.map(df2, latitude='latitude', longitude='longitude')
    
