import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("A simple data dashboard to overview the data")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data OVerview")
    st.write(df.head(250))

    st.subheader("Data Description")
    st.write(df.describe())

    st.subheader("Data Filteration")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Column to filter the data", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select value to filter the data", unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)
    
    st.subheader("Data Visualization")
    x_column = st.selectbox("Select x-axis", columns)
    y_column = st.selectbox("Select y-axis", columns)

    if st.button("Generate visualization"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        st.bar_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Please upload a csv file to get details")