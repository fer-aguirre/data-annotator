from operator import index
import pandas as pd
import streamlit as st


# Set streamlit app title
st.title('Data Annotator')
# Upload a 'csv' or 'excel' file
uploaded_file = st.file_uploader("Load data to annotate", type=['csv', 'xls', 'xlsx', 'xlsm', 'odf', 'ods'], accept_multiple_files=False, key=None, on_change=None, disabled=False,
                                help="Please enter a valid format: \n- csv\n- xls\n- xlsx\n- xlsm\n- odf\n- ods")

# If there's an uploaded file
if uploaded_file:
    # Match file extension
    if uploaded_file.name.rsplit('.', 1)[1] == 'csv':
        # Function to read 'csv' file:
        read_file = pd.read_csv
    else:
        # Function to read 'excel' file:
        read_file = pd.read_excel
    #  Read file as dataframe
    df = read_file(uploaded_file)
    # Select a column to annotate from dataframe
    selected_column = st.selectbox(
        "Select a column to annotate", df.columns, index=0, help=None, on_change=None, disabled=False)

    if 'labels' not in st.session_state:
        # Add labels as a session state variable
        st.session_state.labels = {}
        # Add count as a session state variable
        st.session_state.count = 0
        # Add remaining rows as a session state variable
        st.session_state.remaining_rows = len(df.index)

    # Function to build a stateful annotator
    def annotate(label):
        st.session_state.labels[st.session_state.count] = label
        st.session_state.count += 1
        st.session_state.remaining_rows -= 1

    # Insert containers laid out as columns
    col1, col2, col3, col4 = st.columns([6, 1, 1, 2])

    with col1:
        # Show row by row on dataframe's selected column
        st.write(df.at[st.session_state.count, selected_column])

        # Show the counts for rows annotated and remaining rows
        st.write("Annotated: ", st.session_state.count, " - ", "Remaining:", st.session_state.remaining_rows)

    with col2:
        st.button('Yes ✅', on_click=annotate, args=("Yes",))

    with col3:
        st.button('No ❌', on_click=annotate, args=("No",))

    # Convert values from labels to list
    labels = list(st.session_state.labels.values())
    if st.button('Finish'):
        # Add a new column with labels
        df['Labels'] = pd.Series(labels)
        st.write(df)

    # Add back button
    # Add styles
    # Connect to google API