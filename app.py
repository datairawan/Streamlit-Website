import streamlit as st
import diskcache as dc
cache = dc.Cache("cache")

st.markdown("Ade Ganteng")

file_key = "parquet_data"
if file_key in cache:
    print(f"File sudah ada di cache..")
else:
    print("adding to cache..")
    with cache as c:
        c.set("parquet_data", "sumpah dah")

with cache as c:
    data_cached = c.get("parquet_data")

st.markdown(data_cached)