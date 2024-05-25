import dask.array as da
import numpy as np

arr = da.random.random((10000, 10000), chunks=(1000, 1000))
sum = arr.sum()

print(sum.compute())
