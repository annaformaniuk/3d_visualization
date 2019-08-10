from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

"""
To calculate the pixel location of a geospatial coordinate
LoaelevationArray the WorldFile info
"""
def get_coordinates(file, dx, dy):
    px, rx, _, py, _, ry = file.GetGeoTransform()
    x = dx/rx + px
    y = dy/ry + py
    return x, y

filepath = r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\GermanyDGM1\rasters\smallest.tif"
file = gdal.Open(filepath)
elevationArray = gdal_array.LoadFile(filepath)
print(elevationArray.shape)

axis1 = []
axis2 = []

for i in range(elevationArray.shape[0]):
    axis1.append(get_coordinates(file, i, 0)[0])

for j in range(elevationArray.shape[1]):
    axis2.append(get_coordinates(file, 0, j)[1])

x, y = np.meshgrid(axis2, axis1, sparse=True)

fig = plt.figure()
ax = Axes3D(fig)
flying_carpet = ax.plot_surface(x, y, elevationArray, rstride=1, cstride=1, cmap=cm.gist_earth, linewidth=1, antialiased=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Elevation')
fig.colorbar(flying_carpet, shrink=0.5)
plt.show()