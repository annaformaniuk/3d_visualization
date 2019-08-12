import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import ogr
from datetime import datetime

def plot_cube(filepath):
    # load the shapefile
    driver = ogr.GetDriverByName('ESRI Shapefile')
    data_source = driver.Open(filepath, 0)

    x = [] # Latitude
    y = [] # Latitude
    z = [] # Time in minutes since start

    # counter to know when is the starting point
    counter = 0

    # calculate the time from the start to every next point
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

    # plot the space-time cube
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x,y,z)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Minutes since start')
    fig.canvas.set_window_title('Space-Time Cube')
    plt.show()

# specify path to the shapefile
path = r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\data\shapefiles\ruhr.shp"
plot_cube(path)