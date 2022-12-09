import sys
from parcels import Field, FieldSet, ParticleSet, JITParticle
from parcels import RectilinearZGrid, plotTrajectoriesFile, AdvectionRK4,ErrorCode
import numpy as np
import os
from datetime import timedelta
import datetime
import xarray as xr
import netCDF4
from scipy import interpolate
import math
import pygmt
import parcels.rng as ParcelsRandom

def object_name(uw,vw,state):
    if state == 'PIW State Unknown':
        ang = 40
        uwi = ((uw * 0.01) + 0.08)*math.sin(ang)
        vwi = ((vw * 0.01) + 0.08)*math.cos(ang)
    elif state == 'PIW with lifejacket':
        ang = 45
        uwi = ((uw * 0.02))*math.sin(ang)
        vwi = ((vw * 0.02))*math.cos(ang)
    elif state == 'PIW verticle':
        ang = 25        
        uwi = ((uw * 0.01) + 0.08)*math.sin(ang)
        vwi = ((vw * 0.01) + 0.08)*math.cos(ang)
    elif state == 'PIW sitting \ huddled':
        ang = 25        
        uwi = ((uw * 0.02) + 0.01)*math.sin(ang)
        vwi = ((vw * 0.02) + 0.01)*math.cos(ang)
    elif state == 'PIW verticle':
        ang = 40
        uwi = ((uw * 0.02) + 0.08)*math.sin(ang)
        vwi = ((vw * 0.02) + 0.08)*math.cos(ang)
    elif state == 'No ballast pockets, general type':
        ang = 38
        uwi = ((uw * 0.05) + 0.03)*math.sin(ang)
        vwi = ((vw * 0.05) + 0.03)*math.cos(ang)
    elif state == 'No ballast pockets, no canopy, no drouge':
        ang = 32
        uwi = ((uw * 0.06) + 0.20)*math.sin(ang)
        vwi = ((vw * 0.06) + 0.20)*math.cos(ang)
    elif state == 'No ballast pockets, with canopy, with drouge':
        ang = 38
        uwi = ((uw * 0.03))*math.sin(ang)
        vwi = ((vw * 0.03))*math.cos(ang)
    elif state == 'Shallow ballast pocket with canopy, Capsized':
        ang = 12
        uwi = ((uw * 0.02) - 0.10)*math.sin(ang)
        vwi = ((vw * 0.02) - 0.10)*math.cos(ang)     
    elif state == '4 to 6 man, with canopy, with  drouge':
        ang = 20
        uwi = ((uw * 0.03) + 0.04)*math.sin(ang)
        vwi = ((vw * 0.03) + 0.04)*math.cos(ang)
    elif state == '15 to 25 man, with canopy, with  drouge':
        ang = 15
        uwi = ((uw * 0.04) + 0.08)*math.sin(ang)
        vwi = ((vw * 0.04) + 0.08)*math.cos(ang)
    elif state == '4 to 6 man, with canopy, no drouge':
        ang = 32
        uwi = ((uw * 0.04) + 0.12)*math.sin(ang)
        vwi = ((vw * 0.04) + 0.12)*math.cos(ang)
    elif state == 'Sea kayak, with person':
        ang = 20
        uwi = ((uw * 0.01) + 0.26)*math.sin(ang)
        vwi = ((vw * 0.01) + 0.26)*math.cos(ang)
    elif state == 'Homemade wood raft':
        ang = 25
        uwi = ((uw * 0.02) + 0.18)*math.sin(ang)
        vwi = ((vw * 0.02) + 0.18)*math.cos(ang)
    elif state == 'Homemade wood raft, with sail':
        ang = 45
        uwi = ((uw * 0.08) + 0.18)*math.sin(ang)
        vwi = ((vw * 0.08) + 0.18)*math.cos(ang)       
    elif state == 'Surfboard with person':
        ang = 20
        uwi = ((uw * 0.02))*math.sin(ang)
        vwi = ((vw * 0.02))*math.cos(ang)
    elif state == 'Windsurfer with person, sail and mast in the water':
        ang = 16
        uwi = ((uw * 0.03) + 0.1)*math.sin(ang)
        vwi = ((vw * 0.03) + 0.1)*math.cos(ang)
    elif state == 'Mono hull, keel, medium displacement':
        ang = 65
        uwi = ((uw * 0.04))*math.sin(ang)
        vwi = ((vw * 0.04))*math.cos(ang)     
    elif state == 'Enclosed Lifeboat':
        ang = 30
        uwi = ((uw * 0.04) - 0.08)*math.sin(ang)
        vwi = ((vw * 0.04) - 0.08)*math.cos(ang)
    elif state == 'Vessel with outboard motors no drouge':
        ang = 35
        uwi = ((uw * 0.07) + 0.04)*math.sin(ang)
        vwi = ((vw * 0.07) + 0.04)*math.cos(ang)
    elif state == 'Flat bottomed Boat, Boston whaler':
        ang = 30
        uwi = ((uw * 0.04) + 0.04)*math.sin(ang)
        vwi = ((vw * 0.04) + 0.04)*math.cos(ang)
    elif state == 'V hull boat':
        ang = 25
        uwi = ((uw * 0.0051) + 0.10)*math.sin(ang)
        vwi = ((vw * 0.0051) + 0.10)*math.cos(ang)
