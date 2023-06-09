import streamlit as st
import pandas as pd
import seaborn as sns
import os

# Set proxy environment variables
os.environ['HTTP_PROXY'] = 'http://daicelproxy3:80'
os.environ['HTTPS_PROXY'] = 'http://daicelproxy3:80'

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Sidebar controls for filtering the data
species = st.sidebar.selectbox('Select Species', iris_df['species'].unique())
filtered_df = iris_df[iris_df['species'] == species]

# Display the filtered data table
st.write(filtered_df)

# Scatter plot
st.subheader('Scatter Plot')
x_axis = st.selectbox('Select X-Axis', iris_df.columns[:-1])
y_axis = st.selectbox('Select Y-Axis', iris_df.columns[:-1])
sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue='species')
st.pyplot()

# Histogram
st.subheader('Histogram')
sns.histplot(data=filtered_df, x=x_axis, kde=True)
st.pyplot()

# Bar plot
st.subheader('Bar Plot')
column = st.selectbox('Select Column', iris_df.columns[:-1])
sns.barplot(data=filtered_df, x='species', y=column)
st.pyplot()

# command: streamlit run streamlit_test\st_test.py