import numpy as np
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import matplotlib.pyplot as plt
import xarray as xr


# Initialize flask app & api
app = Flask(__name__)
api = Api(app)


### API BODY

class Lost(Resource):

    ### POST PROCESS
    
    def post(self):
        ## Request :      
        
        parser = reqparse.RequestParser()  # initialize
        
        # Input from the interface
        
        lon = parser.add_argument('Longitude', required=True)  # longitude 
        lat = parser.add_argument('Latitude', required=True)  # latitude
        ttime = parser.add_argument('Start_Date', required=True)   # initial time localisation
        duration = parser.add_argument('Duration', required=True) # number of days
        radius = parser.add_argument('Deployment_radius', required=True)  # deployment radius
        object_type = parser.add_argument('Object_type', required=True) # the type of the object
        
        args = parser.parse_args()  # parse arguments to dictionary

                
        '''a region between 0 and 40 Longitude and -50 and -10
        Latitude, and dates from 2021-05-15 to 2021-05-25. Hence a user will be limited to that geographic 
        extent and time period when running LOST simulations.'''

        
        if lon <= 0 and lon >= 40 or if lat <= -50 and lat >= -10:
            return('Hi you are outside the boundaries!')
        
        else:
            %run LOST-Copy1.py lon lat ttime duration radius object_type 'output_file' # Simulation with our model

        return (output_file.zarr)
    
    ### GET PROCESS
    
    def get(self):   #get request
        ## Load data
        out = xr.open_dataset('output_file_with_default_input.zarr')    ## output from LOST simulation      
        odata = xr.open_dataset('~/app/data/cmems_interp.nc') ## ocean data
        wdata = xr.open_dataset('~/app/data/era5.nc') ## wind data
        
        for i in range(len(out.time[0])):
            
        
            %pylab inline
            
            t = out.time[0][i].values
            print(t)

            fig, ax= plt.subplots(1, figsize=[15,8]) 

            X, Y = np.meshgrid(wdata.longitude, wdata.latitude)

            img0 = ax.imshow((odata.uo['time'==t][0]+odata.vo['time'==t][0])/2, extent=(odata.longitude.min().values, odata.longitude.max().values, odata.latitude.min().values, odata.latitude.max().values), origin='lower')

            ax.quiver(X, Y,wdata.u10['time'==t], wdata.v10['time'==t], color='b')

            plt.scatter(np.nanmean(out.lon[3],axis=0), np.nanmean(out.lat[3],axis=0), c='r')
            plt.show()
            
        return 
    

api.add_resource(Lost, '/lost')  #endpoints

if _name_ == '__main__':
    app.run()
            