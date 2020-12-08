import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('MO COVID-19 Data')

DATE_COLUMN = 'testdate'
DATA_SOURCE = './MetricsTestDateCounty.csv'

# with open(DATA_SOURCE) as f:
#     freader = csv.DictReader(f)
#     for row in freader:
#         print(row)

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_SOURCE, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = data[DATE_COLUMN].astype("datetime64")
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

data = load_data(1000000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Number of cases by test date, county')

st.bar_chart(data)
