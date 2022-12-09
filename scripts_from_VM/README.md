
How to Run LOST:

LOST needs certain variables from a user in order to run the simulations. 
These are the only things that need to be chosen and provided by a user. 
The rest of the code should be able to handle everything within. 

The objective of the hackathon is to create a frontend/API that allows a user to 
provide these variables to the python script that runs LOST (i.e. LOST.py)

In `~/app/data` we've provided data for a region between 0 and 40 Longitude and -50 and -10
Latitude, and dates from 2021-05-15 to 2021-05-25. Hence a user will be limited to that geographic 
extent and time period when running LOST simulations.

The LOST.py script takes the following command line arguments:

Longitude		- The longitude of deployment site
Latitude		- The latitude of deployment site
Start Date		- Start date and time of the deployment in this format "Year/Month/Day Hour:Minute:Second"
Duration		- Duration of the model run in days
Deployment radius	- Optional radius of the deployment of particles around a point
Object type		- The type of object to be deployed
Output file name	- The output file name which can be used for plotting


--------------------------------------


!! Note, this is all set up in a python environment so requires that user works in the `lost_hackathon` environment.
To active the `lost_hackathon` environment do:

	conda activate lost_hackathon

In the below example a LOST simulation is run, deploying virtual particles at 10E, 45S on 15 May 2021 at 00h00. 
The simulation will run for 2 days and deploy particles in a 4 degree radius around 10E, 45S. It will run the 
simulation for the 'PIW State Unknown' object and write the data to 'output_file'.

	python LOST.py 10 -45 '2021/05/15 00:00:00' 2 4 'PIW State Unknown' 'output_file'
	python LOST.py LONGITUDE LATITUDE "Start Date" "Duration" "Deployment Radius" "Object Type" "Output file name"
---------------------------------------

Created by: Michael Hart-Davis (michael.hart-davis@tum.de) and Bjorn Backeberg (bjorn.backeberg@deltares.nl). 
28/11/2022
