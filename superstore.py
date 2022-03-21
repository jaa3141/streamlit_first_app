# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:03:37 2022

@author: jaa31
"""
import streamlit as st
import pandas as pd
import plotly.express as px
st.title('Streamlit Practice App')
df=pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

view_options=['Product Name', 'Category','Region']
metric_options=['Sales','Quantity','Profit']
with st.sidebar:
    check=st.checkbox('Psst, wanna c sum data?')
    pick_metric=st.selectbox('View breakdown of',metric_options)
    pick_view=st.selectbox('by',view_options)

barf=px.bar(df,x=pick_view,y=pick_metric,title=f'Bar chart of {pick_metric} by {pick_view}')
st.plotly_chart(barf)

if check:
    df
