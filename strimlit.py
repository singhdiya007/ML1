# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 18:29:20 2026

@author: SINGH
"""

import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")
upload = st.file_uploader("Upload your dataset in (CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)
if upload is not None:
    if st.checkbox("View Dataset"):
        if st.button("head"):
            st.write(data.head())
        if st.button("tail"):
            st.write(data.tail())

if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Datatypes")
        st.write(data.dtypes())

if upload is not None:
    data_shape = st.radio("What dimensions do you want to check?",('Rows', 'Columns'))
    
    if data_shape == 'Rows':
        st.text("Number of rows: ")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of columns: ")
        st.write(data.shape[1])
        
if upload is not None:
    test=data.isnull().values.any()
    if test== True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations, no missing values")
        
if upload is not None:
    test= data.duplicated().any()
    if test== True:
        st.warning("This datasets contains some duplicate values")
        dup= st.selectbox("Do you want to remove duplicate values?", ("Select One", "Yes", "No"))
        
        if dup=="Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are removed")
        if dup=="No":
            st.text("Ok, no problem")
            
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include="all"))
if st.checkbox("Bye"):
    st.success("Diya-Riya")