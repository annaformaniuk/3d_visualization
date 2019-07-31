from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from osgeo import gdal, gdal_array

ds = gdal_array.LoadFile(r"F:\Dokumente\Uni_Msc\2019_SS\PIGIS\additional_assignment\GermanyDGM1\rasters\smallest.tif")
print(ds.shape)

# TODO: has to be resized if too big
# resized = np.resize(ds, (328, 336))

x, y = np.meshgrid(range(ds.shape[1]), range(ds.shape[0]), sparse=True)

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, ds)
plt.title('Flying Carpet')
plt.show()