import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import ogr
from datetime import datetime

filepath = r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\GermanyDGM1\shapefiles\ruhr.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

data_source = driver.Open(filepath, 0)

x = [] #Latitude
y = [] #Latitude
z = [] #Time in minutes since start

counter = 0

for feat in data_source.GetLayer(0):
    pt = feat.geometry()
    x.append(pt.GetX())
    y.append(pt.GetY())
    time = feat.GetField('time')

    if (counter == 0):
        counter = 1
        start_dt = datetime.strptime(time, "%Y/%m/%d %H:%M:%S.%f")
        z.append(0.0)
    else:
        current_dt = datetime.strptime(time, "%Y/%m/%d %H:%M:%S.%f")
        diff = round(((current_dt - start_dt).total_seconds() / 60.0), 2)
        z.append(diff)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Minutes since start')

fig.suptitle('Space Time Cube')
plt.show()