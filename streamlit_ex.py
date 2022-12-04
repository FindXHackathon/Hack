# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:08:02 2022

@author: User
"""

import streamlit as st
import pandas as pd
import plotly.express as px



st.write('# Langrangian Ocean Search Targets (LOST)')

st.markdown('''
An Interactive Operational Search and Rescue Platform. 
\n 
Brought to you by **FindX**.
''')


# st.header('Map of Location')
# selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
# submitted = st.button('Submit')

st.header('Enter the following required information.')
with st.form(key='my_form'):
    longitude = st.text_input(label='Longitude of deployment site (between 0 & 40)',value ='10')   
    latitude = st.text_input(label='Latitude of deployment site (between -50 & -10)',value ='-45')
    start_date = st.text_input(label='Start date and time of the deployment: (Year/Month/Day Hour:Minute:Second}', value ='2021/05/15 00:00:00')  
    duration = st.text_input(label='Duration of the model run in days',value ='2')
    
    st.header("Select Object Type")
    type_list = ["PIW State Unknown","Something Else", "Other"]
    selected_object_type = st.selectbox(label='Select the object type from the drop down menu', options=type_list)
    
    st.header("Enter Optional Information")
    deployment_radius = st.text_input(label='Enter the radius of the deployment of particles around a point (OPTIONAL)',value ='4')
    Output_file = st.text_input(label='Enter the output file name which can be used for plotting', value ='output_file')                      
    st.form_submit_button("Submit")
    
    
    # submitted = st.button('Submit')

# if submitted:
#     filtered_avocado = avocado[avocado['geography'] == selected_geography]
#     line_fig = px.line(filtered_avocado,
#                        x='date', y='average_price',
#                        color='type',
#                        title=f'Avocado Prices in {selected_geography}')
#     st.plotly_chart(line_fig)

with st.sidebar:
    #st.sidebar.title('LOST')
    st.sidebar.image('.\lost.png')
    st.subheader('About')
    st.markdown('Put information about LOST here')
    st.subheader('\n ')
    st.markdown('Put information about LOST here')


#To plot an image

st.title("Output")