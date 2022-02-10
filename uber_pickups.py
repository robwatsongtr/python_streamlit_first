import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber Pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#function accepts a single parameter nrows, which specifies the number of 
#rows you want to load into the dataframe 
@st.cache
def load_data(nrows):

    # downloads data
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)

    # puts the data into a Pandas dataframe 
    #converts the date column from text to datetime
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    return data


#create a text element and let the reader know the data is loading 
data_load_state = st.text('Loading data....')

#load 10,000 rows of data into the dataframe
data = load_data(10000)

#notify the reader that the data was successfully loaded
data_load_state.text('Done! (using st.cache)')

st.subheader('Raw Data')
st.write(data)