#     elif state == 'V hull boat':
#         uwi = (uw * 0.03) + 0.08
#         vwi = (vw * 0.03) + 0.08
    elif state == 'Sport fisher, centre open console':
        ang = 30
        uwi = ((uw * 0.06) + 0.09)*math.sin(ang)
        vwi = ((vw * 0.06) + 0.09)*math.cos(ang)
    elif state == 'Commercial fishing vessel type unknown':
        ang = 65
        uwi = ((uw * 0.04) + 0.06)*math.sin(ang)
        vwi = ((vw * 0.04) + 0.06)*math.cos(ang)
    elif state == 'Coastal freighter':
        ang = 65
        uwi = ((uw * 0.03))*math.sin(ang)
        vwi = ((vw * 0.03))*math.cos(ang)
    elif state == 'Fishing vessel general debris':
        ang = 15
        uwi = ((uw * 0.02))*math.sin(ang)
        vwi = ((vw * 0.02))*math.cos(ang)
    elif state == 'Cubic meter bait box, loading unknown':
        ang = 30
        uwi = ((uw * 0.04) + 0.04)*math.sin(ang)
        vwi = ((vw * 0.04) + 0.04)*math.cos(ang)
    else:
        print ("object note available")
    print (state)
    return uwi, vwi,state

def loading_data(longitude, latitude,
                 date='2021/05/15 00:00:00', period = '1',
                 ocean='cmems_interp.nc',
                 winds='era5.nc',
                 path = '../data/'):

    '''Function to load and interp appropriately the input data. 
    Usually this should remain untouched. To select an individual 
    wind and ocean product, simply change the path and file name.'''
    
    # Load ocean (nc) and winds (ds) data
    nc = xr.open_dataset(path+ocean)
    ds = xr.open_dataset(path+winds)
    
    # Select the appropriate time period for model
    start_date = datetime.datetime.strptime( date, '%Y/%m/%d %H:%M:%S')
    final_date = (datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S') + 
                  datetime.timedelta(days=np.float64(period)))
    
    if final_date > datetime.datetime.now() + datetime.timedelta(days=10):
        
        print('Forecast exceeds the limitation of currently available data '
              'try reduce the model run period')
        return
        
    nc = nc.sel(longitude=slice(longitude-10,longitude+10),
                latitude=slice(latitude-10,latitude+10),
                time=slice(start_date,final_date))
    ds = ds.sel(longitude=slice(longitude-10,longitude+10),
                latitude=slice(latitude+10,latitude-10),
                time=slice(start_date,final_date))
    
    uo = nc.uo.data
    vo = nc.vo.data
    uo[(uo==0)] = np.nan
    vo[(vo==0)] = np.nan
    lonu = nc.longitude.data
    latu = nc.latitude .data
    tim = nc.time

    # uw = ncw.ugrd10m.data
    # vw = ncw.vgrd10m.data/
    lonw = ds.longitude.data
    latw = ds.latitude.data

    timew = np.linspace(0,len(ds.time.data),len(ds.time.data))
    x = lonw
    y = latw
    xx, yy = np.meshgrid(x, y)

    t = timew

    uw = ds.u10
    vw = ds.v10

    lonU,latU = np.meshgrid(*(lonw,latw))
    lonU = np.ravel(lonU)
    latU = np.ravel(latU)

    uwind = np.zeros((len(nc.time),uo.shape[2], uo.shape[3]))
    vwind = np.zeros((len(nc.time),uo.shape[2], uo.shape[3]))
    reg = str(lonU.min())+"/"+str(lonU.max())+"/"+str(latU.min())+"/"+str(latU.max())+"/"

    for i in range(len(nc.time)):
        Uw = pygmt.blockmean(x=lonU,y=latU,z=np.ravel(uw[i]),spacing=1/12,region=reg)
        uwind[i] = pygmt.sphinterpolate(Uw)
        Vw = pygmt.blockmean(x=lonU,y=latU,z=np.ravel(vw[i]),spacing=1/12,region=reg)
        vwind[i] = pygmt.sphinterpolate(Vw)
    
    return uo,vo,uwind,vwind,lonu,latu,tim

