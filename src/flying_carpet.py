from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

"""
To calculate the pixel location of a geospatial coordinate
Get the WorldFile info: Pixel width and height; 
as well as origin coordinates.
"""
def get_coordinates(file, dx, dy):
    px, rx, _, py, _, ry = file.GetGeoTransform()
    x = dx/rx + px
    y = dy/ry + py
    return x, y

# open and load the raster

def plot_carpet(filepath):
    file = gdal.Open(filepath)

    # elevation values
    elevationArray = gdal_array.LoadFile(filepath)
    print(elevationArray.shape)

    axis1 = []
    axis2 = []

    # append real-world coordinates of pixels
    for i in range(elevationArray.shape[0]):
        axis1.append(get_coordinates(file, i, 0)[0])

    for j in range(elevationArray.shape[1]):
        axis2.append(get_coordinates(file, 0, j)[1])

    # create the grid for the plot
    x, y = np.meshgrid(axis2, axis1, sparse=True)

    # plot the flying carpet
    fig = plt.figure()
    ax = Axes3D(fig)
    flying_carpet = ax.plot_surface(x, y, elevationArray, rstride=1, cstride=1, cmap=cm.gist_earth, linewidth=1, antialiased=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Elevation')
    fig.colorbar(flying_carpet, shrink=0.5)
    fig.canvas.set_window_title('Flying carpet')
    plt.show()

# specify the path to the raster
path = r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\data\rasters\smallest.tif"
plot_carpet(path)
