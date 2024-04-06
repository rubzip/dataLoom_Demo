import streamlit as st
import pandas as pd
from fun import select, get_numeric_cols, get_min_max, filter_number, dropna, group, info, describe

st.title("DataLoom PoC 💡")
data = pd.read_csv("./data/Titanic-Dataset.csv")

st.sidebar.title("Filtering Options")

all_cols = list(data.columns)
select_cols = st.sidebar.multiselect('SELECT columns:', all_cols, default=all_cols)
out = select(data, select_cols)
st.sidebar.write("Filter:")
num_cols = get_numeric_cols(out)
for col in num_cols:
    mini, maxi = get_min_max(out, col)
    start_num, end_num = st.sidebar.slider(col, min_value=mini, max_value=maxi, value=(mini, maxi))
    out = filter_number(out, col, start_num, end_num)

all_cols = list(out.columns)
by = st.sidebar.multiselect('Group By:', all_cols, default=[])
if len(by)>0:
    funcs = st.sidebar.multiselect('Functions:', ['sum', 'min', 'max'], default=['sum'])
    out = group(out, by, funcs)

st.title("")
st.write(out)
st.write(describe(out))
if len(by)==0:
    st.write(info(out))