def get_final_velocities(wu,wv,uo,vo):
    
    a = wu
    b = wv

    U = uo[:,0] +a
    V = vo[:,0] +b
    
    return(U,V)

def running_LOST(lon_dep,lat_dep,U,V,lon_grid,lat_grid,tim_grid,period,box_radius=0,output_file_name='output_file_name'):
    
    # Needed to add a bit of stochasticity
    Kh_zonal =      100 #2K(Zn + 0.5K'(Zn).math.fabs) For fixed values
    Kh_meridional = 100 #2K(Zn + 0.5K'(Zn).math.fabs) For fixed values

    def BrownianMotion2D(particle, fieldset, time):
        # Kernel for simple Brownian particle diffusion in zonal and meridional direction.
        # Assumes that fieldset has fields Kh_zonal and Kh_meridional
        r = 1/3.
        kh_meridional = fieldset.Kh_meridional[time,particle.depth,particle.lat,particle.lon]
        particle.lat += ParcelsRandom.uniform(-1., 1.)*math.sqrt(2*math.fabs(particle.dt)*kh_meridional/r)
        kh_zonal = fieldset.Kh_zonal[time,particle.depth,particle.lat,particle.lon]
        particle.lon += ParcelsRandom.uniform(-1., 1.)*math.sqrt(2*math.fabs(particle.dt)*kh_zonal/r)

    data = {'U': U, 'V': V}
    lon_s = lon_grid
    lat_s = lat_grid
    times = tim_grid

    dimensions = {'U': {'time':times,'lon': lon_s, 'lat': lat_s},
                  'V': {'time':times,'lon': lon_s, 'lat': lat_s}}
    fieldset = FieldSet.from_data(data, dimensions,allow_time_extrapolation=True)

    lonW = lon_dep - box_radius
    lonE = lon_dep + box_radius
    latS = lat_dep - box_radius
    latN = lat_dep + box_radius
    
    lons, lats = np.meshgrid(np.linspace(lonW,lonE,5), np.linspace(latS,latN,5))

    pset = ParticleSet.from_list(fieldset=fieldset, pclass=JITParticle, lon=lons, 
                                 lat=lats)#,time=518400 + 40680) # 12/10/22 @ 11h30
    
    file_name = output_file_name
    try: os.remove(file_name)
    except:  pass

    output_file = pset.ParticleFile(name=file_name,outputdt=timedelta(minutes=15))
    kernels = pset.Kernel(AdvectionRK4)#  + BrownianMotion2D
    
    def DeleteParticle(particle, fieldset, time):
        print("deleting particle at (%g %g %g) at %g" % (particle.lon, particle.lat, particle.depth, time))
        particle.delete()

    pset.execute(kernels, runtime=timedelta(days=period),dt=timedelta(hours=1),output_file=output_file,
                 recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle})
    
    print('lost has finished and data is stored in ' + str(file_name) + ".zarr")
    
def LOST(lon_dep,lat_dep,object_sar,date='2021/05/15 00:00:00',period=1,box_radius=0,output_file_name='output_file_name'):
    
    uo,vo,unew,vnew,lon_grid,lat_grid,tim_grid = loading_data(lon_dep,lat_dep,date = date, period=period)

    wu,wv,state = object_name(unew, vnew, state= object_sar)

    U,V = get_final_velocities(wu,wv,uo,vo)

    running_LOST(lon_dep,lat_dep,U,V,lon_grid,lat_grid,tim_grid,period,box_radius=box_radius,output_file_name=output_file_name)

print(sys.argv)
lon_dep    = np.float64(sys.argv[1]) # longitudinal position of particle deployment
lat_dep    = np.float64(sys.argv[2]) # latitudinal position of particle deployment
date       = sys.argv[3] # start date of simulation
period     = np.float64(sys.argv[4]) # length of run in days
box_radius = np.float64(sys.argv[5]) # deployment box (optional) radius in degrees
object_sar = sys.argv[6] # object needs to be chosen from the object_name function
output_file_name = sys.argv[7]

# example script: python LOST.py 10 -45 '2021/05/15 00:00:00' 2 4 'PIW State Unknown' "output_file"

print(lon_dep)
LOST(lon_dep,lat_dep,object_sar,date,period,box_radius,output_file_name)
