# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:08:02 2022

@author: User
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image



st.write('# LOST')

st.markdown('''
Langrangian Ocean Search Targets
\n
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
    type_list = ["Person In Water: State Unknown","Person In Water: with life jacket", "Person In Water: Vertical", "Person In Water: sitting / huddled", "Person In Water: floating on back", "Liferaft: no ballast pockets, general type", "Liferaft: no ballast pockets, no canopy, no drouge", "Liferaft: no ballast pockets, with canopy, with drouge", "Liferaft: shallow ballast pockets with canopy, capsized", "Liferaft: 4–6 man, with canopy, with drouge", "Liferaft: 15–25 man, with canopy, with drouge", "Aviation raft: 4–6 man, with canopy, no drouge","Personal watercraft: Sea kayak, with person", "Personal watercraft: Homemade wood raft", "Personal watercraft: Homemade wood raft, with sail", "Personal watercraft: Surfboard with person", "Personal watercraft: Windsurfer with person, sail and mast in the water", "Sailing vessel: mono hull, keel, medium displacement", "Power vessel: Enclosed Lifeboat", "Power vessel: Vessel with outboard motors no drouge", "Power vessel: Flat bottomed board, boston whaler", "Power vessel: V hull boat", "Power vessel: Sport fisher, centre open console", "Power vessel: Commercial fishing vessel type unknown", "Power vessel: Commercial fishing vessel longline, stern or net", "Power vessel: Coastal freighter", "Flotsam: Fishing vessel general debris", "Flotsam: Cubic metre bait box, loading unknown"]
    selected_object_type = st.selectbox(label='Select the object type from the drop down menu', options=type_list)
    
    st.header("Enter Optional Information")
    deployment_radius = st.text_input(label='Enter the radius of the deployment of particles around a point (OPTIONAL)',value ='4')
    Output_file = st.text_input(label='Enter the output file name which can be used for plotting', value ='output_file_'+str(start_date[0:4])+str(start_date[5:7])+str(start_date[8:10]))                      
    submitted = st.form_submit_button("Submit")
    
    # Every form must have a submit button.

if submitted:
    st.title("Output")
    image = Image.open('.\Output_image.png')
    st.image(image, caption='Red dot indicates the location of the Person in Water.')



with st.sidebar:
    #st.sidebar.title('LOST')
    st.sidebar.image('.\lost.png')
    st.subheader('\n ')
    st.subheader('About')
    st.markdown('''On the 18th of January 2016, the upturned hull of a catamaran was
                spotted approximately 113 nautical miles off Cape Recife, near Port
                Elizabeth (South Africa). 5 days after being spotted off Cape Recife, on
                the 22nd of January 2016, the National Sea Rescue Institute (NSRI)
                found the capsized catamaran south of Cape Agulhas. The approximate
                locations, the last known position and the recovery site of the capsized
                vessel provides valuable information that are used to assess the ability of
                the LOST particle trajectory model. ( Hart-Davis et al. (2018). 
                LOST projects and models the location of such a particle lost at sea.''')
    st.subheader('\n ')
    st.subheader('\n ')
    st.header("Authors")
    st.markdown('Björn Backeberg')
    st.markdown('Michael Hart-Davis')
    st.subheader('\n ')
    st.subheader('\n ')
    st.header("Made accesible by")
    st.markdown('**_FindX_**')


#To plot an image
# if submitted:
#     filtered_avocado = avocado[avocado['geography'] == selected_geography]
#     line_fig = px.line(filtered_avocado,
#                        x='date', y='average_price',
#                        color='type',
#                        title=f'Avocado Prices in {selected_geography}')
#     st.plotly_chart(line_fig)




# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("url_goes_here")
#     }
#    .sidebar .sidebar-content {
#         background: url("url_goes_here")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
