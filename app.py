import os
import re
import pandas as pd
import streamlit as st

st.title('Data Annotator')
uploaded_file = st.file_uploader("Load data to annotate", type=['csv', 'xls', 'xlsx', 'xlsm', 'odf', 'ods'], accept_multiple_files=False, key=None, on_change=None, disabled=False, 
                                help="Please enter a valid format: \n- csv\n- xls\n- xlsx\n- xlsm\n- odf\n- ods")

if uploaded_file is not None:
    # Match file extension
    if uploaded_file.name.rsplit('.', 1)[1] == 'csv':
        # Read csv as dataframe:
        read_file = pd.read_csv
    else: 
        # Read excel as dataframe:
        read_file = pd.read_excel 
    df = read_file(uploaded_file)
    selected_column = st.selectbox("Select a column to annotate", df.columns, index=0, help=None, on_change=None, disabled=False)
    
    df_copy = df.copy()
    rows_count = len(df_copy.index)