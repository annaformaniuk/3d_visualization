from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_coordinates(file, dx,dy):
    px = file.GetGeoTransform()[0]
    py = file.GetGeoTransform()[3]
    rx = file.GetGeoTransform()[1]
    ry = file.GetGeoTransform()[5]
    x = dx/rx + px
    y = dy/ry + py
    # print(x,y)
    return x,y

filepath = r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\GermanyDGM1\rasters\smallest.tif"
file = gdal.Open(filepath)
ds = gdal_array.LoadFile(filepath)
print(ds.shape)

axis1 = []
axis2 = []

for i in range(ds.shape[0]):
    axis1.append(get_coordinates(file, i, 0)[0])

for j in range(ds.shape[1]):
    axis2.append(get_coordinates(file, 0, j)[1])

print(axis1)
print(axis2)
x, y = np.meshgrid(axis2, axis1, sparse=True)

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, ds)
plt.title('Flying Carpet')
plt.show()