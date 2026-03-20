import streamlit as st
import pandas as pd

st.title("Streamlit data cleaning App")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("Preview")
    st.write(df.head())

    st.subheader("Duplicate Rows")
    duplicates = df[df.duplicated(keep=False)]
    st.write(duplicates)

    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.write("Data after removing duplicates:")
        st.write(df)

    if st.button("Drop Missing Values"):
        df = df.dropna()
        st.write("Data after dropping missing values:")
        st.write(df)