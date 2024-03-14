import streamlit as st
import diskcache as dc
import pandas as pd

cache = dc.Cache("cache")

st.markdown("Ade Ganteng LOH")

file_key = "parquet_data"
if file_key in cache:
    st.markdown("File sudah ada di cache..")
else:
    st.markdown("adding to cache..")
    with cache as c:
        c.set("parquet_data", "sumpah dah")

with cache as c:
    data_cached = c.get("parquet_data")

st.markdown(data_cached)

df = pd.DataFrame({'ade' : [1,2,3]})

try:
    df.to_csv("adenih.csv")
    st.markdown("sending csv success..")
except:
    st.markdown("walah gagal..")