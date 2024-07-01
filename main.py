import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import pandas as pd

if st.checkbox("Check my location"):
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")



if loc:
    df = pd.DataFrame(loc)
    st.markdown(df.columns)
    df2 = df.pivot(index='coords')
    st.dataframe(df2)


#st.map(
    
